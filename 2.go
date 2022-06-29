package main

import "fmt"

func main(){
	var fib0, fib1, fib_t, sum int
	fib0 = 1
	fib1 = 2
	for fib1 < 4000000 {
		fib_t = fib0 + fib1
		if fib1 % 2 == 0{
			sum += fib1
		}
		fib0 = fib1
		fib1 = fib_t
	}
	fmt.Println(sum)
}