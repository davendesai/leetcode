import (
	"math"
)

func findKDistantIndices(nums []int, key int, k int) []int {
    idxs := []int{}
	for idx, elem := range nums {
		if elem == key {
			idxs = append(idxs, idx)
		}
	}

	ret := []int{}
	for i, _ := range nums {
		for _, j := range idxs {
			if int(math.Abs(float64(i) - float64(j))) <= k {
				ret = append(ret, i)
                break
			}
		}
	}
	return ret
}