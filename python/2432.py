class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        lastTime = 0
        largestTime = 0
        largestTimeId = n
        for (id, leaveTime) in logs:
            timeTaken = leaveTime - lastTime
            lastTime = leaveTime
            if timeTaken > largestTime:
                largestTime = timeTaken
                largestTimeId = id
            elif timeTaken == largestTime:
                largestTimeId = min(id, largestTimeId)
        return largestTimeId
        
