import random

# Main mapping — English only
EMOTION_KEYWORDS = {
    "happy": [
        "English feel-good pop",
        "Happy English hits",
        "Upbeat Western music",
        "Positive pop anthems",
        "Danceable English tracks"
    ],
    "sad": [
        "English sad songs",
        "Western breakup ballads",
        "Emotional English music",
        "Soft acoustic heartbreak",
        "Melancholic indie tracks"
    ],
    "angry": [
        "English rock anthems",
        "Aggressive rap tracks",
        "Western pump-up music",
        "Intense metal songs",
        "Hard-hitting hip hop"
    ],
    "fear": [
        "English chill music",
        "Relaxing Western acoustic",
        "Soothing English melodies",
        "Comforting indie folk",
        "Gentle ambient tracks"
    ],
    "surprise": [
        "Viral English hits",
        "Surprising Western mashups",
        "English genre-bending music",
        "Unexpected pop remixes",
        "Experimental indie sounds"
    ],
    "disgust": [
        "English funk pop",
        "Feel-good Western tracks",
        "Uplifting English music",
        "Mood booster pop",
        "Fresh indie grooves"
    ],
    "neutral": [
        "English lo-fi beats",
        "Western chillhop",
        "Soft English background music",
        "Ambient instrumental tracks",
        "Easy listening pop"
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
