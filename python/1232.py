class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return true

        # no duplicates
        p1, p2 = coordinates[0], coordinates[1]
        
        dy, dx = p2[1] - p1[1], p2[0] - p1[0]
        slope = float('inf') if dx == 0 else dy / dx

        for p3 in coordinates[2:]:
            new_dy, new_dx = p3[1] - p1[1], p3[0] - p1[0]
            new_slope = float('inf') if new_dx == 0 else new_dy / new_dx
            if new_slope != slope:
                return False

        return True
