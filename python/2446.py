class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        events = sorted([event1, event2])
        return events[1][0] <= events[0][1]
