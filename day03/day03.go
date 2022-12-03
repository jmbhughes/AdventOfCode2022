package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	Part1()
	Part2()
}

func Part1() {
	answer := 0

	priorities := BuildPriorities()
	lines := ReadFile()
	for _, line := range lines {
		answer += ProcessLine(line, priorities)
	}
	fmt.Println(answer)
}

func Part2() {
	answer := 0

	priorities := BuildPriorities()

	lines := ReadFile()

	for i := 0; i < len(lines); i += 3 {
		answer += ProcessGroup(lines[i], lines[i+1], lines[i+2], priorities)
	}

	fmt.Println(answer)
}

func ReadFile() []string {
	filePath := "day03_input.txt"
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

func SetIntersection(s1 map[string]bool, s2 map[string]bool) map[string]bool {
	intersection := map[string]bool{}
	if len(s1) > len(s2) {
		s1, s2 = s2, s1 // better to iterate over a shorter set
	}
	for k, _ := range s1 {
		if s2[k] {
			intersection[k] = true
		}
	}
	return intersection
}

func BuildPriorities() map[string]int {
	priorities := make(map[string]int)
	for i, s := range "abcdefghijklmnopqrstuvwxyz" {
		priorities[string(s)] = i + 1
	}
	for i, s := range "ABCDEFGHIJKLMNOPQRSTUVWXYZ" {
		priorities[string(s)] = i + 27
	}
	return priorities
}

func ProcessLine(line string, priorities map[string]int) int {
	// make sets out of the first half and second half of the line
	first := make(map[string]bool)
	second := make(map[string]bool)
	for _, c := range line[:len(line)/2] {
		first[string(c)] = true
	}
	for _, c := range line[len(line)/2:] {
		second[string(c)] = true
	}

	// find the intersection; its priority value is the answer
	value := 0
	intersection := SetIntersection(first, second)
	for k, _ := range intersection {
		value = priorities[k]
	}
	return value
}

func ProcessGroup(firstLine string, secondLine string, thirdLine string, priorities map[string]int) int {
	// make sets out of each line
	first := make(map[string]bool)
	second := make(map[string]bool)
	third := make(map[string]bool)
	for _, c := range firstLine {
		first[string(c)] = true
	}
	for _, c := range secondLine {
		second[string(c)] = true
	}
	for _, c := range thirdLine {
		third[string(c)] = true
	}

	// find their intersection, its priority value is the answer
	intersection := SetIntersection(SetIntersection(first, second), third)

	value := 0
	for k, _ := range intersection {
		value = priorities[k]
	}
	return value
}
