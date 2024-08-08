from TTS.api import TTS
import os

def transcribe_text(text, output_file, speaker_name, language='en'):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)  # Set gpu=False if not using GPU
    tts.tts_to_file(
        text=text,
        file_path=output_file,
        speaker=speaker_name,
        language=language,
        split_sentences=True
    )

def main():
    speakers = ['Abrahan Mack', 'Baldur Sanjin', 'Tanja Adelina', 'Viktor Menelaos', 'Chandra MacFarland']
    
    while True:
        # 1. Get the text input from the user
        text = input("Please enter the text for the voiceover: ")
        
        # 2. Display the speaker options
        print("\nAvailable speakers:")
        for idx, speaker in enumerate(speakers, 1):
            print(f"{idx}. {speaker}")
        
        # 3. Get the speaker choice from the user
        while True:
            try:
                speaker_choice = int(input("\nChoose a speaker by entering the corresponding number: "))
                if 1 <= speaker_choice <= len(speakers):
                    speaker_name = speakers[speaker_choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # 4. Get the output file name from the user
        output_name = input("\nEnter a name for the output file (without extension): ").strip()
        output_file = os.path.join("output", f"{output_name}.wav")
        
        # 5. Transcribe the text to speech
        transcribe_text(text, output_file, speaker_name)

        print(f"\nVoiceover generated and saved to: {output_file}\n")

        # 6. Ask if the user wants to generate another voiceover
        another = input("Do you want to generate another voiceover? (y/n): ").strip().lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
