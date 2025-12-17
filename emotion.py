from watson_nlp import EmotionPredictor

def emotion_detector(text):
    predictor = EmotionPredictor.from_pretrained(
        "emotion_predictor_workflow_lang_en_stock"
    )
    result = predictor.run(text)
    emotions = result['emotion']
    dominant = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant
    return emotions