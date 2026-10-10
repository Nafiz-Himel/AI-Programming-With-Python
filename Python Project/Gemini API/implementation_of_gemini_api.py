import streamlit as st
from google import genai
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Give me an idea of Gemini API in 100 words"
)

st.title("Response from ai-model:",anchor=False)
st.markdown(response.text)


# from google import genai
# import os 
# from dotenv import load_dotenv

# load_dotenv()

# # Environment variable থেকে নিজে থেকেই API key নিয়ে নেবে, 
# # তবে চাইলে explicitভাবেও পাস করতে পারেন:
# client = genai.Client()

# interaction = client.interactions.create(
#     model="gemini-3.8-flash",
#     input="Explain how AI works in a few words"
# )

# print(interaction.output_text)
