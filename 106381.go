package main

import (
	"fmt"
)

func main() {
	var st string
	fmt.Scan(&st)
	for pos := range st {
		fmt.Printf("character %c starts at byte position %d\n", st[pos:pos+4], pos)
	}

	fmt.Println(st)

}
