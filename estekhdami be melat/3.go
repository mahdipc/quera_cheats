package main

import (
   "fmt"
   "strings"
)

func main() {
   var n, q int
   fmt.Scan(&n, &q)
   
   var s string
   fmt.Scan(&s)
   
   for i := 0; i < q; i++ {
       var queryType string
       fmt.Scan(&queryType)
       
       if queryType == "?" {
           var t string
           fmt.Scan(&t)
           if strings.Contains(s, t) {
               fmt.Println("YES")
           } else {
               fmt.Println("NO") 
           }
       } else {
           var k int
           fmt.Scan(&k)
           k--
           chars := []rune(s)
           if chars[k] == '0' {
               chars[k] = '1'
           } else {
               chars[k] = '0'
           }
           s = string(chars)
       }
   }
}