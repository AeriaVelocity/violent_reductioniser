# Violent Reductioniser

Violent Reductioniser is a tool built with Python/Tkinter to compress and reduce
video files to an absurd degree, utilising FFmpeg for the most top-of-the-line
video frick-up-er-y.

If you didn't get that, it's a tool that uses FFmpeg, which is an audio/video
processing and manipulation toolkit, to compress and reduce videos to an
incredibly small file size, often resulting in the finalised video having
ludicrously reduced quality and low-fidelty ("tinny") audio.

This tool is primarily meant for comedic and educational purposes, both to
easily make a video file extremely compressed, and to learn how to interact
with FFmpeg using a simple GUI.

This app contains translations for US English (changes "Reductioniser" to
"Reductionizer", etc.). Contributions are welcome for other locales.

## Requirements

- Python 3.5+ (3.8+ recommended)
- FFmpeg
  - On Windows, [install it from here](https://ffmpeg.org/download.html#build-windows).
  - On Linux, install it from your package manager.
    - On Debian and Ubuntu, it's `sudo apt install ffmpeg`.
    - On Fedora, it's `sudo dnf install ffmpeg`. Older versions use `yum`.
    - On Arch, it's `sudo pacman -S ffmpeg`.
    - On Alpine, it's `apk add ffmpeg`.
  - On macOS, install it from [Homebrew](https://brew.sh/) with `brew install ffmpeg`.
  - If you want, [install it from source](https://ffmpeg.org/download.html).
  - After installing, run `ffmpeg -version` in your terminal to check if it's there.
- Tkinter
  - Your Python installation should already have Tkinter pre-installed, but it's
  easy to install it with [pip](https://pip.pypa.io/en/stable/installing/) if
  you don't have it.

## Usage

To run the app from source, run `run.py` with your Python interpreter
(python.exe on Windows, python3 on everything else).

```sh
python3 run.py
```

Type in the absolute or relative path to the input video file and the
destination file you want to output to, or use their respective `Browse...`
buttons to launch a file browser.

Violent Reductioniser recommends MPEG-4 (*.mp4), WebM (*.webm) and MKV (*.mkv)
video files, though other formats may be supported as long as they're supported
by FFmpeg.

When your files are selected, click on the `Reductionise` button. This launches
the FFmpeg process in the background.

When the reductionisation process is complete, a success popup will appear,
and you'll be able to view the video at your chosen destination.

## Licence

This project is licensed under the [GNU General Public License version 3 or later](https://www.gnu.org/licenses/gpl-3.0.en.html).

This means you're allowed to use the program for whatever you want, make as many
copies as you want, distribute it wherever you want and modify it however you
want. The only thing you're not allowed to do is change the licence to a more
restrictive one (i.e. one that isn't free/libre/open source).
