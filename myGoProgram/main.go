package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	// open output file
	fo, err := os.OpenFile("log.csv", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		panic(err)
	}
	// close fo on exit and check for its returned error
	defer func() {
		if err := fo.Close(); err != nil {
			panic(err)
		}
	}()
	fmt.Printf("The args received are:\n")
	for i := 0; i < len(os.Args); i++ {
		fmt.Printf("The arg %v is %v\n", i, os.Args[i])
	}
	if len(os.Args) > 1 && os.Args[1] == "fail" {

		if _, err := fo.WriteString(fmt.Sprintf("From Go failing: %s\n", time.Now().Format("15:04:05 2006-02-01"))); err != nil {
			panic(err)
		}
		panic("Program received argument to fail.")

	}
	if _, err := fo.WriteString(fmt.Sprintf("From Go succeeding: %s\n", time.Now().Format("15:04:05 2006-02-01"))); err != nil {
		panic(err)

	}

}
