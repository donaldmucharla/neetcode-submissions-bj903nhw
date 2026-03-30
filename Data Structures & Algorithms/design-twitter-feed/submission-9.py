class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        heapq.heapify(minheap)
        self.followmap[userId].add(userId)
        for followeeID in self.followmap[userId]:
            if followeeID in self.tweetmap:
                index = len(self.tweetmap[followeeID])-1
                count, tweetId = self.tweetmap[followeeID][index]
                heapq.heappush(minheap, [count, tweetId, followeeID, index-1])
        while minheap and len(res)<10:
            count, tweetId, followeeID, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetmap[followeeID][index]
                heapq.heappush(minheap, [count, tweetId, followeeID, index-1])
        return res



        

    def follow(self, followerId: int, followeeId: int) -> None:
         self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        
