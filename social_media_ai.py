import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from data import user_df, posts_df, messages_df
from textblob import TextBlob

model = SentenceTransformer('all-MiniLM-L6-v2')
scaler = StandardScaler()

def euclidean_distance(loc1, loc2):
    return np.linalg.norm(np.array(loc1) - np.array(loc2))

def get_distances(user):
    user_location = user_df.loc[user_df['id'] == user, 'location'].iloc[0]
    other_users = user_df[user_df['id'] != user].copy()

    other_users['distance'] = other_users['location'].apply(lambda loc: euclidean_distance(user_location, loc))

    return other_users[['id', 'distance']]

def calculate_conversation_scores(user):
    # Filter conversations of the user
    user_conversations = messages_df[(messages_df['sender_id'] == user) | (messages_df['receiver_id'] == user)].copy()

    # Calculate sentiment and length features
    user_conversations['sentiment'] = user_conversations['content'].apply(lambda x: TextBlob(x).sentiment.polarity)
    user_conversations['length'] = user_conversations['content'].apply(len)
    user_conversations['weighted_sentiment'] = user_conversations['sentiment'] * user_conversations['length']

    # Set the conversation_score to NaN initially
    user_conversations['conversation_score'] = np.nan

    scaler = StandardScaler()
    # Don't scale sentiment anymore since it's already scaled from -1 (negative) to 1 (positive)
    user_conversations[['length', 'weighted_sentiment']] = scaler.fit_transform(user_conversations[['length', 'weighted_sentiment']])

    X = user_conversations[['sentiment', 'length', 'weighted_sentiment']]

    y = user_conversations['sentiment'] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)

    predicted_scores = model.predict(X)

    user_conversations['conversation_score'] = predicted_scores

    return user_conversations

print(calculate_conversation_scores(1))