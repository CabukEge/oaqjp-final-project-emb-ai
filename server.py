''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the labels and its confidence 
        scores for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return_string = "Invalid text! Please try again!"
    else:
        dominant_emotion_string = response['dominant_emotion']

        emotions_only = response.copy()
        emotions_only.pop("dominant_emotion")

        emotions_only_string = ""
        for key, value in emotions_only.items():
            emotions_only_string += f"\'{key}\': {value}, "
        emotions_only_string = emotions_only_string[:-2]

        return_string = f'For the given statement, the system response is {emotions_only_string}. \
        The dominant emotion is <b>{dominant_emotion_string}</b>.'

    return return_string

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
