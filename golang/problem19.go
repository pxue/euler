/*
*
* Problem19: Counting sundays
*  Count all the sundays that's 1st of the month
*  between 1 Jan 1901 - 31 Dec 2000
 */
package golang

import (
	"fmt"
	"time"
)

func problem19() {
	start := time.Date(1901, time.January, 6, 0, 0, 0, 0, time.UTC)
	end := time.Date(2000, time.December, 31, 0, 0, 0, 0, time.UTC)

	counter := 0
	for {
		if start.Day() == 1 {
			counter++
		}

		start = start.AddDate(0, 0, 7)
		if start.After(end) {
			break
		}
	}

	fmt.Println(counter)
}
