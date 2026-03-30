from collections import Counter
import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count_map = Counter(hand)
        minH = list(count_map.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count_map:
                    return False

                count_map[i] -= 1

                if count_map[i] == 0:
                    # must remove in correct order
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
                    del count_map[i]

        return True
