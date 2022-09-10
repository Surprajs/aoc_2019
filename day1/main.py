def part1(text_input="input.txt"):
    return sum([int(number)//3 - 2 for number in open(text_input)])

def recursive_fuel(fuel):
    current_fuel = fuel//3 - 2
    if current_fuel > 0:
        current_fuel += max(0,recursive_fuel(current_fuel))
    return current_fuel

def part2(text_input="input.txt"):
    return sum([recursive_fuel(int(number)) for number in open(text_input)])


print(f"{part1() = }")
print(f"{part2() = }")
