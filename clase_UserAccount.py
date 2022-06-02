from clase_Timeline import Timeline
from clase_Tweet import Tweet

class UserAccount(Tweet, Timeline):
    def __init__(self, alias=str,email=str, timeline=Timeline):

        self.alias = alias    #Tanto el alias como el email y los tweets son del tipo str ya que son cadenas de caracteres
        self.email = email
        self.tweets = []         #Tweets será una lista donde se almacenen todos los tweets(str) del user
        self.followers = []       #Followers será una lista que contenga los alias(str) que sigan esa cuenta
        self.timeline = timeline    #timeline es un elemento de la clase Timeline

    def follow(self,user2):
        user2.followers.append(self.alias)

    def tweet(self,tweet1=Tweet):
        self.tweets.append(tweet1)
        for follower in self.followers:
            follower.añadir_tweet(tweet1)

    def get_alias(self):
        return self.alias
    def get_email(self):
        return self.email
    def get_timeline(self):
        return self.timeline