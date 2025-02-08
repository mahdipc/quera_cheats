package main

import (
    "bufio"
    "fmt"
    "os"
    "regexp"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    s, _ := reader.ReadString('\n')
    
    p := regexp.MustCompile(`(kalan(\s*)tar)`)
    var resultSt [][2]int
    
    for {
        matches := p.FindAllStringSubmatchIndex(s, -1)
        if len(matches) == 0 {
            break
        }
        
        var t, c int
        var newS string
        lastIdx := 0
        
        for _, match := range matches {
            start := match[0]
            end := match[1]
            spaceStart := match[4]
            spaceEnd := match[5]
            
            newS += s[lastIdx:start]
            
            if spaceEnd-spaceStart == 0 {
                t++
            } else {
                c++
            }
            
            lastIdx = end
        }
        
        newS += s[lastIdx:]
        s = newS
        resultSt = append(resultSt, [2]int{t, c})
    }
    
    fmt.Println(len(resultSt))
    for _, pair := range resultSt {
        fmt.Println(pair[0], pair[1])
    }
}