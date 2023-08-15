class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        def daysTill(date):
            daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            month, day = date.split("-")
            return sum(daysInMonth[:int(month)-1]) + int(day)

        latestArrival = max(daysTill(arriveAlice), daysTill(arriveBob))
        earliestLeave = min(daysTill(leaveAlice), daysTill(leaveBob))

        return max(0, earliestLeave-latestArrival+1)


