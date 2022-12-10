movements = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}


class Rope:
    def __init__(self, num_components=2):
        self.knots = [(0, 0) for _ in range(num_components)]
        self.tail_visited = {(0, 0)}

    def move(self, direction):
        self.knots[0] = (self.knots[0][0]+movements[direction][0], self.knots[0][1]+movements[direction][1])
        for i in range(1, len(self.knots)):
            delta = (self.knots[i-1][0] - self.knots[i][0], self.knots[i-1][1] - self.knots[i][1])
            self.knots[i] = (self.knots[i][0]+Rope.adjust(delta)[0], self.knots[i][1]+Rope.adjust(delta)[1])
        self.tail_visited.add(self.knots[-1])

    @staticmethod
    def adjust(delta):
        """inspired by https://github.com/Zaitox/AoC2022/blob/main/9/9.py"""
        if delta[0] in [-1, 0, 1] and delta[1] in [-1, 0, 1]:
            return (0, 0)
        if delta[0] > 1 and delta[1] == 0:
            return (1, 0)
        if delta[0] < -1 and delta[1] == 0:
            return (-1, 0)
        if delta[1] > 1 and delta[0] == 0:
            return (0, 1)
        if delta[1] < -1 and delta[0] == 0:
            return (0, -1)
        if delta[0] > 0 and delta[1] > 0:
            return (1, 1)
        if delta[0] < 0 and delta[1] > 0:
            return (-1, 1)
        if delta[0] > 0 and delta[1] < 0:
            return (1, -1)
        if delta[0] < 0 and delta[1] < 0:
            return (-1, -1)


def parse_input(path="day09_input.txt"):
    with open(path, "r") as f:
        lines = f.read().splitlines()
    output = [line.split() for line in lines]
    output = [(t[0], int(t[1])) for t in output]
    return output


def partx(length):
    instructions = parse_input()

    rope = Rope(length)
    for direction, amount in instructions:
        for _ in range(amount):
            rope.move(direction)

    print(len(rope.tail_visited))


if __name__ == "__main__":
    partx(2)
    partx(10)
