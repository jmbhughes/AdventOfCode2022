package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	Part1()
	Part2()
}

func Part1() {
	fileLines := ReadFile()
	totals := TotalGroups(fileLines)
	answer := SumTopK(totals, 1)
	fmt.Println(answer)
}

func Part2() {
	fileLines := ReadFile()
	totals := TotalGroups(fileLines)
	answer := SumTopK(totals, 3)
	fmt.Println(answer)
}

func ReadFile() []string {
	filePath := "day01_input.txt"
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

func TotalGroups(fileLines []string) []int {
	// Convert the raw string buffer into the calorie total for each elf
	// i.e. delimit by spaces and sum
	var output []int

	currentTotal := 0
	for _, line := range fileLines {
		if line != "" {
			value, _ := strconv.Atoi(line)
			currentTotal += value
		} else {
			output = append(output, currentTotal)
			currentTotal = 0
		}
	}
	return output
}

func SumTopK(totals []int, k int) int {
	// This assumes all values are >= 0, which is the case here.
	answer := 0
	for i := 0; i < k; i++ {
		currentMax := 0
		currentMaxIndex := -1
		for valueIndex, value := range totals {
			if value > currentMax {
				currentMax = value
				currentMaxIndex = valueIndex
			}
		}
		answer += currentMax
		totals[currentMaxIndex] = 0
	}
	return answer
}
