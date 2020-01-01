"""
🎅
--- Day 5: Doesn't He Have Intern-Elves For This? ---
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a 
string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping,
like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx,
abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats
with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between,
even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between
them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair
that appears twice.
How many strings are nice under these new rules?
"""

nice_count = 0
total_count = 0

with open("aoc_5_input.txt") as file_input:
    for puzzle_input in file_input:
        puzzle_input = puzzle_input.rstrip()
        #puzzle_input = "sszjzrkrrzmwwwd"
        total_count += 1
        print(puzzle_input)
        for i, letter in enumerate(puzzle_input):
            if i >= 1:
                if i % 1 == 0 or i % 2 == 0:
                    
            l[1] = l[0] # prev prev
            l[0] = letter # prev
        exit(1)





