package main

import (
	"encoding/json"
	"fmt"
)

const v = `
[
  {
    "a": 10,
    "b": 20
  },
  {
    "a": 15,
    "b": 20
  }
]
`
const v2 = `
  {
    "a": 10,
    "b": 20
  }
`

func main() {
	fmt.Printf("Hello, world\n")
	fmt.Println(v)
	var m map[string]interface{}
	json.Unmarshal([]byte(v2), &m)

	fmt.Println(m)
	for k := range m {
		fmt.Println(k)
	}
}
