class Tweet():
    def __init__(self, tweet=str):
        if len(tweet)>140:
            raise Exception("Máximo 140 caracteres")
        else:
            self.tweet=tweet

    def get_tweet(self):
        return self.tweet

    def set_tweet(self, tweetx):
        self.tweet=tweetx