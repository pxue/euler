// Largest product in a grid of len 4 O(n^2)

package golang

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

const A = `
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48`

var G [][]float64

func getLocalMax(g *[][]float64, x int, y int) (max float64) {

	orig := (*g)[x][y]
	chnn := make(chan float64, 1)

	// up - down
	go func(chnn chan float64) {
		localMax := orig
		for mod := -3; mod < 4; mod++ {
			if (y+mod) < 0 || (y+mod) >= len(*g) {
				continue
			}
			if mod == 0 {
				chnn <- localMax
				localMax = orig
				continue
			}
			localMax = localMax * (*g)[x][y+mod]
		}
		chnn <- localMax
	}(chnn)

	// left - right
	go func(chnn chan float64) {
		localMax := orig
		for i := -3; i < 4; i++ {
			if (x+i) < 0 || (x+i) >= len((*g)[x]) {
				continue
			}
			if i == 0 {
				chnn <- localMax
				localMax = orig
				continue
			}
			localMax = localMax * (*g)[x+i][y]
		}
		chnn <- localMax
	}(chnn)

	// \  (-3,-3), (-2,-2), (-1,-1)
	// \  (1, 1), (2, 2), (3, 3)
	go func(chnn chan float64) {
		localMax := orig
		tempi := -3
		for j := -3; j < 4; j++ {
			if (x+tempi) < 0 || (y+j) < 0 || (x+tempi) >= len((*g)[x]) || (y+j) >= len(*g) {
				localMax = orig
				tempi++
				continue
			}
			if tempi == 0 && j == 0 {
				chnn <- localMax
				localMax = orig
				tempi++
				continue
			}
			localMax = localMax * (*g)[x+tempi][y+j]
			tempi++
		}
		chnn <- localMax
	}(chnn)

	// /  (3, -3), (2, -2), (1,-1)
	// /  (-1, 1), (-2, 2), (-3, 3)
	go func(chnn chan float64) {
		localMax := orig
		tempy := 3
		for i := -3; i < 4; i++ {
			if (x+i) < 0 || (y+tempy) < 0 || (x+i) >= len((*g)[x]) || (y+tempy) >= len(*g) {
				localMax = orig
				tempy--
				continue
			}
			if tempy == 0 && i == 0 {
				chnn <- localMax
				localMax = orig
				tempy--
				continue
			}
			localMax = localMax * (*g)[x+i][y+tempy]
			tempy--
		}
		chnn <- localMax
	}(chnn)

	var count int
	for {
		select {
		case m := <-chnn:
			max = math.Max(max, m)
			count++
		}

		if count == 8 {
			close(chnn)
			return
		}
	}

	return
}

func parse() {
	s := strings.Split(strings.TrimLeft(A, "\n"), "\n")
	G = make([][]float64, len(s))

	for i, raw_line := range s {
		line := strings.Split(raw_line, " ")

		for _, chr := range line {
			conv, err := strconv.Atoi(chr)
			if err != nil {
				fmt.Println(err)
				continue
			}
			G[i] = append(G[i], float64(conv))
		}
	}
}

func problem11_b() {
	var max int
	var localMax float64 = 1.0
	for i, line := range G {
		for j, _ := range line {
			localMax = getLocalMax(&G, i, j)
			max = int(math.Max(float64(max), float64(localMax)))
			localMax = 1
		}
	}
	fmt.Println(max)
}

func problem11() {
	var max, localmax float64

	// Kadane's Algorithm
	// break problem down into smaller subproblems

	// global row wise maximu
	for _, line := range G { // n
		for start := 0; start < len(line); start++ { // n
			for j := start; j < start+4; j++ { // just 4
				if j > len(line)-1 {
					continue
				}
				localmax = math.Max(1.0, localmax*line[j])
				max = math.Max(localmax, max)
			}
			localmax = 1.0
		}
	}
	localmax = 1.0

	// global column wise maximum
	for c := 0; c < len(G[0]); c++ {
		for start := 0; start < len(G); start++ {
			for j := start; j < start+4; j++ {
				if j > len(G)-1 {
					continue
				}
				localmax = math.Max(1.0, localmax*G[c][j])
				max = math.Max(localmax, max)
			}
			localmax = 1.0
		}
	}
	localmax = 1.0
	fmt.Println(int(max))


    // diagnals etc

}
