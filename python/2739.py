class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        dist = 0
        while mainTank > 0:
            mainTank -= 1
            dist += 10

            if dist % 50 == 0:
                if additionalTank:
                    additionalTank -= 1
                    mainTank += 1
        return dist

