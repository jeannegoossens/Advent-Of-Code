# Day 24 solution

This one is a special and complicated puzzle, so it deserves an analysis.

```A quick note: this puzzle is about a program which takes an input. I will try to keep a clear distinction between program-input and puzzle-input below.```

## The puzzle
The input is a series of instructions consisting of six different types: read, add, multiply, divide, modulo and compare.
Each time the read instruction is executed, it takes a single digit from the program input (the puzzle solution) and processes the instructions. If the z-value at the end of the program input is equal to 0, it was correct.
The solution to the puzzle consists of finding the highest possible valid program input.

## The puzzle-input (the program)
The input for the puzzle is the list of instructions that make up the program.
What's interesting is that these have a clear pattern to them: every so often, a `inp w` command appears, followed by a number of instructions that repeats almost identically each time until the next `inp w` value.
This pattern repeats itself exactly 14 times (the length of the program input).

The only differences between each iteration of the pattern are the second arguments in 3 instructions:
- the fifth instruction takes a number by which to divide z. This is either a 1 or a 26.
- the sixth instruction adds a number to x. This number is either positive or negative.
- the sixteenth instruction adds a number to y.

The numbers used in these instructions tell us something about the set of instructions we are executing for that digit.
1. If the fifth instruction says to divide by 1, the sixth instruction always has a positive number.
2. And when the fifth instruction divides by 26, the sixth one has a negative number.

If we count the number of digits of each type, we know we have exactly 7 type 1 digits and 7 type 2 digits.

## Type 1 digits
When the instructions for a digit tell us to divide by 1 and add a positive number to x, this is a type 1 digit.
Since all instructions for these types of digits are the same, save for the exact numbers given in instructions 6 and 16, we can generalize a pattern from these instructions, and find a formula to solve it.

Let's take the set of instructions for the first type 1 digit and analyse changes in each value:
The only value that is passed on between digits is z, zo we will consider that an unknown value. w is initialized by reading the next digit from the program input.
```
                w           x           y           z
                -------------------------------------
inp w           w                                   z
mul x 0                     0
add x z                     z
mod x 26                  z % 26
div z 1                                             z
add x 10                 z%26 + 10
eql x w                    1 or 0
eql x 0                    0 or 1
mul y 0                                 0
add y 25                                25
mul y x                               0 or 25
add y 1                               1 or 26
mul z y                                           z or 26z
mul y 0                                 0
add y w                                 w
add y 12                              w + 12
mul y x                              0 or w+12
add z y                                          z or 26z + w + 12
```
We now have a formula that gives us the z value at the end of the set of instructions for a digit. Depending on whether w matches z%26+10, the z at the end of the set of instructions is either left as it is, or it is multiplies by 26 and summed with w and 12.

There's one other simplification we can do based on the instructions for all type 1 digits.
The value added in the sixth instruction is always 10 or higher. Since w has to be a number between 1 and 9, w could never be equal to z%26 + the instructions number. That means the equality check in the seventh instruction will never return true. At the end of the set of instructions, we therefore know that z can always be determined by `26z + w + ?` (where ? is replacable with the number given in the 16th instruction for the relevant digit).

Since we don't know the z we start the instruction with just yet, and we need to find the right value for w to have the z and the end of all sets of instructions match 0, we will need to test all possible values of w for all type 1 digits.

## Type 2 digits
When the instructions for a digit tell us to divide by 26 and add a negative number to x, we have a type 2 digit.

We can simplify the instructions for type 2 digits the same way we did for type 1:
```
                w           x           y           z
                -------------------------------------
inp w           w                                   z
mul x 0                     0
add x z                     z
mod x 26                  z % 26
div z 26                                          z // 26   (divide, then round down)
add x -16               z%26 + -16
eql x w                   1 or 0
eql x 0                   0 or 1
mul y 0                                 0
add y 25                                25
mul y x                               0 or 25
add y 1                               1 or 26
mul z y                                         (z//26) or (z//26) * 26
mul y 0                                 0
add y w                                 w
add y 12                              w + 12
mul y x                            0 or w + 12
add z y                                         (z//26) or (z//26)*26 + w+12
```

In this case, we cannot be certain whether the seventh instruction will give us a true or false value.
So depending on the w that we input, z can be determined with either `z // 26` or `(z // 26) * 26 + w + 12`.

## The plan for z
We know that at the end of the 14 digits, we want z to have a value of 0.
When handling type 1 digits, regardless of the w we input, z will be multiplied by 26, with some small additions.

We also know that there is an equal number of type 1 and type 2 digits. So in order to make sure that z can equal 0 at the end, we need to divide z by 26 the same amout of times as we multiply it by 26.
That means that in case of type 2 digits, we always want to choose our w so, that we end up with the `z//26` formula, and not the other one, where z remains roughly the same.
We can do that by making sure to choose a w that is equal to z%26 + -? (where the -? differs for each digit).

Therefore, in type 2 digits, we don't have to iterate through all possible values for w, but we can calculate w from z%26 + -?.
This saves us 7 ** 9 options. This leaves only about 4.5 million possible program input values to iterate through, and we need the highest one that gives a valid end result.

## The code
First I collected all the values that differ across each digit. I used the number given in the 5th instruction for each digit to determine the digits type, and made lists of the indexes of both types of digits.
I made a list containing the numbers given in the 6th and 16th instruction for each digit. I stored these in a list named params.

Then I made a recursive function, which takes the index of the next digit to process, and the value of z at the end of the previous digit. For the first digit, z is initialized at 0.
This function first checks whether we have processed the final digit, and then compares z to 0 to determine success.

Then we look at the digit we are processing. If it is a type 2 digit, we can calculate the right value for w that lets us divide z by 26. If that gives us a w value outside of the possible range (1..9), we know the value for the previous digit would not work, so we go back.
otherwise, we calculate what z will be after processing the current digit and pass it forwards.

If we encounter a type 1 digit, we will loop through all possible values of w for that digit, calculate what z it would give us, and pass that on into the recursion.

In order to get the final correct values for each digit, I created a global array sol (for solution) in which I store the right value for each digit.

```python
def solve(digit, z):
    global sol
    if digit > 13:
        return z == 0
    if digit in type2:
        w = (z % 26) + params[digit][0]
        thenz = int(z/26)
        if w < 1 or w > 9:
            return False
        else:
            sol[digit] = w
            return solve(digit+1, thenz)
    else:
        for w in range(1, 10):
            thenz = (26 * z) + w + params[digit][1]
            if solve(digit + 1, thenz):
                sol[digit] = w
                return True
```

### Credit where it's due
This was a tough puzzle, mostly in that it is a very unique one for Advent of Code. It requires some analysis of the input, and some pattern recognition and simplification, in order to process this in code.
That's a very interesting and different kind of puzzle that Advent of Code usually provides, and it makes this one especially interesting.

I did not figure out all of the above on my own. I couldn't do it last year, then I didn't touch this puzzle for about 11 months, and picked it up again in preparation for AoC 2022.
Since it had been months, I still couldn't figure it out on my own, and I did really want to solve and understand it, I started looking online. I found some youtube videos of people streaming themselves solving this problem, but none of them were as informative as [William Y. Feng's discussion](https://www.youtube.com/watch?v=Eswmo7Y7C4U) of the logic behind the puzzle.
Using his technique I finally solved the puzzle!

This puzzle has been frustrating, especially when I was still trying to fully solve it in code, as I would most other AoC puzzles. That code might still have been running by now if I had left it on since december 2021.
Turns out that's not always the right way to do it. Solving it partially by hand first, taught me a lot about logic and pattern recognition in these sets of instructions, and simplifying them to some short formulas. A very fun and interesting puzzle!