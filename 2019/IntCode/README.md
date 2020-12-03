# Advent of IntCode

2019 was a year of repeating puzzles and continued progress on a single puzzle. Every other day revolved around "IntCode". By approximately day 10, this program had evolved almost to an NP-full programming computer. If I understood it correctly.

That was the problem with this IntCode compiler: it was complex, and hard to understand. There was a big risk of errors on one day continuing to the next. And, if you couldn't finish one of them, you couldn't continue with some of the following puzzles.

Let's hope that gets improved in 2020.

The IntCode computer did stick in my mind though. I still want to understand it and build it completely, so that's what I'm going to try.
I'm going back to 2019 AOC and try to complete the IntCode puzzles one by one. I'll document my progress and (hopefully at some point) an explanation on the IntCode computer once I understand it enough.

## The IntCode Computer

### Terms and words

`Intcode program` a list of integers separated by commas

`opcode` (either 1, 2 or 99) indicates what to do

`instruction` combination of opcode and parameters

`address` a position in memory

`instruction pointer` address of the current instruction (after an instruction finishes, the instruction pointer increases the number of values in the instruction)

`noun` the value placed in address 1

`verb` the value placed in address 2

`parameter mode` 0 if position mode, 1 if immediate mode