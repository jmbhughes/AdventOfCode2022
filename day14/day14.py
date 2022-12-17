from enum import Enum


class Terrain(Enum):
    ROCK = 1
    AIR = 2
    SAND_SOURCE = 3
    SAND = 4


def parse_input(path="day14_input.txt"):
    """ Creates a dictionary where the keys are the coordinates and the value is what is present there, e.g. Rock"""
    with open(path) as f:
        lines = f.read().splitlines()

    rock_paths = []
    for line in lines:
        coordinate_pairs = line.split("->")
        split_pairs = [tuple(map(int, pair.split(","))) for pair in coordinate_pairs]
        rock_paths.append(split_pairs)

    landscape = {}

    for path in rock_paths:
        for i in range(1, len(path)):
            start, end = path[i-1], path[i]
            for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                    landscape[(x, y)] = Terrain.ROCK

    return landscape, max([k[0] for k in landscape.keys()]), max([k[1] for k in landscape.keys()])


def simulate_sand_fall(landscape, max_fall=1_000):
    positions = [(500, 0)]
    keep_falling = True
    fall_count = 0
    while keep_falling:
        if fall_count > max_fall:
            keep_falling = False

        directly_below = (positions[-1][0], positions[-1][1] + 1)
        diagonal_left_below = (positions[-1][0] - 1, positions[-1][1] + 1)
        diagonal_right_below = (positions[-1][0] + 1, positions[-1][1] + 1)

        if landscape.get(directly_below, Terrain.AIR) == Terrain.AIR:
            positions.append(directly_below)
        elif landscape.get(diagonal_left_below, Terrain.AIR) == Terrain.AIR:
            positions.append(diagonal_left_below)
        elif landscape.get(diagonal_right_below, Terrain.AIR) == Terrain.AIR:
            positions.append(diagonal_right_below)
        else:
            keep_falling = False
        fall_count += 1
    landscape[positions[-1]] = Terrain.SAND
    return landscape, fall_count > max_fall


def visualize(landscape, start_x, end_x, start_y, end_y):
    symbols = {Terrain.ROCK: "#", Terrain.AIR: ".", Terrain.SAND_SOURCE: "+", Terrain.SAND: "o"}
    for y in range(start_y, end_y+1):
        for x in range(start_x, end_x+1):
            print(symbols[landscape.get((x, y), Terrain.AIR)], end="")
        print()


def part1():
    landscape, end_x, end_y = parse_input()
    count = 0
    while True:
        landscape, eternally_fell = simulate_sand_fall(landscape)
        count += 1
        if eternally_fell:
            break
    print(count - 1)


def part2():
    landscape, end_x, end_y = parse_input()

    # add the floor
    for x in range(end_x+1_000):
        landscape[(x, end_y+2)] = Terrain.ROCK

    # let the sand fall!
    count = 0
    while landscape.get((500, 0), Terrain.AIR) != Terrain.SAND:
        landscape, _ = simulate_sand_fall(landscape)
        count += 1

    print(count)


if __name__ == "__main__":
    part1()
    part2()
