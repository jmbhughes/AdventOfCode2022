import math

class Monkey:
    def __init__(self, number, items, operation, divisible_test_constant, true_partner, false_partner):
        self.number = number
        self.items = items
        self.operation = operation
        self.divisible_test_constant = divisible_test_constant
        self.true_partner = true_partner
        self.false_partner = false_partner
        self.inspection_count = 0

    def operate(self, value):
        return eval(self.operation.replace("old", str(value)))

    def process_all_items(self, monkey_list, mod_factor=1):
        for worry_level in self.items:
            if mod_factor == 1:
                new_value = self.operate(worry_level) // 3
            else:
                new_value = self.operate(worry_level) % mod_factor
            if new_value % self.divisible_test_constant == 0:
                monkey_list[self.true_partner].add_item(new_value)
            else:
                monkey_list[self.false_partner].add_item(new_value)
            self.inspection_count += 1
        self.items = []

    def add_item(self, worry_level):
        self.items.append(worry_level)


def parse_input(path="day11_input.txt"):
    with open(path) as f:
        lines = f.read().splitlines()

    monkey_index = 0
    monkeys = []
    for i, line in enumerate(lines):
        if i % 7 == 0:  # start of a new monkey
            items = [int(worry) for worry in lines[i+1].split(":")[-1].split(",")]
            operation = lines[i+2].split(":")[-1].split("=")[-1]
            divisible_test_constant = int(lines[i+3].split()[-1])
            true_partner = int(lines[i+4].split()[-1])
            false_partner = int(lines[i+5].split()[-1])
            monkeys.append(Monkey(monkey_index, items, operation, divisible_test_constant, true_partner, false_partner))
            monkey_index += 1
    return monkeys


def part1():
    monkeys = parse_input()
    for _ in range(20):
        for monkey in monkeys:
            monkey.process_all_items(monkeys)
    top_two_monkeys = sorted([monkey.inspection_count for monkey in monkeys])[-2:]
    print(top_two_monkeys[0] * top_two_monkeys[1])


def part2():
    monkeys = parse_input()
    mod_factor = math.lcm(*[monkey.divisible_test_constant for monkey in monkeys])
    for _ in range(10_000):
        for monkey in monkeys:
            monkey.process_all_items(monkeys, mod_factor=mod_factor)
    top_two_monkeys = sorted([monkey.inspection_count for monkey in monkeys])[-2:]
    print(top_two_monkeys[0] * top_two_monkeys[1])


if __name__ == "__main__":
    part1()
    part2()
