import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # We use a negative count to turn Python's min-heap into a max-heap
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        # KEY FIX: A user follows themselves implicitly for the feed
        # We make a copy of the set or add userId to the iteration
        followees = self.followMap[userId].copy()
        followees.add(userId)
        
        for followee in followees:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                count, tweet = self.tweetMap[followee][index]
                minHeap.append([count, tweet, followee, index - 1])
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweet, followee, index = heapq.heappop(minHeap)
            res.append(tweet)
            if index >= 0:
                count, tweet = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [count, tweet, followee, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Only remove if they are actually following that person
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)