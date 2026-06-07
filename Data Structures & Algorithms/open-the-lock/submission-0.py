class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        visited = set(deadends)
        q = collections.deque()
        q.append(["0000", 0])

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i])+1) % 10)
                new_lock = lock[:i]+digit+lock[i+1:]
                res.append(new_lock)
                digit = str((int(lock[i])-1+10)%10)
                new_lock = lock[:i]+ digit+lock[i+1:]
                res.append(new_lock)
            
            return res
        
        while q:
            lock, move = q.popleft()
            if lock == target:
                return move
            
            for child in children(lock):
                if not child in visited:
                    visited.add(child)
                    q.append([child, move+1])
        
        return -1

            
