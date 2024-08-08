import warnings
import os
import sys
from TTS.api import TTS

# Suppress warnings
warnings.filterwarnings("ignore")

# Redirect stderr to null to suppress unwanted messages
sys.stderr = open(os.devnull, 'w')

def transcribe_text(text, output_file, speaker_name, language='en'):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    tts.tts_to_file(
        text=text,
        file_path=output_file,
        speaker=speaker_name,
        language=language,
        split_sentences=True
    )

while True:
    text = input("Please enter the text for the voiceover: ")
    
    speakers = ['Abrahan Mack', 'Baldur Sanjin', 'Tanja Adelina', 'Viktor Menelaos', 'Chandra MacFarland']
    
    print("\nAvailable speakers:")
    for idx, speaker in enumerate(speakers, 1):
        print(f"{idx}. {speaker}")
    
    speaker_choice = int(input("\nChoose a speaker by entering the corresponding number: ")) - 1
    speaker_name = speakers[speaker_choice]
    
    output_name = input("\nEnter a name for the output file (without extension): ")
    output_file = f"output/{output_name}.wav"
    
    transcribe_text(text, output_file, speaker_name)
    
    print(f"\nVoiceover generated and saved to: {output_file}\n")

    new_voiceover = input("Do you want to generate another voiceover? (yes/no): ").strip().lower()
    if new_voiceover not in ["y", "yes"]:
        break

# Restore stderr
sys.stderr = sys.__stderr__
