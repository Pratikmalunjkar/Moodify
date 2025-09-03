# app.py

import streamlit as st
from deepface import DeepFace
from PIL import Image
import numpy as np
import requests
from mood_map import query_for_emotion
from history import init_db, add_record, fetch_history, clear_history

API_KEY = st.secrets["API_KEY"]  # ✅ Securely stored in Streamlit secrets

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


# ------------------ Streamlit UI ------------------

st.set_page_config(page_title="Moodify Phase 5", layout="centered")
init_db()  # ✅ Initialize DB on app start

st.title("🎶 Moodify: Emotion-Based Music Recommender")

# Tabs for better navigation
tab1, tab2 = st.tabs(["🎭 Detect Mood", "📜 Mood History"])


# ------------------ Tab 1: Detect Mood ------------------
with tab1:
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
                result = DeepFace.analyze(
                    img_path=np.array(image),
                    actions=['emotion'],
                    enforce_detection=False,
                    detector_backend='opencv'
                )
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

                    # ✅ Save to local database
                    add_record(dominant_emotion, title, link)

            except Exception as e:
                st.error(f"Emotion detection failed: {e}")
    else:
        st.info("Please upload an image or take a photo to begin.")


# ------------------ Tab 2: Mood History ------------------
with tab2:
    st.subheader("📜 Your Mood History")

    history = fetch_history()
    if history:
        for emotion, title, link, timestamp in history:
            st.markdown(f"**{timestamp}** — 🎭 *{emotion.capitalize()}*")
            st.markdown(f"- [{title}]({link})")

        if st.button("🗑️ Clear History"):
            clear_history()
            st.success("History cleared! Refresh the app to see changes.")
    else:
        st.info("No history found yet. Start detecting moods to build your history!")
