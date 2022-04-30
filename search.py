import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
query = 'pyladies OR PyLadies'
#response = client.search_recent_tweets(query=query)
users = client.get_users(usernames=['MmeMarielouise'])

for user in users:
    print(user)
timeline = client.get_users_tweets(id=config.USER_ID)

for post in timeline.data:
    print(post)

followers = client.get_users_followers(id=config.USER_ID)

for follow in followers.data:
    print(follow)

#for tweet in response.data:
   # print(tweet)