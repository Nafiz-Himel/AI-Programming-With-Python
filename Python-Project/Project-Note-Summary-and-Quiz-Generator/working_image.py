import streamlit as st

from google import genai
from dotenv import load_dotenv
import os

from PIL import Image
#Image ekta method

# env file loading
load_dotenv()

# api key read kora
my_api_key = os.getenv("GEMINI_API_KEY")

# client intializing
client = genai.Client(api_key=my_api_key)



images = st.file_uploader(
        "Upload the photos of your note",
        type=["jpg","jpeg",'png'],
        accept_multiple_files = True,
    )

print(type(images))

if images:
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    # print(type(images))

    prompt = """Summarize the picture in note format at max 100 words
        make sure to add necessary markdown to differentiate different section"""
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        # model="gemini-3.8-flash",
        contents=[pil_images,prompt],
    )
    st.markdown(response.text)