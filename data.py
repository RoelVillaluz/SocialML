import datetime
import random
import numpy as np
import pandas as pd

users = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "name": ['prince', 'sam', 'elrey', 'jomari', 'joms', 'khian', 'mark', 'vince', 'leonard', 'arjay', 'josh'],
    "location": [[1 , 3], [2, 5], [-9, -6], [-3, -2], [12, 10], [14, 11], [1, 4], [5, 6], [4, 4], [6, 6], [6, 7]],

    "friends": [[2, 3], # prince
                [1, 2, 4, 5],     # sam
                [1],           # elrey
                [2],           # jomari
                [2, 6],        # joms
                [5, 7],        # khian
                [6, 8, 9],     # mark
                [7],           # vince
                [7, 10],       # leonard
                [9, 11],       # arjay
                [10]]        # josh
}

posts = {
    "id": list(range(201, 231)),
    "author_type": [
        "user", "page", "user", "user", "page",
        "user", "user", "page", "user", "user",
        "page", "user", "user", "page", "user",
        "page", "user", "page", "page", "user",
        "user", "page", "user", "user", "page",
        "user", "page", "user", "page", "user"
    ],
    "author_id": [
        2, 101, 11, 5, 102,
        1, 6, 103, 8, 10,
        104, 3, 7, 105, 9,
        106, 11, 107, 102, 2,
        5, 101, 10, 6, 103,
        8, 104, 1, 105, 9
    ],
    "interactions": [
        [{"user_id": 1, "type": "like"}, {"user_id": 2, "type": "comment"}],
        [{"user_id": 3, "type": "share"}],
        [{"user_id": 5, "type": "like"}, {"user_id": 1, "type": "comment"}],
        [{"user_id": 6, "type": "comment"}, {"user_id": 7, "type": "share"}],
        [{"user_id": 3, "type": "like"}],
        [{"user_id": 4, "type": "share"}, {"user_id": 2, "type": "like"}],
        [{"user_id": 1, "type": "comment"}],
        [{"user_id": 9, "type": "like"}, {"user_id": 10, "type": "comment"}],
        [],
        [{"user_id": 1, "type": "like"}, {"user_id": 6, "type": "share"}],
        [{"user_id": 8, "type": "comment"}],
        [{"user_id": 2, "type": "like"}],
        [{"user_id": 4, "type": "comment"}, {"user_id": 5, "type": "like"}],
        [{"user_id": 3, "type": "share"}],
        [],
        [{"user_id": 6, "type": "like"}],
        [{"user_id": 7, "type": "comment"}],
        [],
        [{"user_id": 2, "type": "like"}, {"user_id": 8, "type": "share"}],
        [{"user_id": 1, "type": "comment"}],
        [{"user_id": 3, "type": "like"}],
        [{"user_id": 5, "type": "share"}, {"user_id": 7, "type": "comment"}],
        [],
        [{"user_id": 4, "type": "like"}],
        [{"user_id": 2, "type": "share"}],
        [{"user_id": 8, "type": "like"}],
        [],
        [{"user_id": 9, "type": "comment"}],
        [{"user_id": 5, "type": "share"}],
        [{"user_id": 6, "type": "like"}]
    ]
}

messages = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    "sender_id": [1, 2, 1, 3, 5, 6, 1, 2, 3, 1, 4, 4, 5, 2, 1, 3, 5, 6, 1, 2, 1, 3, 2, 4, 6, 5, 1, 2, 1, 3, 5, 2, 6, 4, 1, 3, 5, 2, 4, 6],
    "receiver_id": [2, 1, 3, 1, 6, 5, 2, 1, 1, 3, 1, 5, 4, 1, 2, 1, 6, 5, 4, 1, 2, 1, 3, 2, 6, 5, 1, 2, 1, 3, 5, 2, 6, 4, 1, 3, 5, 2, 4, 6],
    "content": [
        "Hey, how are you doing today?", "Fine", "Did you see the new update?", "Yup, looks cool!", 
        "Meeting at 6pm. Don’t be late!", "Ok", "Let’s team up for the project.", "Sure", 
        "I'll send the file soon.", "Did you understand the lesson?", "That movie was absolutely amazing!", 
        "I’m so frustrated with this app crashing again.", "Thank you for always helping me, it means a lot.", 
        "Ugh. I hate dealing with this every day.", "You’re the best teammate I’ve ever had.", 
        "This is hopeless. I’ve tried everything.", "I’m excited for our trip next week!", 
        "Whatever. I don’t care anymore.", "Let’s grab coffee and catch up soon.", "Why do you keep ignoring me?", 
        "Can we talk later about the project?", "Sure, call me when you're free.", 
        "That was really helpful, thanks!", "Not sure if this is going to work...", 
        "I don't want to deal with this right now.", "Looking forward to next weekend!", 
        "I’ll check in on this tomorrow.", "What time are we meeting?", "I don’t know how to fix this...", 
        "It’s been a long day, let's chat tomorrow.", "Are you free next week?", 
        "Let’s catch up over the weekend!", "Can we meet up in the next few days?", 
        "This isn’t working out, I’m sorry.", "It’s been too long, let’s talk soon!", 
        "Just got back from the trip, let’s chat.", "I’ll reach out soon!", "Feeling overwhelmed with everything.", 
        "I think we need a break from all of this.", "Let's make plans for next month."
    ],
    "date_sent": [
        "2025-04-27 10:00:00", "2025-04-27 10:05:00", "2025-04-27 10:20:00", "2025-04-27 10:45:00", 
        "2025-04-27 12:30:00", "2025-04-27 14:00:00", "2025-04-27 14:30:00", "2025-04-27 15:00:00", 
        "2025-04-27 15:30:00", "2025-04-27 16:15:00", "2025-04-27 18:00:00", "2025-04-27 20:00:00", 
        "2025-04-28 10:00:00", "2025-04-29 09:30:00", "2025-04-30 11:00:00", "2025-05-02 13:00:00", 
        "2025-05-05 15:00:00", "2025-05-10 17:00:00", "2025-05-12 18:30:00", "2025-05-15 20:00:00", 
        "2025-05-16 08:00:00", "2025-05-20 10:00:00", "2025-05-22 14:00:00", "2025-05-25 18:00:00", 
        "2025-05-28 10:30:00", "2025-06-01 09:00:00", "2025-06-03 15:00:00", "2025-06-05 16:00:00", 
        "2025-06-08 17:30:00", "2025-06-10 20:00:00", "2025-06-15 21:30:00", "2025-06-17 22:00:00", 
        "2025-06-20 23:00:00", "2025-06-22 10:00:00", "2025-06-25 12:00:00", "2025-06-28 14:00:00", 
        "2025-07-02 16:00:00", "2025-07-05 18:00:00", "2025-07-08 20:00:00", "2025-07-10 12:00:00"  
    ]
}


user_df = pd.DataFrame(users)
posts_df = pd.DataFrame(posts)
messages_df = pd.DataFrame(messages)