class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1

        steps = 0
        while True:
            forwards = words[(startIndex + steps) % len(words)]
            backwards = words[(startIndex - steps + len(words)) % len(words)]

            if forwards == target or backwards == target:
                return steps
            steps += 1

