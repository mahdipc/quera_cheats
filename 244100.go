package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	s := string(data)

	res := strings.ReplaceAll(s, ".NET", "Golang")

	fmt.Print(res)
}
