class SimpleComputer:

    def __init__(self):
        self.register = 1
        self.cycle_history = []
        self.screen = [['.']*40 for _ in range(6)]

    def noop(self):
        self.cycle_history.append(self.register)
        self.draw()

    def addx(self, x):
        self.cycle_history.append(self.register)
        self.draw()
        self.register += x
        self.cycle_history.append(self.register)
        self.draw()

    def score(self, cycles=(20, 60, 100, 140, 180, 220)):
        return sum([self[cycle] * cycle for cycle in cycles])

    def draw(self):
        screen_position = (self.current_cycle // 40, self.current_cycle % 40)
        if self.register - 1 <= screen_position[1] <= self.register + 1:
            self.screen[screen_position[0]][screen_position[1]] = '#'

    def __getitem__(self, index):
        if index <= len(self.cycle_history):
            return self.cycle_history[index-2]
        else:
            raise RuntimeError(f"The computer has not yet run for {index} cycles.")

    @property
    def current_cycle(self):
        return len(self.cycle_history)

    def execute(self, lines):
        for line in lines:
            if line == "noop":
                self.noop()
            else:
                _, x = line.split()
                self.addx(int(x))

    def show_screen(self):
        print("\n".join(["".join(row) for row in self.screen]))


def parse_input(path="day10_input.txt"):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def part1():
    lines = parse_input()
    computer = SimpleComputer()
    computer.execute(lines)
    print(computer.score())


def part2():
    lines = parse_input()
    computer = SimpleComputer()
    computer.execute(lines)
    computer.show_screen()


if __name__ == "__main__":
    part1()
    part2()
