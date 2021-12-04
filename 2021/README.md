# Advent of Code 2021

This folder contains all my code and inputs for the 2021 challenges. I'm using python 3.

My personal goals for this year's event are
- solving more puzzles than last year (35)
- documenting my code with a short explanation of the algorithm for every script
- revamping my python knowledge, since I have barely touched python the past months, and I would like to get back into it
- trying out new packages and libraries that would be useful for AoC this year

## Day 01
A short script; for a list of integers, check how many of them are higher than their predecessor. And for the second part, use a rolling window sum of size 3 for comparisons.

## Day 02
For a list of instructions with a direction and a distance (e.g. "up 3", "forward 5", "down 2"), calculate the x,y coordinates of a submarine after following these instructions. Then multiply those to get to the answer.

For the second part, another dimension "aim" is added, which adds a diagonal direction and affects the x,y coordinates.
- on "up" decrease the aim with the distance,
- on "down" increase the aim with the distance,
- on "forward" increase x with the distance, and increase y with the distance multiplied by the aim.

I suspect this code might be expanded on in future days' puzzles.

## Day 03
Count the values for each bit in a series of bytes. Construct new bytes out of the most and least occurring numbers for each bit.
For the second part, filter the original list of bytes by whether they follow a pattern defined by bit value occurrence.

## Day 04
A simple game of bingo! Find the first and last board to win and calculate scores for those.