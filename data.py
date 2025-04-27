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
    "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    "author_id": [2, 4, 11, 5, 5, 1, 2, 6, 8, 10, 7, 9, 3, 1, 2, 4, 10, 11, 6, 2],
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
        [{"user_id": 1, "type": "comment"}]
    ]
}

messages = {
    "id": list(range(1, 21)),
    "sender_id": [1, 2, 1, 3, 5, 6, 1, 2, 3, 1, 4, 4, 5, 2, 1, 3, 5, 6, 1, 2],
    "receiver_id": [2, 1, 3, 1, 6, 5, 2, 1, 1, 3, 1, 5, 4, 1, 2, 1, 6, 5, 4, 1],
    "content": [
        "Hey, how are you doing today?",                  # neutral
        "Fine",                                           # short, dry
        "Did you see the new update?",                   # curious
        "Yup, looks cool!",                              # mild positive
        "Meeting at 6pm. Don’t be late!",                # assertive
        "Ok",                                             # neutral
        "Let’s team up for the project.",                # collaborative
        "Sure",                                           # agreeable
        "I'll send the file soon.",                      # neutral
        "Did you understand the lesson?",                # question
        "That movie was absolutely amazing!",            # strong positive
        "I’m so frustrated with this app crashing again.", # frustrated
        "Thank you for always helping me, it means a lot.", # emotional, grateful
        "Ugh. I hate dealing with this every day.",       # strong negative
        "You’re the best teammate I’ve ever had.",       # emotional positive
        "This is hopeless. I’ve tried everything.",       # sad, defeated
        "I’m excited for our trip next week!",           # excited
        "Whatever. I don’t care anymore.",               # detached
        "Let’s grab coffee and catch up soon.",          # warm
        "Why do you keep ignoring me?"                   # confrontational
    ]
}


user_df = pd.DataFrame(users)
posts_df = pd.DataFrame(posts)
messages_df = pd.DataFrame(messages)