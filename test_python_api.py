# app_phase3.py

import streamlit as st
from deepface import DeepFace
from PIL import Image
import numpy as np
import requests
from mood_map import query_for_emotion

# Securely load API key from Streamlit secrets
API_KEY = st.secrets["AIzaSyDK11-b7ly53Q7_fK0Gu6WZXqhb1OUbcSo"]

def get_music_by_emotion(emotion, api_key, max_results=5):
    query = query_for_emotion(emotion)
    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&q={requests.utils.quote(query)}"
        f"&type=video&maxResults={max_results}&key={api_key}"
    )
    response = requests.get(url)
    data = response.json()

    results = []
    if "items" in data:
        for item in data["items"]:
            title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            link = f"https://www.youtube.com/watch?v={video_id}"
            thumbnail = f"https://img.youtube.com/vi/{video_id}/0.jpg"
            results.append((title, link, thumbnail))
    return results

# Streamlit UI
st.set_page_config(page_title="Moodify Phase 3", layout="centered")
st.title("🎶 Moodify: Emotion-Based Music Recommender")

st.markdown("Upload a face image or take a photo to detect your mood and get music recommendations.")

# Step 1: Ask user to choose input method
input_choice = st.radio("How would you like to provide your image?", ["📁 Upload", "📷 Camera"])

# Step 2: Show input based on choice
image = None
if input_choice == "📁 Upload":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

elif input_choice == "📷 Camera":
    camera_image = st.camera_input("Take a photo")
    if camera_image is not None:
        image = Image.open(camera_image)

# Step 3: Display and process image
if image is not None:
    st.image(image, caption="Input Image", use_container_width=True)

    with st.spinner("🔍 Detecting emotion..."):
        try:
            result = DeepFace.analyze(img_path=np.array(image), actions=['emotion'], enforce_detection=False)
            dominant_emotion = result[0]['dominant_emotion']
            st.success(f"🎭 Detected Emotion: **{dominant_emotion.capitalize()}**")

            songs = get_music_by_emotion(dominant_emotion, API_KEY)
            st.subheader("🎧 Recommended Songs:")

            display_mode = st.radio("Choose display style:", ["▶️ Embedded Video", "🎞️ Clickable Thumbnail"])

            for title, link, thumbnail in songs:
                st.markdown(f"**{title}**")
                if display_mode == "▶️ Embedded Video":
                    st.video(link)
                else:
                    st.markdown(f"[![Thumbnail]({thumbnail})]({link})")

        except Exception as e:
            st.error(f"Emotion detection failed: {e}")
else:
    st.info("Please upload an image or take a photo to begin.")
