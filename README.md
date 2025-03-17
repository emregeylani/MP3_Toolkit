# MP3 Tool Kit

MP3 Tool Kit is a Python 3 script that allows you to edit MP3 files by adjusting their volume. It supports two main operations:

1. **VOLUME_DOWN**: Reduces the maximum volume of an MP3 file by a specified percentage.
2. **REGULATE**: Adjusts multiple MP3 files to match the lowest volume among them.

## Requirements

- Python 3
- `pydub` library
- `ffmpeg` installed on your system

### Install dependencies
```sh
pip install pydub
```
Ensure `ffmpeg` is installed and accessible via command line:
```sh
ffmpeg -version
```
If not installed, you can install it via:
- **Linux (Ubuntu/Debian)**: `sudo apt install ffmpeg`
- **Mac (Homebrew)**: `brew install ffmpeg`
- **Windows**: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add it to your system path.

## Usage

### Reduce Volume (VOLUME_DOWN)
```sh
python3 reduce_volume.py VOLUME_DOWN <mp3_file> <percentage>
```
**Example:** Lower volume of `song.mp3` by 20%
```sh
python3 reduce_volume.py VOLUME_DOWN song.mp3 20
```
_Output:_ `song_edited.mp3`

### Normalize Volume Across Files (REGULATE)
```sh
python3 reduce_volume.py REGULATE <mp3_files>
```
**Example:** Normalize volume for all MP3 files in the current directory:
```sh
python3 reduce_volume.py REGULATE "*.mp3"
```
_Each file will be saved with `_edited.mp3` appended to its name._

## Notes
- Running the script multiple times overwrites existing `_edited.mp3` files.
- Volume reduction is calculated in decibels (dB).
- The script automatically detects the lowest volume in the provided MP3s for normalization.

## License
This project is open-source and free to use.


