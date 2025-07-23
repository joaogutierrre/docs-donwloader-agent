import os
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse
import re
from pathlib import Path
import json
from smolagents import CodeAgent, DuckDuckGoSearchTool, PythonInterpreterTool

class VideoSDKDocsAgent:
    def __init__(self, base_urls):
        self.base_urls = base_urls
        self.base_domain = "https://docs.videosdk.live"
        self.downloaded_urls = set()
        self.docs_structure = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Initialize smolagents
        self.agent = CodeAgent(
            tools=[DuckDuckGoSearchTool(), PythonInterpreterTool()],
            model="gpt-4"
        )
    
    def clean_filename(self, filename):
        """Clean filename for Windows compatibility"""
        # Remove or replace invalid characters
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        filename = filename.strip('. ')
        return filename[:200]  # Limit length
    
    def extract_sidebar_links(self, url):
        """Extract all documentation links EXCLUSIVELY from sidebar"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Enhanced sidebar selectors - more comprehensive
            sidebar_selectors = [
                '.sidebar',
                '.navigation',
                '.nav-sidebar',
                '.docs-sidebar',
                '.docs-nav',
                '.side-nav',
                '.left-sidebar',
                '.main-nav',
                '[class*="sidebar"]',
                '[class*="navigation"]',
                '[class*="nav"]',
                '.menu',
                '.toc',
                '.table-of-contents',
                'nav[role="navigation"]',
                '[data-testid*="sidebar"]',
                '[data-testid*="nav"]',
                '.docusaurus-doc-sidebar',
                '.theme-doc-sidebar-container'
            ]
            
            links = set()
            sidebar_found = False
            
            # Try each selector to find the sidebar
            for selector in sidebar_selectors:
                sidebar_elements = soup.select(selector)
                if sidebar_elements:
                    sidebar_found = True
                    print(f"Found sidebar using selector: {selector}")
                    
                    for sidebar in sidebar_elements:
                        # Find all links in this sidebar element
                        for link in sidebar.find_all('a', href=True):
                            href = link['href']
                            # Handle relative URLs
                            if href.startswith('/'):
                                full_url = urljoin(self.base_domain, href)
                            elif href.startswith('http'):
                                full_url = href
                            else:
                                full_url = urljoin(url, href)
                            
                            # Only include VideoSDK documentation links
                            if 'docs.videosdk.live' in full_url and full_url != url:
                                links.add(full_url)
                                print(f"  Found sidebar link: {full_url}")
            
            if not sidebar_found:
                print(f"Warning: No sidebar found on {url}")
                # Fallback: look for any navigation-like structure
                nav_elements = soup.find_all(['nav', 'ul', 'ol'])
                for nav in nav_elements:
                    # Check if this nav contains multiple doc links
                    doc_links = nav.find_all('a', href=lambda x: x and ('/react/' in x or '/api-reference/' in x or '/guide/' in x))
                    if len(doc_links) > 3:  # Likely a navigation menu
                        print(f"Found potential navigation with {len(doc_links)} links")
                        for link in doc_links:
                            href = link['href']
                            if href.startswith('/'):
                                full_url = urljoin(self.base_domain, href)
                                if 'docs.videosdk.live' in full_url:
                                    links.add(full_url)
            
            print(f"Total sidebar links found from {url}: {len(links)}")
            return list(links)
            
        except Exception as e:
            print(f"Error extracting sidebar links from {url}: {e}")
            return []
    
    def get_page_content(self, url):
        """Extract main content from a documentation page"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                element.decompose()
            
            # Try different selectors for main content
            content_selectors = [
                '.main-content',
                '.content',
                '.documentation',
                '.docs-content',
                'main',
                '.markdown-body',
                '[role="main"]'
            ]
            
            content = None
            for selector in content_selectors:
                content_elem = soup.select_one(selector)
                if content_elem:
                    content = content_elem
                    break
            
            if not content:
                # Fallback: use body content
                content = soup.find('body')
            
            if content:
                # Convert to markdown-like format
                text_content = self.html_to_markdown(content)
                return text_content
            
            return ""
            
        except Exception as e:
            print(f"Error getting content from {url}: {e}")
            return ""
    
    def html_to_markdown(self, soup):
        """Convert HTML content to markdown format"""
        markdown_content = []
        
        for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'code', 'pre', 'blockquote']):
            if element.name.startswith('h'):
                level = int(element.name[1])
                markdown_content.append('#' * level + ' ' + element.get_text().strip())
                markdown_content.append('')
            elif element.name == 'p':
                text = element.get_text().strip()
                if text:
                    markdown_content.append(text)
                    markdown_content.append('')
            elif element.name in ['ul', 'ol']:
                for li in element.find_all('li', recursive=False):
                    prefix = '- ' if element.name == 'ul' else '1. '
                    markdown_content.append(prefix + li.get_text().strip())
                markdown_content.append('')
            elif element.name == 'code':
                markdown_content.append('`' + element.get_text() + '`')
            elif element.name == 'pre':
                code_text = element.get_text()
                markdown_content.append('```')
                markdown_content.append(code_text)
                markdown_content.append('```')
                markdown_content.append('')
            elif element.name == 'blockquote':
                lines = element.get_text().strip().split('\n')
                for line in lines:
                    if line.strip():
                        markdown_content.append('> ' + line.strip())
                markdown_content.append('')
        
        return '\n'.join(markdown_content)
    
    def create_folder_structure(self, url):
        """Create folder structure based on URL path"""
        parsed = urlparse(url)
        path_parts = [part for part in parsed.path.split('/') if part]
        
        # Create base docs folder
        base_folder = Path('videosdk_docs_final')
        current_path = base_folder
        
        for part in path_parts:
            if part and part != 'docs.videosdk.live':
                clean_part = self.clean_filename(part)
                current_path = current_path / clean_part
        
        return current_path
    
    def save_content(self, url, content):
        """Save content to appropriate folder structure"""
        if not content.strip():
            return
        
        folder_path = self.create_folder_structure(url)
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Create filename from URL
        parsed = urlparse(url)
        filename = parsed.path.split('/')[-1] or 'index'
        filename = self.clean_filename(filename)
        
        if not filename.endswith('.md'):
            filename += '.md'
        
        file_path = folder_path / filename
        
        # Add URL and title to content
        full_content = f"# {filename.replace('.md', '').replace('_', ' ').title()}\n\n"
        full_content += f"**Source URL:** {url}\n\n"
        full_content += content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"Saved: {file_path}")
    
    def download_all_docs(self):
        """Main method to download all documentation EXCLUSIVELY from sidebar links"""
        print("Starting VideoSDK documentation download...")
        print("FOCUS: Only downloading content from sidebar sections of the three specified URLs")
        
        # Clear any existing downloads to start fresh
        base_folder = Path('videosdk_docs_final')
        if base_folder.exists():
            import shutil
            shutil.rmtree(base_folder)
            print("Cleared existing downloads to start fresh")
        
        # Collect sidebar URLs ONLY from the three base URLs
        sidebar_urls = set()
        
        for base_url in self.base_urls:
            print(f"\n=== Analyzing sidebar from: {base_url} ===")
            sidebar_links = self.extract_sidebar_links(base_url)
            sidebar_urls.update(sidebar_links)
            print(f"Found {len(sidebar_links)} sidebar links from this page")
            time.sleep(2)  # Be respectful
        
        # Also include the base URLs themselves
        sidebar_urls.update(self.base_urls)
        
        print(f"\n=== TOTAL SIDEBAR URLS TO PROCESS: {len(sidebar_urls)} ===")
        
        # Sort URLs for organized processing
        sorted_urls = sorted(sidebar_urls)
        
        # Download content from each sidebar URL
        successful_downloads = 0
        failed_downloads = 0
        
        for i, url in enumerate(sorted_urls, 1):
            if url in self.downloaded_urls:
                continue
                
            print(f"\nProcessing {i}/{len(sorted_urls)}: {url}")
            
            content = self.get_page_content(url)
            if content and content.strip():
                self.save_content(url, content)
                self.downloaded_urls.add(url)
                successful_downloads += 1
                print(f"  ✅ Successfully downloaded and saved")
            else:
                failed_downloads += 1
                print(f"  ❌ Failed to get content or content was empty")
            
            time.sleep(1.5)  # Be respectful to the server
        
        # Clean up any .txt files and images
        self.cleanup_unwanted_files()
        
        # Create reference file
        self.create_reference_file()
        
        print(f"\n=== DOWNLOAD SUMMARY ===")
        print(f"Total URLs processed: {len(sorted_urls)}")
        print(f"Successful downloads: {successful_downloads}")
        print(f"Failed downloads: {failed_downloads}")
        print(f"Documentation download completed!")
        print(f"Check the 'videosdk_docs_final' folder for organized content.")
    
    def cleanup_unwanted_files(self):
        """Remove .txt files and images as requested"""
        base_folder = Path('videosdk_docs_final')
        if not base_folder.exists():
            return
        
        # Remove .txt files
        for txt_file in base_folder.rglob('*.txt'):
            txt_file.unlink()
            print(f"Removed .txt file: {txt_file}")
        
        # Remove image files
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico']
        for ext in image_extensions:
            for img_file in base_folder.rglob(f'*{ext}'):
                img_file.unlink()
                print(f"Removed image file: {img_file}")
    
    def create_reference_file(self):
        """Create a reference file showing the folder structure"""
        base_folder = Path('videosdk_docs_final')
        if not base_folder.exists():
            return
        
        reference_content = ["# VideoSDK Documentation Structure\n"]
        reference_content.append("This file shows the organization of the downloaded VideoSDK documentation.\n")
        reference_content.append("## Folder Structure\n")
        
        def add_folder_to_reference(folder_path, indent=0):
            items = []
            if folder_path.is_dir():
                for item in sorted(folder_path.iterdir()):
                    prefix = "  " * indent
                    if item.is_dir():
                        items.append(f"{prefix}- 📁 {item.name}/")
                        items.extend(add_folder_to_reference(item, indent + 1))
                    else:
                        items.append(f"{prefix}- 📄 {item.name}")
            return items
        
        structure_lines = add_folder_to_reference(base_folder)
        reference_content.extend(structure_lines)
        
        reference_file = base_folder / 'README.md'
        with open(reference_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(reference_content))
        
        print(f"Created reference file: {reference_file}")

# Main execution
if __name__ == "__main__":
    # URLs provided by the user
    base_urls = [
        "https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/concept-and-architecture",
        "https://docs.videosdk.live/react/api/sdk-reference/setup",
        "https://docs.videosdk.live/api-reference/realtime-communication/intro"
    ]
    
    # Create and run the agent
    agent = VideoSDKDocsAgent(base_urls)
    agent.download_all_docs()
    
    print("\n=== DOWNLOAD COMPLETE ===")
    print("All VideoSDK documentation has been downloaded and organized.")
    print("Check the 'videosdk_docs_final' folder for the organized content.")
    print("A README.md file has been created showing the folder structure.")