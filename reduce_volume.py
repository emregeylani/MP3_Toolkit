import sys
import os
import glob
from pydub import AudioSegment


def volume_down(mp3_file, percentage):
    sound = AudioSegment.from_file(mp3_file, format="mp3")
    reduction_db = 20 * (percentage / 100)  # Convert percentage to dB scale
    quieter_sound = sound - reduction_db
    
    output_file = get_output_filename(mp3_file)
    quieter_sound.export(output_file, format="mp3")
    print(f"Saved: {output_file}")


def regulate(mp3_files):
    volumes = []
    audio_segments = {}

    for mp3_file in mp3_files:
        sound = AudioSegment.from_file(mp3_file, format="mp3")
        volumes.append(sound.dBFS)
        audio_segments[mp3_file] = sound
    
    if not volumes:
        print("No files processed.")
        return
    
    min_volume = min(volumes)
    
    for mp3_file, sound in audio_segments.items():
        adjustment_db = min_volume - sound.dBFS
        adjusted_sound = sound + adjustment_db
        
        output_file = get_output_filename(mp3_file)
        adjusted_sound.export(output_file, format="mp3")
        print(f"Saved: {output_file}")


def get_output_filename(mp3_file):
    base, ext = os.path.splitext(mp3_file)
    return f"{base}_edited{ext}"


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python3 reduce_volume.py VOLUME_DOWN <mp3_file> <percentage>")
        print("  python3 reduce_volume.py REGULATE <mp3_files>")
        return
    
    command = sys.argv[1].upper()
    
    if command == "VOLUME_DOWN" and len(sys.argv) == 4:
        mp3_file = sys.argv[2]
        try:
            percentage = float(sys.argv[3])
            volume_down(mp3_file, percentage)
        except ValueError:
            print("Invalid percentage value.")
    elif command == "REGULATE" and len(sys.argv) >= 3:
        mp3_files = glob.glob(sys.argv[2])
        regulate(mp3_files)
    else:
        print("Invalid command or arguments.")


if __name__ == "__main__":
    main()

