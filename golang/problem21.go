/*
* Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# Solution:
# There's a clever way of solving this:
# http://math.stackexchange.com/questions/22721/is-there-a-formula-to-calculate-the-sum-of-all-proper-divisors-of-a-number
#
# We just need need to find the prime factors and follow
# the fomula.

# the Pow and Sqrt functions are taken from https://code.google.com/p/intmath
# under New BSD Liscense (http://opensource.org/licenses/BSD-3-Clause)

*/
package golang

import (
	"fmt"
	"math"
)

func Pow(x, y int) (r int) {
	if x == r || y < r {
		return
	}
	r = 1
	if x == r {
		return
	}
	if x < 0 {
		x = -x
		if y&1 == 1 {
			r = -1
		}
	}
	for y > 0 {
		if y&1 == 1 {
			r *= x
		}
		x *= x
		y >>= 1
	}
	return
}

func Sqrt(x int) (r int) {
	if x < 0 {
		return -1
	}

	//Fast way to make p highest power of 4 <= x
	var n uint
	p := x
	if int64(p) >= 1<<32 {
		p >>= 32
		n = 32
	}
	if p >= 1<<16 {
		p >>= 16
		n += 16
	}
	if p >= 1<<8 {
		p >>= 8
		n += 8
	}
	if p >= 1<<4 {
		p >>= 4
		n += 4
	}
	if p >= 1<<2 {
		n += 2
	}
	p = 1 << n
	var b int
	for ; p != 0; p >>= 2 {
		b = r | p
		r >>= 1
		if x >= b {
			x -= b
			r |= p
		}
	}
	return
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func isPrime(n int) bool {

	if n <= 3 {
		return n >= 2
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	for i := 5; i < Sqrt(n)+1; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}

	return true
}

func factorPrime(input int, fp *map[float64]float64) {

	G := func(n int) int {
		return ((n * n) + 1) % input
	}

	gcd := func(a int, b int) int {
		for b > 0 {
			a, b = b, a%b
		}
		return a
	}

	var d = 1
	var x, y = 2, 2
	for d == 1 {
		x = G(x)
		y = G(G(y))

		d = gcd(Abs(x-y), input)
		if d != 1 {
			(*fp)[float64(d)]++
			(*fp)[float64(input/d)]++
		}
	}
}

func factor(input int) map[float64]float64 {

	var pf = make(map[float64]float64)

	// check if sqrt-able
	if sqrt := math.Sqrt(float64(input)); sqrt == float64(int(sqrt)) {
		pf[sqrt] += 1
		input = int(sqrt)
	}

	for _, prime := range []int{2, 3, 5, 7, 11, 13, 17, 19} {
		for input%prime == 0 {
			input = input / prime
			pf[float64(prime)]++
		}
		if input == 1 {
			return pf
		}
	}

	if isPrime(input) {
		pf[float64(input)]++
	} else {
		factorPrime(input, &pf)
	}

	return pf
}

func problem21() {

	factored := make(map[int]float64)
	for a := 1; a < 10000; a++ {
		var sum float64 = 1
		for k, v := range factor(a) {
			var local_sum float64 = 1
			for n := 1.0; n <= v; n++ {
				local_sum += math.Pow(k, n)
			}
			sum *= local_sum
		}

		properSum := sum - float64(a)
		if properSum != 1 && properSum < 10000 {
			factored[a] = properSum
		}
	}

	amicableSum := 0
	for k, v := range factored {
		if proper, ok := factored[int(v)]; ok && k != int(v) && int(proper) == k {
            fmt.Println(k, v)
			amicableSum += k
		}
	}
	fmt.Println("Sum of amicable numbers", amicableSum)

}
