class Timeline():
    def __init__(self):
        self.timeline=[]

    def añadir_tweet(self, tweet):
        self.timeline.append(tweet)

    def get_timeline(self):
        return self.timeline
