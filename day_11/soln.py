from math import prod

RELIEF_ROUNDS = 20
ZERO_RELIEF_ROUNDS = 10000
WORRY_REDUCTION = 3


with open("input.txt") as input:
    monkeys_raw = [line.strip() for line in input.readlines()]
    monkeys = [
        [
            list(map(int, monkeys_raw[7 * i + 1][16:].split(", "))),
            monkeys_raw[7 * i + 2][17:],
            int(monkeys_raw[7 * i + 3].split(" ")[-1]),
            int(monkeys_raw[7 * i + 4].split(" ")[-1]),
            int(monkeys_raw[7 * i + 5].split(" ")[-1]),
        ]
        for i in range((len(monkeys_raw) + 1) // 7)
    ]

monkeys_copy = [
    [data.copy() if type(data) == list else data for data in monkey]
    for monkey in monkeys
]

monkeys_modulo = prod([monkey[2] for monkey in monkeys])

# --------------------------------- Part One ---------------------------------


def process_round(monkeys, inspect_counts, relief, monkeys_modulo):
    for i, monkey in enumerate(monkeys):
        inspect_counts[i] += len(monkey[0])
        monkey, monkeys = process_monkey(monkey, monkeys, relief, monkeys_modulo)
    return monkeys, inspect_counts


def process_monkey(monkey, monkeys, relief, monkeys_modulo):
    while monkey[0]:
        old = monkey[0].pop(0)
        new = eval(monkey[1])
        if relief:
            new //= WORRY_REDUCTION
        else:
            new %= monkeys_modulo
        monkeys[monkey[-(new % monkey[2] == 0) - 1]][0].append(new)
    return monkey, monkeys


inspect_counts = [0] * len(monkeys)

for _ in range(RELIEF_ROUNDS):
    monkeys, inspect_counts = process_round(
        monkeys, inspect_counts, True, monkeys_modulo
    )
inspect_counts.sort(reverse=True)
relief_monkey_business = inspect_counts[0] * inspect_counts[1]

print(
    f"Level of monkey business after {RELIEF_ROUNDS}"
    f" rounds is {relief_monkey_business}"
)

# --------------------------------- Part Two ---------------------------------

inspect_counts = [0] * len(monkeys)

for _ in range(ZERO_RELIEF_ROUNDS):
    monkeys_copy, inspect_counts = process_round(
        monkeys_copy, inspect_counts, False, monkeys_modulo
    )
inspect_counts.sort(reverse=True)
zero_relief_monkey_business = inspect_counts[0] * inspect_counts[1]

print(
    f"Level of monkey business after {ZERO_RELIEF_ROUNDS}"
    f" rounds without any relief is {zero_relief_monkey_business}"
)
