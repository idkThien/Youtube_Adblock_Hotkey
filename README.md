# YouTube Ad Blocker

A Python-based tool that helps you skip YouTube ads by automatically clicking through the ad interface. This tool works by simulating mouse clicks to navigate through YouTube's ad interface and skip ads.

## Features

- Works with multiple browsers (Chrome, Firefox, Edge, Opera, Safari, Brave, Internet Explorer)
- Simple hotkey-based operation
- Automatically detects when YouTube is the active window
- Tries multiple click positions to handle different YouTube layouts

## Requirements

- Python 3.8 or higher
- Windows operating system
- One of the supported browsers with YouTube open

## Installation

1. Clone this repository
2. Install the required packages using pipenv:
   ```
   pipenv install
   ```
   or using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you have a YouTube tab open in your browser
2. Run the script:
   ```
   python ad_blocker.py
   ```
3. When an ad appears, press the backtick key (`) to trigger the ad blocker
4. Press 'Esc' to exit the program

## How It Works

The script uses PyAutoGUI to simulate mouse movements and clicks to:
1. Click the "i" button in the ad
2. Navigate to the "Stop seeing this ad" option
3. Click through any confirmation dialogs
4. Close any remaining ad interfaces

## Notes

- The script only works when a YouTube tab is the active window in your browser
- It may not work with all types of YouTube ads
- Use at your own discretion and in accordance with YouTube's terms of service

## Troubleshooting

If the script isn't working:
1. Make sure a YouTube tab is active in your browser
2. Check that your screen resolution is supported
3. Try running the script as administrator
4. Ensure all required packages are installed correctly 