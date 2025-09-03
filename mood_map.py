# mood_map.py
import random

# Main mapping
EMOTION_KEYWORDS = {
    "happy": [
        "Hindi upbeat songs",
        "Marathi dance hits",
        "Bollywood party tracks",
        "Zingaat style songs"
    ],
    "sad": [
        "Hindi emotional songs",
        "Bollywood heartbreak",
        "Marathi soulful tracks",
        "Agar Tum Saath Ho type songs"
    ],
    "angry": [
        "Gully Boy rap",
        "Bollywood intense songs",
        "Marathi power tracks",
        "Malhari style music"
    ],
    "fear": [
        "Hindi calming music",
        "Marathi soothing melodies",
        "Bollywood comfort songs",
        "soft acoustic Hindi tracks"
    ],
    "surprise": [
        "Trending Hindi songs",
        "Bollywood mashups",
        "Marathi pop fusion",
        "Ritviz style music"
    ],
    "disgust": [
        "Mood booster Hindi songs",
        "Positive Marathi tracks",
        "Bollywood funk",
        "feel good Indian music"
    ],
    "neutral": [
        "Hindi lo-fi",
        "Marathi chillhop",
        "Bollywood easy listening",
        "background Indian jazz"
    ]
}


# Handle alternate labels (just in case)
ALIASES = {
    "joy": "happy",
    "happiness": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fearful": "fear",
    "contempt": "disgust",
    "calm": "neutral"
}

def normalize_emotion(e: str) -> str:
    if not e:
        return "neutral"
    e = e.strip().lower()
    return ALIASES.get(e, e if e in EMOTION_KEYWORDS else "neutral")

def query_for_emotion(emotion: str) -> str:
    """Return one keyword phrase chosen at random for the given emotion."""
    base = normalize_emotion(emotion)
    return random.choice(EMOTION_KEYWORDS[base])
