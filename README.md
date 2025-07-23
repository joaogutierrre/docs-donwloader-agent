# VideoSDK Documentation Downloader Agent

An intelligent agent that automatically downloads and organizes VideoSDK documentation from their official website. This tool extracts content exclusively from sidebar navigation sections and converts it into well-structured markdown files.

## 🚀 Features

- **Smart Sidebar Extraction**: Automatically identifies and extracts links from documentation sidebars
- **Intelligent Content Parsing**: Converts HTML documentation to clean markdown format
- **Organized File Structure**: Creates hierarchical folder structure based on URL paths
- **Content Filtering**: Removes unwanted files (.txt, images) and focuses on documentation content
- **Progress Tracking**: Real-time progress updates during download process
- **Reference Generation**: Creates a README with complete folder structure overview
- **Respectful Scraping**: Implements delays between requests to be server-friendly

## 📋 Prerequisites

- Python 3.7 or higher
- Internet connection
- pip package manager

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/joaogutierrre/docs-donwloader-agent.git
   cd docs-downloader-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Quick Start

Run the agent using the convenient runner script:

```bash
python run_agent.py
```

This will:
1. Install required dependencies automatically
2. Start the documentation download process
3. Create organized folder structure in `videosdk_docs_final/`

### Manual Execution

Alternatively, run the agent directly:

```bash
python agent_videosdk_docs.py
```

## 📁 Project Structure

```
docs-downloader-agent/
├── agent_videosdk_docs.py    # Main agent implementation
├── run_agent.py              # Convenient runner script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── videosdk_docs_final/      # Generated documentation (after running)
    ├── README.md             # Auto-generated structure overview
    ├── react/                # React SDK documentation
    ├── api-reference/        # API reference documentation
    ├── android/              # Android SDK documentation
    ├── ios/                  # iOS SDK documentation
    ├── flutter/              # Flutter SDK documentation
    ├── python/               # Python SDK documentation
    ├── javascript/           # JavaScript SDK documentation
    ├── react-native/         # React Native SDK documentation
    ├── unity/                # Unity SDK documentation
    ├── prebuilt/             # Prebuilt components documentation
    └── ai_agents/            # AI agents documentation
```

## 🔧 Configuration

The agent is pre-configured to download from these VideoSDK documentation sections:

- React SDK Guide and API Reference
- Real-time Communication API Reference
- Concept and Architecture Documentation

To modify the target URLs, edit the `base_urls` list in `agent_videosdk_docs.py`:

```python
base_urls = [
    "https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/concept-and-architecture",
    "https://docs.videosdk.live/react/api/sdk-reference/setup",
    "https://docs.videosdk.live/api-reference/realtime-communication/intro"
]
```

## 📊 Output

After successful execution, you'll find:

- **Organized Documentation**: All content structured in logical folders
- **Markdown Files**: Clean, readable documentation in markdown format
- **Reference File**: Auto-generated README.md showing complete structure
- **Progress Reports**: Console output showing download statistics

## 🛡️ Features in Detail

### Smart Content Extraction
- Identifies sidebar navigation elements using multiple CSS selectors
- Handles both static and dynamic navigation structures
- Converts HTML to clean markdown with proper formatting

### File Organization
- Creates folder structure based on URL hierarchy
- Sanitizes filenames for cross-platform compatibility
- Removes duplicate content and unwanted file types

### Error Handling
- Graceful handling of network errors
- Retry mechanisms for failed downloads
- Detailed logging of success/failure rates

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This tool is designed for educational and documentation purposes. Please respect the VideoSDK website's terms of service and robots.txt file. The tool implements respectful scraping practices with delays between requests.

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed via `pip install -r requirements.txt`
2. **Network Errors**: Check internet connection and try again
3. **Permission Errors**: Ensure write permissions in the project directory
4. **Empty Content**: Some pages might have dynamic content that requires JavaScript

### Getting Help

If you encounter issues:
1. Check the console output for detailed error messages
2. Verify all dependencies are correctly installed
3. Ensure you have write permissions in the project directory
4. Open an issue on GitHub with detailed error information

---

**Made with ❤️ for the VideoSDK developer community**