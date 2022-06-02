from clase_Tweet import Tweet
from clase_UserAccount import UserAccount
import datetime


class Retweet(Tweet, UserAccount):

    def __init__(self, sender, message):

        Tweet.get_tweet=message
        UserAccount.get_alias=sender
        self.time= datetime

    def __str__(self):
        print(self.message)
