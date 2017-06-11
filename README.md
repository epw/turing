turing
======

Experiments with simulating a Turing machine from scratch.

Plans
=====
Possible instructions:
If on 0, move left, if on 1, move right
If on 0, move right, if on 1, move left
(also still)
So
- If on 0, move *, if on 1, move * (M)
- If on 0, write *, if on 1, write * (W)
- HALT (H)

Wait

Instructions actually do need to behave more like assembly.
Must be able to dictate next state of program counter.
Possibilities are, pseudo-opcodes that talk about the program,
or each operation includes an ID of the next operation. What a pain.
It would be reasonable, given a tape for the program and a mechanical
device, to still have a default of "go to the next value", and
numbers beyond that.

Full syntax:
[label] opcode 0-case 1-case [next label]
label: A human-aiding way to identify a particular line. Optional.
opcode: MOVE or WRITE (or special HALT that lets the real program
terminate)
0-case and 1-case: What to do in case of the current cell being a
0 or 1
  MOVE: Can be LEFT, RIGHT, or NONE
  WRITE: Can be 0, 1, or -
next label: The next command to run, identified by label. If omitted,
move one line down.
