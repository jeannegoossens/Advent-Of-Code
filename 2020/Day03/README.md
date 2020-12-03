# Day 3

This was a fun one! If you sled down a hill in a certain direction, how many trees would block your path? The grid copied to the right infinitely. I half expected it to ask me to find the one route that was free of trees, but that was not the question.

## Part 1
The first part of the puzzle required following a route of 1 down, 3 to the right. I made a simple function that checks whether there is a tree at the current coordinate, then moves to the next row and adds 3 to the x coordinate. If the x coordinate reaches the end of a row, it flips back to 0 to start at the left again.

## Part 2
For this part, there were multiple routes to try, and then the answer was the product of all trees on all those routes. I only needed to change how far I moved to the right each row (at first). So I made that a variable and voila. However there was also a test route where the vertical step increased, so I had to change the way I looped through my grid rows.
Luckily, python provides. Using `grid[::verticalstep]` allowed me to set a step size. In that `[]` there's three values: the first one (before the first colon) is the start, the second one is the end, and the third is the step size. So using `grid[10:50:3]` would loop through rows 10 through 49 of my grid, with a step size of 3, so only hitting 10, 13, 17, etc.

This was a very fun puzzle! I wonder what the image in the Calendar view is going to represent at the end of this...
