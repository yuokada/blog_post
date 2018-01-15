package main

import (
	"encoding/json"
	"fmt"
)

const v2 = `
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

func main() {
	// var m map[interface{}]interface{}
	var m interface{}
	err := json.Unmarshal([]byte(v2), &m)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(m)
	// .(map[string]interface{})
	// for k, _ := range m {
	// 	fmt.Println(k)
	// }
	for k, v := range m.([]interface{}) {
		fmt.Println(k, v)
	}
}
