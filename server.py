from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector


app = Flask(__name__)

@app.route('/')
def emotionDetector():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
  
    text_to_analyze = request.args.get('textToAnalyze', default='', type=str)

    if not text_to_analyze:
        return jsonify({'error': 'Missing "textToAnalyze" parameter'}), 400

    result = emotion_detector(text_to_analyze)

    emotions_str = ", ".join([f"'{emotion}': {score}" for emotion, score in result.items() if emotion != 'dominant_emotion'])
    dominant_emotion = result.get('dominant_emotion')

    response_str = f"For the given statement, the system response is {emotions_str}. The dominant emotion is {dominant_emotion}."
    return response_str


if __name__ == '__main__':
    app.run(debug=True)