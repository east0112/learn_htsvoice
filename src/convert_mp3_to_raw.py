import os
import subprocess
import argparse

def convert_mp3_to_raw(input_dir):
    raw_dir = os.path.join(input_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".mp3"):
            mp3_path = os.path.join(input_dir, file_name)
            wav_path = os.path.join(input_dir, file_name.replace(".mp3", ".wav"))
            raw_path = os.path.join(raw_dir, file_name.replace(".mp3", ".raw"))

            # Convert mp3 to wav
            subprocess.run(f"ffmpeg -i {mp3_path} -acodec pcm_s16le -ar 44100 {wav_path} > /dev/null 2>&1", shell=True, check=True)
            
            # Calculate volume
            vol = subprocess.check_output(f"sox {wav_path} -n stat -v 2>&1", shell=True, text=True)
            volGain = float(vol.strip()) / 2.86

            # Convert wav to raw
            subprocess.run(f"sox {wav_path} -t raw -r 16k -e signed-integer -b 16 -c 1 -B {raw_path} vol {volGain}", shell=True, check=True)
            
            # Remove wav file
            os.remove(wav_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert mp3 files to raw format.')
    parser.add_argument('inputDir', type=str, help='Directory containing mp3 files')
    args = parser.parse_args()

    convert_mp3_to_raw(args.inputDir)
