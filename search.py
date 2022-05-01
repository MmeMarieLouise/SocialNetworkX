import tweepy
import config

# instantiate client
client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
query = 'pyladies OR PyLadies'
# response = client.search_recent_tweets(query=query)
users = client.get_users(usernames=['MmeMarielouise'], user_fields=['username'])
# test = client.get_user(id=config.USER_ID, user_fields=['id'])

print(users.data)


def pull_id():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
    test = client.get_user(username='MesrenyameDogbe')
    return test.data.id


print(pull_id())


def pull_name():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
    test = client.get_user(username='MesrenyameDogbe')
    return test.data.name


print(pull_name())

# tweets = client.search_recent_tweets(query=query,tweet_fields=['context_annotations', 'created_at'],
# expansions='entities.mentions.username', max_results=10, user_fields=['username']

member_2 = client.get_user(username='MesrenyameDogbe')

# member_21 = client.get_user( username='MesrenyameDogbe', expansions, tweet_fields, user_fields)

# for i_d in ident.data:
# print(i_d)

for user in users.data:
    print(f'handle:@{user}')

timeline = client.get_users_tweets(id=config.USER_ID)

for post in timeline.data:
    print(post)

followers = client.get_users_followers(id=config.USER_ID)

for follow in followers.data:
    print(follow)

# for tweet in response.data:
# print(tweet)
