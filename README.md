## A python based CLI game launcher

**Why I built this?** 

I created this because other flashy UI-based solutions like Playnite were painfully slow and took too long to load due to various issues. From the very beginning, I wanted a CLI-oriented/styled tool, which I ended up building myself

**It supports:**
- Independently manageable ASCII art and menu colors
- Custom ASCII art from art.txt
- Custom games from apps folder

**Note:** It is designed for Windows Terminal, which is required for accurate color rendering and proper ASCII art display. Currently uses solutions that only work on Windows.

**Image:**

<img width="1170" height="819" alt="image" src="https://github.com/user-attachments/assets/4cfb8edf-9015-46ce-a262-d71c2c292702" />

## Quick Start / Running:

**Prerequisites:**
- Windows and Python
- Pylnk3
- Pathlib
- Colorama

**How to run:**

1. Download and extract the archive.
2. Edit art.txt and settings.conf as desired.
3. Place your game icons into the apps folder.
4. Open Windows Terminal and navigate to the folder containing the files from the terminal.
5. Run the application using the .\PythonCGLI.exe command.

**setting.conf help:**

| Line     | Function |
| ---      | ---       |
| 1. line | The ASCII art color |
| 2. line | The Menu color      |
| 3. line | The Background color|
