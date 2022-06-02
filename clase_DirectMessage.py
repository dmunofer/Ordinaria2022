from clase_Tweet import Tweet
from clase_UserAccount import UserAccount
from clase_Timeline import Timeline
from datetime import *


class DirectMessage(Tweet, UserAccount):
    def __init__(self,message=Tweet, sender=UserAccount, receiver=UserAccount):
        self.message=message
        self.sender=sender
        self.receiver=receiver
        self.time=datetime

    def get_message(self):
        return self.message
    def get_sender(self):
        return self.sender
    def get_receiver(self):
        return self.receiver