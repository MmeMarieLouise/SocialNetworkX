import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)


# constructor
class Member:
    def __init__(self, id, name, handle, bio, location, url, date, followers, following):
        self.id = id
        self.name = name
        self.handle = handle
        self.bio = bio
        self.location = location
        self.url = url
        self.date = date
        self.followers = followers
        self.following = following


# Object instantiation
Member_1 = Member(config.USER_ID,
                  'Marie-Louise',
                  '@MmeMarieLouise',
                  'Data Scientist @UKCivilService| Global Council member @pyladies | Proud #Mama. Views are my own. '
                  'She / Her',
                  'London,UK',
                  'https://linktr.ee/MmeMarieLouise',
                  'May 2016',
                  client.get_users_followers(id=config.USER_ID),
                  client.get_users_following(id=config.USER_ID))


print(f'{Member_1.followers}')
print(f'{Member_1.following}')
