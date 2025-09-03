# Moodify
AI-Based Music Recommender Based on User’s Mood

## Phase 1: Planning & Setup
- Finalized scope: Mood-based music recommender
- Repo created
- Platform chosen: Streamlit
- Model chosen: DeepFace (FER-2013)


✅ Phase 2: Emotion Detection

Built Streamlit UI with:

📂 Image upload

📷 Webcam capture (st.camera_input)

Processed input image with DeepFace

Displayed detected dominant emotion (Happy, Sad, Angry, etc.)

Fixed deprecated warnings (use_container_width)

Error handling for cases where no face is detected

📄 Final File: app.py

✅ Phase 3: Music Recommendation

Integrated YouTube Data API

Created a mood → music mapping dictionary (mood_map.py)

Fetches top 5 songs from YouTube matching user’s detected mood

Displays results in Streamlit with two modes:

▶️ Embedded video

🎞️ Clickable thumbnail with link

Error handling for API quota issues or missing results

📄 Final File: app_phase3.py


---

## ✅ Phase 4: Deployment

* 📦 Added `requirements.txt` with all required dependencies (`deepface`, `tensorflow`, `tf-keras`, `opencv-python-headless`, `pillow`, `requests`, `streamlit`)
* 🛠️ Added `runtime.txt` to specify Python version (`python-3.11`) for deployment
* 🌐 Deployed successfully on **Streamlit Cloud**
* 📱 Verified **mobile-friendly support** → Upload & camera input works directly on phone
* 🐞 Fixed deployment issues:

  * TensorFlow + tf-keras compatibility
  * OpenCV import error (`opencv-python-headless`)

### 🌍 Live App Features after Deployment

* Upload or capture an image (desktop/mobile)
* Detect **dominant emotion** using DeepFace
* Fetch and display **YouTube music recommendations** based on mood

📄 **Files Involved:**

* `app.py` → Main Streamlit application
* `requirements.txt` → Dependencies list
* `runtime.txt` → Python version configuration

---

✅ Phase 5: User History & Profile  

- Integrated **SQLite database** (`history.db`) for storing user’s detected moods and recommended songs.  
- Created `history.py` to handle database functions (init, add record, fetch history).  
- Updated `app.py` to:
  - Save each detected **emotion + recommended song** with timestamp.  
  - Display a **📜 Mood History** section inside the Streamlit app.  
- Users can now view their **past moods** and the songs recommended at that time.  



Deployed on Streamlit Cloud
.
Works on desktop & mobile (camera + gallery input supported).

👨‍💻 Author

Pratik Chandrabhan Malunjkar
MCA Student | Data & Cloud Enthusiast
GitHub: Pratikmalunjkar
