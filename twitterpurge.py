import tweepy
from datetime import datetime, timedelta
import time

consumer_key = "KEY"
consumer_secret = "SECRET"
access_token = "TOKEN"
access_token_secret = "SECRET TOKEN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

ticker = 0

friends = api.friends_ids(USER ID)

with open("friends.txt", "r") as r:
    for line in r:
        user = api.user_timeline(line)
        status = user[0]
        time_gap = datetime.now() - status.created_at
        if time_gap.days > 14:
            with open("rejects.txt", "a") as f:
                name = api.get_user(line)
                username = name.screen_name
                f.write("@" + str(username) + "\n")
                print(username)
        ticker += 1
        print("tick: " + str(ticker))
        time.sleep(5)
