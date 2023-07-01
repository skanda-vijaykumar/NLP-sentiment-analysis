import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
text = input("enter your comment")
scores = sid.polarity_scores(text)

print("Sentiment scores for the text: ", text)
print("Positive sentiment score: ", scores['pos'])
print("Neutral sentiment score: ", scores['neu'])
print("Negative sentiment score: ", scores['neg'])

if scores['compound'] >= 0.05:
    sentiment = "Positive"
elif scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"
    
print("Overall sentiment: ", sentiment)
