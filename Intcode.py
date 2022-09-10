from copy import copy

class Intcode:
    def __init__(self, text_input):
        self.instructions = [int(instruction) for instruction in open(text_input).read().split(",")]

    def show_instructions(self):
        print(self.instructions)
        
    def load_instructions(self, new_instructions):
        self.instructions = copy(new_instructions)

    def change_instruction(self, idx, value):
        self.instructions[idx] = value

    def get_instruction(self, idx):
        # print(f"{idx = }")
        return self.instructions[idx]

    def get_instructions(self):
        return self.instructions

    def get_copy_of_instructions(self):
        return copy(self.instructions)

    def get_length(self):
        return len(self.instructions)

    def interpret_opcode(self, idx, debug=False):
        if debug:
            print(f"The opcode at idx={idx} is equal to {self.get_instruction(idx)}.")
        if self.get_instruction(idx) == 1:
            if debug:
                print(f"Changing instruction[{self.get_instruction(idx+3)}] to {self.get_instruction(idx+1)}+{self.get_instruction(idx+2)}={self.get_instruction(idx+1)+self.get_instruction(idx+2)}.\n")
            self.change_instruction(self.get_instruction(idx+3), self.get_instruction(self.get_instruction(idx+1))+self.get_instruction(self.get_instruction(idx+2)))
        elif self.get_instruction(idx) == 2:
            if debug:
                print(f"Changing instruction[{self.get_instruction(idx+3)}] to {self.get_instruction(idx+1)}*{self.get_instruction(idx+2)}={self.get_instruction(idx+1)*self.get_instruction(idx+2)}.\n")
            self.change_instruction(self.get_instruction(idx+3), self.get_instruction(self.get_instruction(idx+1))*self.get_instruction(self.get_instruction(idx+2)))
        elif self.get_instruction(idx) == 99:
            if debug:
                print("The program halts.\n")
            return True
        return False
