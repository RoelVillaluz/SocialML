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

    # Remove self-messages (user talking to themselves)
    user_conversations = user_conversations[user_conversations['sender_id'] != user_conversations['receiver_id']]
    
    # Calculate sentiment and length features
    user_conversations['sentiment'] = user_conversations['content'].apply(lambda x: TextBlob(x).sentiment.polarity)
    user_conversations['length'] = user_conversations['content'].apply(len)
    user_conversations['weighted_sentiment'] = user_conversations['sentiment'] * user_conversations['length']

    # Set the conversation_score to NaN initially
    user_conversations['conversation_score'] = np.nan

    # Group by the user and the other user they communicated with
    user_conversations['other_user'] = user_conversations.apply(lambda row: row['receiver_id'] if row['sender_id'] == user else row['sender_id'], axis=1)

    # Calculate average time between replies between users
    user_conversations['date_sent'] = pd.to_datetime(user_conversations['date_sent']) # Convert date_sent to datetime
    user_conversations = user_conversations.sort_values(by='date_sent')

    # Calculate time differences between replies for each pair
    user_conversations['time_diff'] = user_conversations.groupby('other_user')['date_sent'].diff().dt.total_seconds()

    # Now compute the average time between replies per user pair
    avg_reply_time = user_conversations.groupby('other_user')['time_diff'].mean().reset_index()
    avg_reply_time.columns = ['other_user', 'avg_reply_seconds']

    # Invert time to make faster replies have higher values
    avg_reply_time['inv_reply_time'] = 1 / avg_reply_time['avg_reply_seconds']

    # Merge inverse reply time back to each message
    user_conversations = user_conversations.merge(avg_reply_time[['other_user', 'inv_reply_time']], on='other_user', how='left')

    scaler = StandardScaler()
    # Don't scale sentiment anymore since it's already scaled from -1 (negative) to 1 (positive)
    user_conversations[['length', 'weighted_sentiment', 'inv_reply_time']] = scaler.fit_transform(user_conversations[['length', 'weighted_sentiment', 'inv_reply_time']])

    X = user_conversations[['sentiment', 'length', 'weighted_sentiment', 'inv_reply_time']]

    y = user_conversations['sentiment'] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)

    predicted_scores = model.predict(X)

    user_conversations['conversation_score'] = predicted_scores

    # Group by the other users and sum the conversation scores
    total_scores = user_conversations.groupby('other_user')['conversation_score'].sum().reset_index()
    total_scores.columns = ['other_user', 'total_conversation_score'] 

    # Merge with avg reply time
    total_scores = total_scores.merge(avg_reply_time[['other_user', 'avg_reply_seconds']], on='other_user', how='left')

    # Merge with user_df to get the name of the other user
    total_scores = total_scores.merge(user_df[['id', 'name']], left_on='other_user', right_on='id', how='left')
    total_scores = total_scores.drop(columns=['id']) # Remove redundant ID column
    total_scores = total_scores.rename(columns={'name': 'other_user_name'})

    # Reorder for clarity
    total_scores = total_scores[['other_user', 'other_user_name', 'avg_reply_seconds', 'total_conversation_score']]

    return total_scores

def calculate_user_interaction_scores(user):
    return

print(calculate_conversation_scores(1))