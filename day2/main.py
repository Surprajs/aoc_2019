from dis import get_instructions
from operator import is_
from sys import path
path.append("..")
import Intcode

def run_intcode(intcode):
    for i in range(0,intcode.get_length(),4):
        is_finished = intcode.interpret_opcode(i)
        if is_finished:
            return

def part1(text_input="input.txt"):
    intcode1 = Intcode.Intcode(text_input)
    intcode1.change_instruction(1,12)
    intcode1.change_instruction(2,2)
    run_intcode(intcode1)
    return intcode1.get_instruction(0)

from itertools import product

def part2(text_input="input.txt"):
    intcode1 = Intcode.Intcode(text_input)
    original_instructions = intcode1.get_copy_of_instructions()
    for noun, verb in product(list(range(100)),repeat=2):
        intcode1.load_instructions(original_instructions)
        intcode1.change_instruction(1,noun)
        intcode1.change_instruction(2,verb)
        run_intcode(intcode1)
        if intcode1.get_instruction(0) == 19690720:
            return 100*noun + verb
    return -1


print(f"{part1() = }")
print(f"{part2() = }")


