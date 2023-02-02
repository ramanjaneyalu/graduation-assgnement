ASSIGNMENT:

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal
Test cases:

for 5 days: 14/29

for 10 days: 372/773


SOLUTION:

- Generate all possible combinations of absent and present ways.
  - Remove consecutive 4 days absent from the above generated list and get the length of it, which is the solution for 1.
- Remove last day absent from the above list, get the count of it to get the probability that you will miss your graduation ceremony.
  - This will be the solution for 2. Answer will  be in the form "Answer of (2) / Answer of (1)" as per the given format.
    