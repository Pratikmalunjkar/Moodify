# mood_map.py
import random

# Main mapping
EMOTION_KEYWORDS = {
    "happy":   ["feel good songs", "upbeat pop", "dance hits", "summer vibes"],
    "sad":     ["uplifting songs", "emotional ballads", "soft piano", "healing music"],
    "angry":   ["calm instrumental", "relaxing acoustic", "chill beats", "lofi to calm down"],
    "fear":    ["soothing piano", "comforting melodies", "ambient chill", "gentle acoustic"],
    "surprise":["trending now", "exciting tracks", "electro pop", "genre mashups"],
    "disgust": ["mood boosters", "positive vibes", "funk & groove", "good mood music"],
    "neutral": ["lofi chill", "easy listening", "background jazz", "chillhop"]
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
