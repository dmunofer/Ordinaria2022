from datetime import date

class Timeline():
    def __init__(self,timeline):
        self.timeline=timeline

class UserAccount(Tweet, Email, Timeline):
    def __init__(self, alias=str,email=str, timeline=Timeline):

        self.alias = alias    #Tanto el alias como el email y los tweets son del tipo str ya que son cadenas de caracteres
        self.email = email
        self.tweets = []         #Tweets será una lista donde se almacenen todos los tweets(str) del user
        self.followers = []       #Followers será una lista que contenga los alias(str) que sigan esa cuenta
        self.timeline = timeline    #timeline es un elemento de la clase Timeline

    def follow(self,user2):
        user2.followers.append(self.alias)

    def tweet(self,tweet1):
        self.tweets.append(tweet1)
