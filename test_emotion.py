from deepface import DeepFace

result = DeepFace.analyze(img_path="smile.jpg", actions=["emotion"], enforce_detection=False)

if isinstance(result, list):
    print("Dominant Emotion:", result[0]['dominant_emotion'])
else:
    print("Dominant Emotion:", result['dominant_emotion'])
