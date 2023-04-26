import streamlit as st
import requests
import os

api_key = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
data = response.json()

title = data["title"]
image_url = data["hdurl"]
explanation = data["explanation"]

# Download the image
img_response = requests.get(image_url)
img_content = img_response.content
with open("image.jpg", "wb") as file:
    file.write(img_content)

st.title(title)
st.image("image.jpg")
st.write(explanation)
