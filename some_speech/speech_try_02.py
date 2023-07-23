"""

some speech try 02

"""


from gtts import gTTS
import os


def text_to_speech(text, language='en', output_file='output.mp3'):
    try:
        # Create a gTTS object with the text and language
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the audio file
        tts.save(output_file)
        print(f"Text-to-speech conversion successful. Saved to {output_file}")

        # Play the audio (optional)
        # os.system(f"start {output_file}")  # For Windows
        # os.system(f"xdg-open {output_file}")  # For Linux
        # os.system(f"open {output_file}")  # For macOS

    except Exception as e:
        print("Error occurred during text-to-speech conversion:", e)


if __name__ == "__main__":
    input_text = "You are the most beautiful in the world"
    text_to_speech(input_text, language='en', output_file='output.mp3')

