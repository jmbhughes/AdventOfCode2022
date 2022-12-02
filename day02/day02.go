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
	fileContents := ReadFile()

	totalScore := 0
	for _, line := range fileContents {
		elfChoiceString := line[0]
		myChoiceString := line[2]

		elfChoice := 0
		switch elfChoiceString {
		case 'A':
			elfChoice = Rock
		case 'B':
			elfChoice = Paper
		case 'C':
			elfChoice = Scissors
		}

		myChoice := 0
		switch myChoiceString {
		case 'X':
			myChoice = Rock
		case 'Y':
			myChoice = Paper
		case 'Z':
			myChoice = Scissors
		}

		totalScore += ScoreRound(elfChoice, myChoice)
	}
	fmt.Println(totalScore)
}

func Part2() {
	fileContents := ReadFile()

	totalScore := 0
	for _, line := range fileContents {
		elfChoiceString := line[0]
		outcomeString := line[2]

		elfChoice := 0
		switch elfChoiceString {
		case 'A':
			elfChoice = Rock
		case 'B':
			elfChoice = Paper
		case 'C':
			elfChoice = Scissors
		}

		outcome := 0
		switch outcomeString {
		case 'X':
			outcome = Loss
		case 'Y':
			outcome = Draw
		case 'Z':
			outcome = Win
		}

		myChoice := DetermineMyPlay(elfChoice, outcome)
		totalScore += ScoreRound(elfChoice, myChoice)
	}
	fmt.Println(totalScore)
}

func ReadFile() []string {
	filePath := "day02_input.txt"
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

const (
	Rock     int = 1
	Paper        = 2
	Scissors     = 3
)

const (
	Win  int = 6
	Draw     = 3
	Loss     = 0
)

func CalculateOutcome(otherChoice int, myChoice int) int {
	switch otherChoice {
	case Rock:
		switch myChoice {
		case Rock:
			return Draw
		case Paper:
			return Win
		case Scissors:
			return Loss
		}
	case Paper:
		switch myChoice {
		case Rock:
			return Loss
		case Paper:
			return Draw
		case Scissors:
			return Win
		}
	case Scissors:
		switch myChoice {
		case Rock:
			return Win
		case Paper:
			return Loss
		case Scissors:
			return Draw
		}
	}
	return -1
}

func ScoreRound(elfChoice int, myChoice int) int {
	return myChoice + CalculateOutcome(elfChoice, myChoice)
}

func DetermineMyPlay(elfChoice int, outcome int) int {
	switch elfChoice {
	case Rock:
		switch outcome {
		case Win:
			return Paper
		case Draw:
			return Rock
		case Loss:
			return Scissors
		}
	case Paper:
		switch outcome {
		case Win:
			return Scissors
		case Draw:
			return Paper
		case Loss:
			return Rock
		}
	case Scissors:
		switch outcome {
		case Win:
			return Rock
		case Draw:
			return Scissors
		case Loss:
			return Paper
		}
	}
	return -1
}
