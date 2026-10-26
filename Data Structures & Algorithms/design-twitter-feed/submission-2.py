class Twitter:

    def __init__(self):
        self.count = 0
        self.followmap = defaultdict(set)
        self.feedmap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.feedmap[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        heap = []

        self.followmap[userId].add(userId)
        for idx in self.followmap[userId]:
            if idx in self.feedmap:
                index = len(self.feedmap[idx]) - 1
                count, tweetid = self.feedmap[idx][index]
                heapq.heappush(heap,[count,tweetid,idx,index-1])
            
        while heap and len(ans) < 10:

            count,tweetid,idx,index = heapq.heappop(heap)
            ans.append(tweetid)
            if index >= 0:
                count, tweetid = self.feedmap[idx][index]

                heapq.heappush(heap,[count,tweetid,idx,index-1])
        
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
