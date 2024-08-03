import subprocess
from pathlib import Path

script_dir = Path.cwd()
# Automatically find Rhubarb
rhubarb_path = [p for p in script_dir.glob("**/rhubarb") if p.is_file()][0]

# Select English or Non-English
while True:
    english = input("Are your voice recordings in English? (Y/N)")
    if english in "yY":
        command = [rhubarb_path, "-f", "tsv", "-o"]
        break
    elif english in "nN":
        command = [rhubarb_path, "-r", "phonetic", "-f", "tsv", "-o"]
        break
    else:
        continue

# Iterate through characters and voice files
for voice_dir in (script_dir.parent / "audio" / "voice").iterdir():
    if voice_dir.is_dir():
        character = voice_dir.name
        output_dir = script_dir / "lip-sync-data" / character
        # Create the corresponding directory structure in the output path    
        output_dir.mkdir(exist_ok=True)
        for audio_path in voice_dir.iterdir():
            if audio_path.suffix in [".ogg", ".wav"] and audio_path.is_file():
                output_path = (output_dir / audio_path.name).with_suffix(".txt")
                process = command + [output_path, audio_path]
                # Run Rhubarb to generate lipsync data
                subprocess.run(process, check=True)
