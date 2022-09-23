package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	fmt.Print("W")
	for i := 0; i < n; i++ {
		fmt.Print("o")
	}
	fmt.Print("w!")
}
