import (
	"math"
)

func maxDistance(s string, k int) int {
	curMax := 0
	north, south, west, east := 0, 0, 0, 0

	for _, dir := range s {
		switch dir {
		case 'N':
			north++
		case 'S':
			south++
		case 'W':
			west++
		case 'E':
			east++
		}

		// both axis equiv affect manhattan dist
		dVert := min(north, south)
		dHoriz := min(west, east)

		numChanges := min(k, dVert)
		if numChanges < k {
			numChanges += min(k - numChanges, dHoriz)
		}

		// a change adds 2 to manhattan dist i.e. from a -1 to a +1
		manhattanDist := math.Abs(float64(north - south)) + math.Abs(float64(west - east))
		curMax = max(curMax, int(manhattanDist) + (2 * numChanges))
	}

	return curMax
}