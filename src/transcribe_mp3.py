import os
import argparse
from google.cloud import speech

def transcribe_mp3(input_dir, service_account_json):
    txt_dir = os.path.join(input_dir, "txt")
    os.makedirs(txt_dir, exist_ok=True)

    client = speech.SpeechClient.from_service_account_file(service_account_json)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".mp3"):
            mp3_path = os.path.join(input_dir, file_name)
            txt_file_name = file_name.replace(".mp3", ".txt")
            txt_path = os.path.join(txt_dir, txt_file_name)

            with open(mp3_path, 'rb') as audio_file:
                content = audio_file.read()

            audio = speech.RecognitionAudio(content=content)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.MP3,
                sample_rate_hertz=44100,
                language_code="ja-JP"
            )

            try:
                response = client.recognize(config=config, audio=audio)
                
                with open(txt_path, 'w') as txt_file:
                    if not response.results:
                        print(f"No results for {file_name}")
                    for result in response.results:
                        txt_file.write(result.alternatives[0].transcript + '\n')

            except Exception as e:
                print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe MP3 audio files to text using Google Speech to Text API.')
    parser.add_argument('inputDir', type=str, help='Directory containing MP3 files')
    parser.add_argument('serviceAccountJson', type=str, help='Path to Google Speech to Text API service account JSON file')

    args = parser.parse_args()
    transcribe_mp3(args.inputDir, args.serviceAccountJson)
