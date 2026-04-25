class Twitter:

    def __init__(self):
        self.user_following=defaultdict(set)
        self.twitters=[]

    def postTweet(self, userId: int, tweetId: int) -> None:
        # the stack is user_twitter[userId]
        # normal stack is enough to track
        self.twitters.append((tweetId, userId))
        print(self.twitters)
    def getNewsFeed(self, userId: int) -> List[int]:
        total_users_needed=[userId]
        for following in self.user_following[userId]:
            total_users_needed.append(following)
        temp_twitters=self.twitters.copy()
        ans_list=[]
        
        while(temp_twitters):
            cur_twitter, cur_user=temp_twitters.pop()
            if(cur_user in total_users_needed):
                ans_list.append(cur_twitter)
            if(len(ans_list)>9):
                break
        return ans_list


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        return 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followeeId in self.user_following[followerId]):
            self.user_following[followerId].remove(followeeId)
        return
