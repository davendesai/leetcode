class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        recolors = float('inf')
        i, j = 0, k

        while j <= len(blocks):
            block = Counter(blocks[i:j])
            recolors = min(recolors, block['W'])
            i += 1
            j += 1
        
        return recolors

