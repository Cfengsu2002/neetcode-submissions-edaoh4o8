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
            if self.user_tweets[followee]:
                index = len(self.user_tweets[followee]) - 1
                timestamp, tweet = self.user_tweets[followee][index]
                tweets.append((timestamp, tweet, index, followee))
        heapq.heapify(tweets)
        for i in range(10):
            if (not tweets):
                return ans
            timestamp, tweet, index, followee = heapq.heappop(tweets)
            ans.append(tweet)
            if index>0:
                heapq.heappush(tweets, ( self.user_tweets[followee][index-1][0], self.user_tweets[followee][index-1][1],index-1, followee))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].discard(followeeId)

#