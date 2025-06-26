"""
n pizzas
pizzas[i]: weight

if pizza_weights seq/eq then:
    odd: gain heaviest
    even: gain 2nd heaviest

find max weight gain poss
"""
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        print(pizzas)
        weight = 0

        n = len(pizzas)
        for _ in range(n//4 - n//8):
            # heaviest  
            weight += pizzas.pop()

        for _ in range(n//8):
            # 2nd heaviest
            pizzas.pop()
            weight += pizzas.pop()
                
        return weight
