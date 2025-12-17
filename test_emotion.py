from emotion import emotion_detector

def test_emotion_detector():
    result = emotion_detector("I am very happy today")
    assert "joy" in result