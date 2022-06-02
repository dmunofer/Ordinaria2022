from clase_Tweet import Tweet
from clase_UserAccount import UserAccount
from clase_Timeline import Timeline
from datetime import *


class DirectMessage(Tweet, UserAccount):
    def __init__(self,message=Tweet, sender=UserAccount, receiver=UserAccount):
        Tweet.get_tweet=message
        UserAccount.get_alias=sender
        UserAccount.get_alias=receiver
        self.time=datetime

    def __str__(self):
        print(self.message)

    def get_message(self):
        return self.message
    def get_sender(self):
        return self.sender
    def get_receiver(self):
        return self.receiver

    def set_message(self, string):
        self.message=string
    def set_sender(self, user):
        self.sender=user
    def set_receiver(self, user2):
        self.receiver=user2

