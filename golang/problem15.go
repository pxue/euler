// GRAPH Traversal. Find all lattice path from top left corner of
// a 20x20 grid to bottom right corner by moving ONLY RIGHT and DOWN

package golang

import "fmt"

func problem15() {

	// this is a pascal's triangle question
	// or a combinatory question: ie 40 C 20

	// here's the pascal's triagle solution
	//
	// we have 20x20 grid = (20+1) * 2 vertices = 40th row of pascal's triangle

	pascal := []int{1}
	for i := 0; i < 40; i++ {
		pascal = append(pascal, (pascal[i] * (40 - i) / (i + 1)))
	}

	fmt.Println(pascal[len(pascal)/2])

}
