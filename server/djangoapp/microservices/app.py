from flask import Flask
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import json
import os

app = Flask("Sentiment Analyzer")

# Ensure nltk data paths include local sentiment folder or download vader_lexicon
local_sentiment_dir = os.path.join(os.path.dirname(__file__))
nltk.data.path.append(local_sentiment_dir)

try:
    sia = SentimentIntensityAnalyzer()
except LookupError:
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()


@app.get('/')
def home():
    return "Welcome to the Sentiment Analyzer. \
    Use /analyze/text to get the sentiment"


@app.get('/analyze/<input_txt>')
def analyze_sentiment(input_txt):
    scores = sia.polarity_scores(input_txt)
    print(scores)
    pos = float(scores['pos'])
    neg = float(scores['neg'])
    neu = float(scores['neu'])
    res = "positive"
    print("pos neg neu ", pos, neg, neu)
    if (neg > pos and neg > neu):
        res = "negative"
    elif (neu > neg and neu > pos):
        res = "neutral"
    res = json.dumps({"sentiment": res})
    print(res)
    return res


if __name__ == "__main__":
    app.run(debug=True, port=5050)
