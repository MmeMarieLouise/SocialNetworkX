import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)


# constructor
class Member:
    def __init__(self, name, handle, bio, location, url, date, followers, following):
        self.name = name
        self.handle = handle
        self.bio = bio
        self.location = location
        self.url = url
        self.date = date
        self.followers = followers
        self.following = following

    def id(self):
        info = tweepy.Client(bearer_token=config.BEARER_TOKEN)
        member_handle = self.handle
        detail = info.get_user(username=member_handle)
        ident = detail.data.id
        return print(ident)

    def social_name(self):
        info = tweepy.Client(bearer_token=config.BEARER_TOKEN)
        member_handle = self.handle
        detail = info.get_user(username=member_handle)
        names = detail.data.name
        return print(names)

    def social_handle(self):
        info = tweepy.Client(bearer_token=config.BEARER_TOKEN)
        member_handle = self.handle
        detail = info.get_user(username=member_handle)
        handles = detail.data.username
        return print(handles)

    def biog(self):
        info = tweepy.Client(bearer_token=config.BEARER_TOKEN)
        member_handle = self.handle
        detail = info.get_user(username=member_handle)
        ident = detail.data.id
        response = client.get_users(ids=ident, user_fields=["description"])
        for user in response.data:
            bio = user.description
            return print(bio)

    def loc(self):
        info = tweepy.Client(bearer_token=config.BEARER_TOKEN)
        member_handle = self.handle
        detail = info.get_user(username=member_handle)
        ident = detail.data.id
        response = client.get_users(ids=ident, user_fields=["location"])
        for user in response.data:
            loca = user.location
            return print(loca)

    def link(self):
        info = tweepy.Client(bearer_token=config.BEARER_TOKEN)
        member_handle = self.handle
        detail = info.get_user(username=member_handle)
        ident = detail.data.id
        response = client.get_users(ids=ident, user_fields=["url"])
        for user in response.data:
            urls = user.url
            return print(urls)

    def date_made(self):
        info = tweepy.Client(bearer_token=config.BEARER_TOKEN)
        member_handle = self.handle
        detail = info.get_user(username=member_handle)
        ident = detail.data.id
        response = client.get_users(ids=ident, user_fields=["created_at"])
        for user in response.data:
            dates = user.created_at
            return print(dates)


# Create instances of the Member Class
Member_1 = Member('Marie-Louise',
                  'MmeMarieLouise',
                  'Data Scientist @UKCivilService| Global Council member @pyladies | Proud #Mama. Views are my own. '
                  'She / Her',
                  'London,UK',
                  'https://linktr.ee/MmeMarieLouise',
                  'May 2016',
                  client.get_users_followers(id=config.USER_ID),
                  client.get_users_following(id=config.USER_ID))

Member_1.id()
Member_1.social_name()
Member_1.social_handle()
Member_1.biog()
Member_1.loc()
Member_1.link()
Member_1.date_made()


def _id():
    info = tweepy.Client(bearer_token=config.BEARER_TOKEN)
    detail = info.get_user(username='MesrenyameDogbe')
    return print(detail.data.id)


print(f'{Member_1.followers}')
print(f'{Member_1.following}')
print(f'{Member_1.name}')
