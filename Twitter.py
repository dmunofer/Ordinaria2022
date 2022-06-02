import datetime

class Tweet():
    def __init__(self, tweet=str):
        if len(tweet)>140:
            raise Exception("Máximo 140 caracteres")
        else:
            self.tweet=tweet

class Timeline():
    def __init__(self):
        self.timeline=[]

    def añadir_tweet(self, tweet):
        self.timeline.append(tweet)

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

class DirectMessage(Tweet, UserAccount):
    def __init__(self,message=Tweet, sender=UserAccount, receiver=UserAccount):
        self.message=message
        self.sender=sender
        self.receiver=receiver
        self.time=datetime




    


