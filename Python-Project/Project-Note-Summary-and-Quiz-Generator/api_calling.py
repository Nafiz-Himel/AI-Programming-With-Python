from google import genai
from dotenv import load_dotenv
import os, io
from gtts import gTTS

# env file loading
load_dotenv()

# api key read kora
my_api_key = os.getenv("GEMINI_API_KEY")

# client intializing
client = genai.Client(api_key=my_api_key)


# note generator
def note_generator(images):

    prompt = """Summarize the picture in note format in Bangla at max 100 words
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[images,prompt],
    )

    return response.text

def audio_transcription(text):
    speech = gTTS(text,lang='bn',slow=False)

    # speech.save("welcome.mp3")
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_generator(images,difficulty):
    prompt = f"Generate 3 quizzes in Bangla based on the {difficulty}. Make sure to add markdown to differentiate the options. And correct answer too"
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[images,prompt],
    )
    
    return response.text
