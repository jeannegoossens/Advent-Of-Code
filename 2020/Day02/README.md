# Day 2

The puzzle for today was about passwords. Each password had to be checked for following company policy, and every password came with its own rule.
The input for each password consisted of: `rule`, `letter` and `password`.

## Part 1
For the first part of the puzzle, each password needed to be checked for how often the given letter occured in that password, and that amount had to be within the range provided by the rule (including boundaries).
Python provides a simple `string.count(subtring, start=..., end=...)` method that can be called on a string, which returns the number of times the substring occurs within the string.
I then only had to check whether that count is within the given limits, and return the number of valid passwords.

## Part 2
For the second part, the rules were different. Now, the given letter had to occur exactly _one_ time in the password at the indices given by the rule numbers (starting at 1 rather than 0).
To do this, I took only the part of the password that is indicated by the first and second index, and submitted that to the existing method, with boundaries 1 and 1 instead of the indices. This way I could count the amount of valid passwords again, with the new rules.
