package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	PartX(4)
	PartX(14)
}

func PartX(length int) {
	line := ReadFile()[0]

	for i := length; i < len(line); i++ {
		thisWindow := line[i-length : i]
		isMarker := true
		for _, char := range thisWindow {
			isMarker = isMarker && (strings.Count(thisWindow, string(char)) == 1)
		}
		if isMarker {
			fmt.Println(i)
			return
		}
	}
	fmt.Println("not found")
}

func ReadFile() []string {
	filePath := "day06_input.txt"
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	readFile.Close()

	return fileLines
}

// borrowed from https://stackoverflow.com/a/66751055
func removeDuplicateStr(strSlice []string) []string {
	allKeys := make(map[string]bool)
	list := []string{}
	for _, item := range strSlice {
		if _, value := allKeys[item]; !value {
			allKeys[item] = true
			list = append(list, item)
		}
	}
	return list
}
