from flask import Flask, request, jsonify
from emotion import emotion_detector

app = Flask(__name__)

@app.route("/emotion", methods=["POST"])
def detect_emotion():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Input text tidak ditemukan"}), 400
    try:
        result = emotion_detector(data["text"])
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)