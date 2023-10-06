class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky, heavy = False, False

        if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4:
            bulky = True
        if mass >= 100:
            heavy = True

        volume = length * width * height
        if not bulky and volume >= 10 ** 9:
            bulky = True

        if bulky and heavy:
            return "Both"
        elif not bulky and not heavy:
            return "Neither"
        elif bulky:
            return "Bulky"
        else:
            return "Heavy"

