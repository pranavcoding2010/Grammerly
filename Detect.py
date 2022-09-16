from textblob import TextBlob
a = TextBlob("bonjour")
print(a.detect_language())