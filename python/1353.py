class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # sort events by start, then end date
        events.sort()

        backlog = []
        attended = []

        idx = 0
        end = max(e[1] for e in events)

        for day in range(1, end+1):
            
            # all events that start before/on today
            while idx < len(events) and events[idx][0] <= day:
                heapq.heappush(backlog, (events[idx][1], events[idx]))
                idx += 1

            # remove all events that end before today
            while backlog and backlog[0][0] < day:
                heapq.heappop(backlog)
            
            # attend meeting that ends earliest in case
            # there are multiple possible
            # i.e. to save some meetings to attend later if possible
            if backlog:
                attended.append(heapq.heappop(backlog)[1])                

        print(attended)
        return len(attended)
    
