"""
Library import 
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def homepage():
    """
    method to return index.html
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def index():
    """
    Function to elaborate form string to call API request and return result to the view
    """
    requests = request.args.get('textToAnalyze')
    response = emotion_detector(requests)
    if not response['dominant_emotion']:
        return (
        f"For the given statement, the system response is:<br>"
        f" - 'Anger': {response['anger']},<br>"
        f" - 'Disgust': {response['disgust']},<br>"
        f" - 'Fear': {response['fear']},<br>"
        f" - 'Joy': {response['joy']},<br>"
        f" - 'Sadness': {response['sadness']}.<br>"
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
        "<h3 style=color:red;>Invalid text! Please try Again</h3>")
    return (
    f"For the given statement, the system response is:<br>"
    f" - 'Anger': {response['anger']},<br>"
    f" - 'Disgust': {response['disgust']},<br>"
    f" - 'Fear': {response['fear']},<br>"
    f" - 'Joy': {response['joy']},<br>"
    f" - 'Sadness': {response['sadness']}.<br>"
    f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )

if __name__ == "__main__":
    app.run(debug=True)
