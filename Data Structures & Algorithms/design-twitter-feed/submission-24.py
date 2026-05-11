class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                c, t = self.tweetMap[followeeId][index]
                maxHeap.append([c, t, followeeId, index-1])
        
        heapq.heapify(maxHeap)
        while maxHeap and len(res)<10:
            c, t, followeeId, index = heapq.heappop(maxHeap)
            res.append(t)
            if index >=0:
                c, t = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [c, t, followeeId, index-1])
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
