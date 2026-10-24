class Twitter:

    def __init__(self):
        # data structures
        self.user_followers=defaultdict(set)
        self.user_tweets=defaultdict(list)
        self.timestamp=0 #[]
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.user_followers[userId].add(userId)
        self.timestamp-=1
        # [1: (0, 10), 2:(1, 20)]

    def getNewsFeed(self, userId: int) -> List[int]:
        followees=[]
        for followee in self.user_followers[userId]:
            followees.append(followee)
        tweets=[]
        ans=[]
        for followee in followees:
            for timestamp, tweet in self.user_tweets[followee]:
                tweets.append((timestamp, tweet))
        heapq.heapify(tweets)
        for i in range(10):
            if (not tweets):
                return ans
            timestamp, tweet = heapq.heappop(tweets)
            ans.append(tweet)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].discard(followeeId)

#