#!/usr/bin/env python3
"""
VideoSDK Documentation Download Agent Runner

This script runs the VideoSDK documentation download agent that:
1. Analyzes the sidebar structure of VideoSDK documentation
2. Downloads all documentation pages as markdown files
3. Organizes content in a hierarchical folder structure
4. Removes unwanted .txt files and images
5. Creates a reference file showing the organization
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False
    return True

def run_agent():
    """Run the VideoSDK documentation agent"""
    print("Starting VideoSDK Documentation Download Agent...")
    try:
        subprocess.check_call([sys.executable, "agent_videosdk_docs.py"])
        print("Agent completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running agent: {e}")
        return False
    return True

if __name__ == "__main__":
    print("VideoSDK Documentation Download Agent")
    print("=====================================")
    
    # Check if requirements.txt exists
    if Path("requirements.txt").exists():
        if not install_requirements():
            sys.exit(1)
    
    # Run the agent
    if run_agent():
        print("\n✅ Documentation download completed successfully!")
        print("📁 Check the 'videosdk_docs_final' folder for organized content")
        print("📄 See README.md for the folder structure reference")
    else:
        print("\n❌ Agent execution failed")
        sys.exit(1)