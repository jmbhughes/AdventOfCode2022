import numpy as np


def parse_input(path="day08_input.txt"):
    return np.genfromtxt(path, delimiter=1, dtype=int)


def part1():
    matrix = parse_input()

    visible_top = np.zeros_like(matrix, dtype=bool)
    visible_top[0, :] = True
    for i in range(1, visible_top.shape[0]):
        visible_top[i, :] = matrix[i, :] > np.max(matrix[:i, :], axis=0)

    visible_bottom = np.zeros_like(matrix, dtype=bool)
    visible_bottom[-1, :] = True
    for i in range(visible_bottom.shape[0] - 2, -1, -1):
        visible_bottom[i, :] = matrix[i, :] > np.max(matrix[i + 1:, :], axis=0)

    visible_left = np.zeros_like(matrix, dtype=bool)
    visible_left[:, 0] = True
    for i in range(1, visible_top.shape[1]):
        visible_left[:, i] = matrix[:, i] > np.max(matrix[:, :i], axis=1)

    visible_right = np.zeros_like(matrix, dtype=bool)
    visible_right[:, -1] = True
    for i in range(visible_bottom.shape[1] - 2, -1, -1):
        visible_right[:, i] = matrix[:, i] > np.max(matrix[:, i + 1:], axis=1)

    visible_any = np.sum([visible_top, visible_bottom, visible_left, visible_right], axis=0) >= 1

    print(np.sum(visible_any))


def part2():
    matrix = parse_input()

    best_score = 0

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            this_score = 1

            directional_vision = 0
            for d in range(i + 1, matrix.shape[0]):
                if matrix[d, j] < matrix[i, j]:
                    directional_vision += 1
                else:
                    directional_vision += 1
                    break
            this_score *= directional_vision

            directional_vision = 0
            for d in range(i - 1, -1, -1):
                if matrix[d, j] < matrix[i, j]:
                    directional_vision += 1
                else:
                    directional_vision += 1
                    break
            this_score *= directional_vision

            directional_vision = 0
            for d in range(j + 1, matrix.shape[1]):
                if matrix[i, d] < matrix[i, j]:
                    directional_vision += 1
                else:
                    directional_vision += 1
                    break
            this_score *= directional_vision

            directional_vision = 0
            for d in range(j - 1, -1, -1):
                if matrix[i, d] < matrix[i, j]:
                    directional_vision += 1
                else:
                    directional_vision += 1
                    break
            this_score *= directional_vision

            best_score = max(this_score, best_score)

    print(best_score)


if __name__ == "__main__":
    part1()
    part2()
