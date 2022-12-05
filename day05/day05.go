package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	Part1()
	Part2()
}

type MoveInstruction struct {
	count int
	from  int
	to    int
}

func Part1() {
	stacks, instructions := ParseFile()

	for _, instruction := range instructions {
		fromTop := GetStackTop(stacks[instruction.from-1])
		toTop := GetStackTop(stacks[instruction.to-1])
		for i := 0; i < instruction.count; i++ {
			movingChar := stacks[instruction.from-1][fromTop-i]
			stacks[instruction.to-1][toTop+i+1] = movingChar
			stacks[instruction.from-1][fromTop-i] = ""
		}
	}

	for stackI := 0; stackI < 9; stackI++ {
		fmt.Print(stacks[stackI][GetStackTop(stacks[stackI])])
	}
	fmt.Println()
}

func Part2() {
	stacks, instructions := ParseFile()

	for _, instruction := range instructions {
		fromTop := GetStackTop(stacks[instruction.from-1])
		toTop := GetStackTop(stacks[instruction.to-1])
		for i := 0; i < instruction.count; i++ {
			movingChar := stacks[instruction.from-1][fromTop-i]
			stacks[instruction.to-1][toTop+(instruction.count-i)] = movingChar
			stacks[instruction.from-1][fromTop-i] = ""
		}
	}

	for stack_i := 0; stack_i < 9; stack_i++ {
		fmt.Print(stacks[stack_i][GetStackTop(stacks[stack_i])])
	}
	fmt.Println()
}

func GetStackTop(stack [80]string) int {
	for i := 79; i >= 0; i-- {
		entry := stack[i]
		if entry != "" && entry != " " {
			return i
		}
	}
	return -1
}

func ParseFile() ([9][80]string, []MoveInstruction) {
	lines := ReadFile()
	stackStrings := lines[:10]
	moveStrings := lines[10:]

	stacks := [9][80]string{}
	for column := 0; column < 9; column++ {
		for row := 7; row >= 0; row-- {
			stacks[column][7-row] = string(stackStrings[row][2*(2*(column+1)-1)-1])
		}
	}

	var instructions []MoveInstruction
	for _, moveString := range moveStrings {
		lineContents := strings.Split(moveString, " ")
		count, _ := strconv.Atoi(lineContents[1])
		from, _ := strconv.Atoi(lineContents[3])
		to, _ := strconv.Atoi(lineContents[5])
		instructions = append(instructions, MoveInstruction{count, from, to})
	}

	return stacks, instructions
}

func ReadFile() []string {
	filePath := "day05_input.txt"
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
