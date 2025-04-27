import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.ensemble import RandomForestRegressor
from data import user_df, posts_df, messages_df
from textblob import TextBlob

model = SentenceTransformer('all-MiniLM-L6-v2')

def euclidean_distance(loc1, loc2):
    return np.linalg.norm(np.array(loc1) - np.array(loc2))

def get_distances(user):
    user_location = user_df.loc[user_df['id'] == user, 'location'].iloc[0]
    other_users = user_df[user_df['id'] != user].copy()

    other_users['distance'] = other_users['location'].apply(lambda loc: euclidean_distance(user_location, loc))

    return other_users[['id', 'distance']]


print((get_distances(1)))