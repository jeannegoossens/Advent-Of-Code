#Day 2

The puzzle for today was about passwords. Each password had to be checked for following company policy, and every password came with its own rule.
The input for each password consisted of: `rule`, `letter` and `password`.

## Part 1
For the first part of the puzzle, each password needed to be checked for how often the given letter occured in that password, and that amount had to be within the range provided by the rule (including boundaries).
Python provides a simple `string.count(subtring, start=..., end=...)` method that can be called on a string, which returns the number of times the substring occurs within the string.
I then only had to check whether that count is within the given limits, and return the number of valid passwords.

## Part 2
For the second part, the rules were different. Now, the given letter had to occur exactly _one_ time in the password at the indices given by the rule numbers (starting at 1 rather than 0).
I created a separate method for this which checks both indices and whether the letter occurs once within those. Then I could count the number of valid passwords.

I regret making a different method for this second part, and I feel like I overlooked a way to use the same function for both parts. I might improve this code once I figure out how to make it more efficient and shorter.
