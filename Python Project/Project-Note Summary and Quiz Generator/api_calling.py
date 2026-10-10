from google import genai
from dotenv import load_dotenv
import os

# env file loading
load_dotenv()

# api key read kora
my_api_key = os.getenv("GEMINI_API_KEY")

# client intializing
client = genai.Client(api_key=my_api_key)


# note generator
def note_generator(images):

    prompt = """Summarize the picture in note format at max 100 words
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        # model="gemini-3.8-flash",
        contents=[images,prompt],
    )

    return response.text