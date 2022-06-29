package main

import (
	"fmt"
	//"math"
)

func power(x uint64, exp uint64) uint64 {
	var result, i uint64
	result = x
	for i=1; i < exp; i++ {
		result *= x
	}
	return result
}

func main(){
	var sum, i uint64
	sum = 0
	for i=1; i < 1001; i++{
		sum += power(i, i)
	}
	fmt.Println(sum)
}