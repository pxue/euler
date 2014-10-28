/*
* None Abundant sums

* We can reuse our factoring functions from problem21.

 */
package golang

import (
	"fmt"
	"math"
)

func problem23() {

	var abundant []float64
	for a := 12; a < 28123; a++ {
		var sum float64 = 1
		for k, v := range factor(a) {
			var local_sum float64 = 1
			for n := 1.0; n <= v; n++ {
				local_sum += math.Pow(k, n)
			}
			sum *= local_sum
		}

		properSum := sum - float64(a)
		if properSum > float64(a) { // abundant number
			abundant = append(abundant, float64(a))
		}
	}
	/*fmt.Println(abundant)*/

	result := make([]bool, 28124)
	var localSum float64
	for i := 0; i < len(abundant); i++ {
		for j := i; j < len(abundant); j++ {
			localSum = abundant[i] + abundant[j]
			if localSum <= 28123 {
				result[int(localSum)] = true
			} else {
				break
			}
		}
	}

	var sum int
	for i := 0; i < len(result); i++ {
		if !result[i] {
			sum += i
		}
	}

	fmt.Println(int(sum))

}
