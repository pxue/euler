package golang

import (
	"fmt"
	"strconv"
)

func problem17() {

	ONES := map[int]string{
		49: "ONE",
		50: "TWO",
		51: "THREE",
		52: "FOUR",
		53: "FIVE",
		54: "SIX",
		55: "SEVEN",
		56: "EIGHT",
		57: "NINE",
	}

	TEENS := map[int]string{
		48: "TEN",
		49: "ELEVEN",
		50: "TWELVE",
		51: "THIRTEEN",
		52: "FOURTEEN",
		53: "FIFTEEN",
		54: "SIXTEEN",
		55: "SEVENTEEN",
		56: "EIGHTEEN",
		57: "NINETEEN",
	}

	TENS := map[int]string{
		49: "TEN",
		50: "TWENTY",
		51: "THIRTY",
		52: "FORTY",
		53: "FIFTY",
		54: "SIXTY",
		55: "SEVENTY",
		56: "EIGHTY",
		57: "NINETY",
	}

	var count int

	for i := 1; i <= 1000; i++ {

		word := strconv.Itoa(i)
		if i < 20 {
			if i < 10 {
				count += len(ONES[int(word[0])])
				fmt.Println(i, ONES[int(word[0])], count)
			} else {
				count += len(TEENS[int(word[1])])
				fmt.Println(i, TEENS[int(word[1])], count)
			}
		} else {
			if len(word) == 2 {
				if word[1] == 48 {
					count += len(TENS[int(word[0])])
					fmt.Println(i, TENS[int(word[0])], count)
				} else {
					count += len(TENS[int(word[0])] + ONES[int(word[1])])
					fmt.Println(i, TENS[int(word[0])]+ONES[int(word[1])], count)
				}
			} else if len(word) == 3 {
				h := ONES[int(word[0])] + "HUNDRED"
				var t string
				var o string
				if i%100 != 0 {
					h += "AND"

					if word[1] > 48 {
						if word[1] == 49 {
							t = TEENS[int(word[2])]
						} else {
							t = TENS[int(word[1])]
						}
					}

					if word[1] != 49 {
						o = ONES[int(word[2])]
					}
				}
				fmt.Println(i, h, t, o, len(h+t+o))
				count += len(h + t + o)
			} else {
				fmt.Println(i, "ONE"+"THOUSAND")
                count += len("ONETHOUSAND")
			}
		}
	}

	fmt.Println(count)

}
