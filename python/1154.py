class Solution:
    def dayOfYear(self, date: str) -> int:
        fields = date.split('-')
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def isLeap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        if isLeap(int(fields[0])): daysInMonth[1] = 29
        return sum(daysInMonth[:int(fields[1]) - 1]) + int(fields[2])

