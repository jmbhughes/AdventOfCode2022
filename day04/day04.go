package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	PartX(IsContained)
	PartX(IsOverlapping)
}

func PartX(operation func(int, int, int, int) bool) {
	total := 0
	lines := ReadFile()
	for _, line := range lines {
		if ProcessLine(line, operation) {
			total += 1
		}
	}
	fmt.Println(total)
}

func ReadFile() []string {
	filePath := "day04_input.txt"
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

func ProcessLine(line string, operation func(int, int, int, int) bool) bool {
	// parse the line into integers
	commaSplit := strings.Split(line, ",")
	firstAssignment := strings.Split(commaSplit[0], "-")
	secondAssignment := strings.Split(commaSplit[1], "-")

	firstStart, _ := strconv.Atoi(firstAssignment[0])
	firstEnd, _ := strconv.Atoi(firstAssignment[1])

	secondStart, _ := strconv.Atoi(secondAssignment[0])
	secondEnd, _ := strconv.Atoi(secondAssignment[1])

	// do the check
	return operation(firstStart, firstEnd, secondStart, secondEnd)
}

func IsContained(firstStart int, firstEnd int, secondStart int, secondEnd int) bool {
	return (firstStart <= secondStart && firstEnd >= secondEnd) || (firstStart >= secondStart && firstEnd <= secondEnd)

}

func IsOverlapping(firstStart int, firstEnd int, secondStart int, secondEnd int) bool {
	// We'll check for them not overlapping since that's simpler, and then negate
	minStart, minEnd, maxStart, maxEnd := firstStart, firstEnd, secondStart, secondEnd
	if maxStart < minEnd {
		minStart, minEnd, maxStart, maxEnd = maxStart, maxEnd, minStart, minEnd
	}
	return !(minEnd < maxStart)
}
