# KeyLogger-Python

A simple, cross-platform Python keylogger that records keystrokes to text files, with automatic file numbering for each run.

> **Disclaimer:** Use this tool only on devices you own or have explicit permission to monitor. Unauthorized monitoring may violate applicable laws.

## Features

- Records keystrokes in the order they are pressed.
- Pressing `Enter` starts a new line.
- Other keys are followed by a comma.
- The comma key is recorded as `comma`.
- The spacebar is recorded as `space`.
- Creates a new file for each run (`file1.txt`, `file2.txt`, etc.).
- Supports Windows, Linux, and macOS, subject to system permissions.

## Example

Typing `Hello, dear` produces:

    H,e,l,l,o,comma,space,d,e,a,r,

## Save Locations

| Operating System | Directory |
|---|---|
| Windows | `C:\Captures\` |
| Linux | `~/Captures/` |
| macOS | `~/Captures/` |

The capture directory is created automatically if it does not exist.

## Requirements

- Python 3.7+
- [`keyboard`](https://pypi.org/project/keyboard/) library

## Installation

Clone the repository and install the required dependency:

    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
    python -m pip install keyboard

## Usage

### Windows

    python script.py

### Linux

    sudo python3 script.py

### macOS

    python3 script.py

Replace `script.py` with your Python script's filename. Press `Ctrl + C` in the terminal to stop execution.

> **Note:** Keyboard monitoring may require additional permissions depending on your operating system.

## File Numbering

The script checks the capture directory and selects the next available sequential filename.

For example, if `file1.txt` through `file4.txt` already exist, the next run creates `file5.txt`. If no numbered files exist, numbering starts at `file1.txt`.
