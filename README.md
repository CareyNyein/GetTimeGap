# Subtitle Gap Finder
 Python script to analyze  subtitle files and detect gaps between subtitles for ad placement. Designed to locate sufficient pauses for inserting commercials without disrupting the flow of the content.

## Overview
Subtitle Gap Finder is a Python utility for analyzing `.srt` subtitle files to identify gaps between subtitles longer than a user-specified duration. This tool is perfect for editors and developers working with time-sensitive subtitle adjustments.

## Features
- Efficiently parses `.srt` subtitle files using regular expressions.
- Identifies gaps between subtitle timestamps exceeding a given duration (in seconds).
- Provides clear output specifying where the gap is found.

## Installation
### Prerequisites
- Python 3.6 or above
- Basic knowledge of command-line usage

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/subtitle-gap-finder.git
   ```
2. Navigate to the project directory
   ```bash
   cd GetTimeGap
   ```
### Usage

## Running the Script
1. Place you `.srt` subtitle file in the same directory as the script
2. Run the program:
   ```bash
   python getTimeGap.py
   ```
3. Provide the required inputs:
   * Subtitle file name (without extension)
   * Total gap duration in seconds
4. Review the output for details gaps found

### Example Input
```bash
Enter subtitle file name (without extension):
>>> sample_subtitle
Enter total gap you want to find (in seconds):
>>> 10
```

### Example Output
```bash
The 10-second gap found at line 25, starts from 00:12:34.545
```

### License
This project is licensed under the MIT License. See `LICENSE` for more details.

### Contact
If you encounter any issues or have suggestions, feel free to reach out:
* Email - scrn.carey@gmail.com
