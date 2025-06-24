import (
	"fmt"
	"strings"
    "strconv"
)

func kMirror(k int, n int) int64 {
	cnt, total := 0, 0
	palindromeLength := 1
	for {
		for _, p := range genPalindromes(palindromeLength) {
			baseK, _ := convertBase(p, k)
			if isPalindrome(baseK) {
				cnt += 1
				total += p

				if cnt == n {
					return int64(total)
				}
			}
		}
		palindromeLength += 1
	}
}

func genPalindromes(len int) []int {
	if len == 1 {
		return []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	}

	digits := len / 2
	min, _ := strconv.Atoi("1" + strings.Repeat("0", digits - 1))
	max, _ := strconv.Atoi(strings.Repeat("9", digits))

	ret := []int{}
	if len % 2 == 0 {
		// even means doubling
		for i := min; i <= max; i++ {
			rev := reverseString(strconv.Itoa(i))
			fin, _ := strconv.Atoi(strconv.Itoa(i) + rev)
			ret = append(ret, fin)
		}
	} else {
		// odd means adding digit in the middle
		for i := min; i <= max; i++ {
			for j := 0; j <= 9; j++ {
				rev := reverseString(strconv.Itoa(i))
				fin, _ := strconv.Atoi(strconv.Itoa(i) + strconv.Itoa(j) + rev)
				ret = append(ret, fin)
			}
		}
	}
	return ret
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes) - 1; i < j; i, j = i + 1, j - 1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func convertBase(n, b int) (int, error) {
	var conv string
	for n != 0 {
		conv = strconv.Itoa(n % b) + conv
		n = n / b
	}
	return strconv.Atoi(conv)
}

func isPalindrome(n int) bool {
	runes := []rune(strconv.Itoa(n))
	for i, j := 0, len(runes) - 1; i < j; i, j = i + 1, j - 1 {
		if runes[i] != runes[j] {
			return false
		}
	}
	return true
}