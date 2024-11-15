"""
This module provides a Flask application for emotion detection.
"""

import logging
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Handle POST requests to detect emotions in text.

    Returns:
        JSON response containing emotion scores or error messages.
    """
    app.logger.debug("Received request")
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    if not text_to_analyze:
        app.logger.debug("No text provided")
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response})

if __name__ == '__main__':
    app.logger.info("Starting Flask server...")
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)
