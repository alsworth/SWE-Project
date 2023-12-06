import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from sklearn.decomposition import LatentDirichletAllocation
from textblob import TextBlob
from gensim import corpora
import gensim

# Preprocessing Function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = [word for word in text.split() if word not in ENGLISH_STOP_WORDS]
    return text

# Function to perform sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.1:
        return 'Positive'
    elif analysis.sentiment.polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Function to display topics
def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print(f"Topic {topic_idx}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))

if __name__ == '__main__':
    # Load the CSV file
    file_path = 'chatgpt_reviews(1).csv'  
    data = pd.read_csv(file_path)

    # Combine title and review, then preprocess
    data['combined_review'] = data['title'] + ' ' + data['review']
    data['processed_review'] = data['combined_review'].apply(preprocess_text)

    # Vectorize the text
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    processed_docs = [' '.join(text) for text in data['processed_review']]
    X = vectorizer.fit_transform(processed_docs)

    # Perform LDA
    optimal_num_topics = 3  # Use the optimal number of topics determined
    lda = LatentDirichletAllocation(n_components=optimal_num_topics, random_state=0)
    lda.fit(X)

    # Assign the most dominant topic to each review
    topic_results = lda.transform(X)
    data['topic'] = topic_results.argmax(axis=1)

    # Perform sentiment analysis
    data['sentiment'] = data['combined_review'].apply(analyze_sentiment)

    # Display topics
    print("LDA Topics:")
    display_topics(lda, vectorizer.get_feature_names_out(), no_top_words=10)

    # Aggregate sentiment analysis by topic
    sentiment_by_topic = data.groupby('topic')['sentiment'].value_counts(normalize=True).unstack().fillna(0)
    print("\nSentiment by Topic:")
    print(sentiment_by_topic)


