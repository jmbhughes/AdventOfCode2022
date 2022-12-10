
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []
        self.files = []
        self.parent = None

    @property
    def size(self):
        return sum(f.size for f in self.files) + sum(d.size for d in self.subdirectories)

    def get_subdirectory(self, name):
        for subdir in self.subdirectories:
            if subdir.name == name:
                return subdir
        raise RuntimeError(f"No subdirectory with name={name}")

    @property
    def complete_path(self):
        containment = ""
        current_directory = self
        while current_directory.parent is not None:
            containment = current_directory.name + "/" + containment
            current_directory = current_directory.parent
        return "/" + containment


def load_lines(path="day07_input.txt"):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines


def parse_commands(lines):
    root = Directory("/")
    current_directory = root
    all_directories = [root]

    for line in lines[1:]:
        if line == "$ ls":
            pass
        elif line[:4] == "$ cd":
            to_dir = line.split()[2]
            if to_dir == "..":
                current_directory = current_directory.parent
            else:
                current_directory = current_directory.get_subdirectory(to_dir)
        elif line[:3] == "dir":
            name = line.split()[1]
            new_directory = Directory(name)
            new_directory.parent = current_directory
            current_directory.subdirectories.append(new_directory)
            all_directories.append(new_directory)
        else:
            # It's a file
            size, name = line.split()
            current_directory.files.append(File(name, int(size)))

    return root, all_directories


def part1():
    lines = load_lines()

    _, all_directories = parse_commands(lines)

    total = 0
    for d in all_directories:
        if d.size <= 100_000:
            total += d.size

    print(total)


def part2():
    lines = load_lines()

    root, all_directories = parse_commands(lines)

    free_space = 70000000 - root.size
    target_free_space = 30000000
    delete_amount = target_free_space - free_space

    candidates = [d for d in all_directories if d.size > delete_amount]

    least_candidate = min(candidates, key=lambda d: d.size)

    print(least_candidate.size)


if __name__ == "__main__":
    print("Day 7")
    part1()
    part2()
