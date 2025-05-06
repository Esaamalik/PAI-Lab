import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()
text = "I love programming in Python. It's so versatile and easy to use!"

sentiment = sia.polarity_scores(text)

if sentiment['compound'] >= 0.05:
    print("Positive sentiment")
elif sentiment['compound'] <= -0.05:
    print("Negative sentiment")
else:
    print("Neutral sentiment")