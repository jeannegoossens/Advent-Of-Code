# Day 1

Today's puzzle was a challenge of finding any combination of two or three numbers from a list that summed up to 2020. The expected answer to the puzzle was the product of those numbers.

## Part 1
My first approach was making a list of [permutations](https://en.wikipedia.org/wiki/Permutation) of two numbers and looping through those to find the permutation that sums to 2020. This returned 2 answers for the first part of the puzzle, which were the same combination of two numbers in two different orders.
I then realized that this was a simpler task, where order did in fact not matter, so I changed the tactic from permuations to [combinations](https://en.wikipedia.org/wiki/Combination), which returned only 1 combination for the right solution.

For this first part, I found the product of these numbers by simply taking the first number times the other.

## Part 2
The second part of the puzzle simply required changing the 2 in the combination function to a 3, to find combinations of three numbers.
I switched to the numpy function `prod()` to find the product of these numbers now, since that would make it more scalable and would not require hardcoding every element into a product function.
