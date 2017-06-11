#! /usr/bin/env python

import sys

def isleft(direction):
    return direction == "LEFT" or direction == "L"
def isright(direction):
    return direction == "RIGHT" or direction == "R"
def isnone(direction):
    return direction == "NONE" or direction == "N"

class Machine(object):
    """Represents a Universal Turing Machine."""

    tape = None
    head_pos = None

    def __init__(self):
        self.tape = [0]
        self.head_pos = 0

    def halt(self):
        print "Halting"
        print "Tape:"
        print ''.join(map (str, self.tape))
        print "Final head position:", self.head_pos

    def move(self, direction):
        if isleft(direction):
            self.head_pos -= 1
            if self.head_pos < 0:
                raise ValueError("Moved off left end of tape")
        elif isright(direction):
            self.head_pos += 1
            if self.head_pos >= len(self.tape):
                self.tape.append(0)
        elif isnone(direction):
            pass
        else:
            raise ValueError("Bad MOVE direction %s" % direction)

    def write(self, value):
        if value == "-":
            return
        elif value != 0 and value != 1:
            raise ValueError("Bad WRITE value %s" % value)

        self.tape[self.head_pos] = value

    def full_operation(self, opcode, zerocase, onecase):
        if opcode == "MOVE":
            if self.tape[self.head_pos] == 0:
                self.move(zerocase)
            elif self.tape[self.head_pos] == 1:
                self.move(onecase)
            else:
                raise ValueError("Bad value in tape %s"
                                 % self.tape[self.head_pos])
        elif opcode == "WRITE":
            if self.tape[self.head_pos] == 0:
                self.write(int(zerocase))
            elif self.tape[self.head_pos] == 1:
                self.write(int(onecase))
            else:
                raise ValueError("Bad value in tape %s"
                                 % self.tape[self.head_pos])
        else:
            raise ValueError("Bad opcode %s" % opcode)

    def operate(self, state_register, program):
        arguments = program[state_register].strip().split(' ')
        next_label = None
        if arguments[0][0] == '#':
            return
        elif arguments[0][0] == ':':
            opcode, zerocase, onecase = arguments[1:]
            if len(arguments) > 4:
                next_label = arguments[4]
        else:
            opcode, zerocase, onecase = arguments
            if len(arguments) > 3:
                next_label = arguments[3]

        self.full_operation(opcode, zerocase, onecase)

        if next_label != None:
            line_num = 0
            for line in program:
                if line.split(' ')[0] == next_label:
                    return line_num
                line_num += 1
            raise ValueError("Label %s not found" % next_label)
        return state_register + 1
        
    def run(self, program):
        """Runs a program.

program should be a list of strings.
        """

        state_register = 0
        while state_register < len(program):
            state_register = self.operate(state_register, program)
        self.halt()

def main():
    machine = Machine()
    program = sys.stdin.readlines()
    machine.run(program)

if __name__ == "__main__":
    main()

