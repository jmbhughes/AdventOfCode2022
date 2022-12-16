from collections import deque
import numpy as np


def bfs_step_count(node_neighbors, source_name, end_name):
    queue = deque()
    queue.append(source_name)
    visited = {source_name}
    distance = {node: 0 for node in node_neighbors}

    while queue:
        node_name = queue.popleft()
        if node_name == end_name:
            return distance[node_name]

        for neighbor in node_neighbors[node_name]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                distance[neighbor] = distance[node_name] + 1

    return float("inf")


def parse_input(path="day12_input.txt"):
    str_matrix = np.genfromtxt(path, delimiter=1, dtype=str)
    matrix = np.zeros(str_matrix.shape, dtype=int)

    start, end = None, None
    node_neighbors = {}
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            node_neighbors[(i, j)] = []
            if str_matrix[i, j] == "S":
                start = (i, j)
                matrix[i, j] = 0
            elif str_matrix[i, j] == "E":
                end = (i, j)
                matrix[i, j] = 26
            else:
                matrix[i, j] = ord(str_matrix[i, j]) - 97

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            this_value = matrix[i, j]
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + direction[0] < matrix.shape[0] and 0 <= j + direction[1] < matrix.shape[1]:
                    neighbor_value = matrix[i+direction[0], j+direction[1]]
                    if neighbor_value - this_value <= 1:
                        node_neighbors[(i, j)].append((i+direction[0], j+direction[1]))

    return node_neighbors, start, end, matrix


def part1():
    node_neighbors, start, end, _ = parse_input()
    print(bfs_step_count(node_neighbors, start, end))


def part2():
    node_neighbors, _, end, heights = parse_input()
    min_distance = len(node_neighbors)**2
    for node in node_neighbors:
        if heights[node] == 0:
            this_distance = bfs_step_count(node_neighbors, node, end)
            min_distance = min(min_distance, this_distance)
    print(min_distance)


if __name__ == "__main__":
    part1()
    part2()
