# Day 5

The goal for today was to find a seat without having a boarding pass.

## Part 1
The first part of this puzzle was basically a binary search. To get from a boardingpass code to a seat id, every letter in the boardingpass code indicated whether to search in the front or the back of the leftover range. The first 7 letters indicated row numbers, and the last 3 indicated seat numbers.
With 128 rows and each row 8 seats, this results in a list of occupied seats.

This exercise can be done with a recursive function but since the list of attempts was always exactly 7 steps for each boardingpass, I looped through the letters and executed the function for each.

## Part 2
The second part required finding the single seat missing in the occupied seats ID. I looped through the list to find the case where the id of the next seat was not 1 higher than the current seat id. That missing id was the empty seat.