# Design discussion
This is a pretty simple task so there isn't much 'design' discussion to be had, but here are some of the challenges:

1. need to be able to take input and convert it to a formatted output
2. need to be able to bucket the number into categories
3. need to be able to trim the numbers based on conditions
4. need to be able to truncate, not round, numbers
5. need to be able to return inline

we should try and separate out all the needs into different functions, classes, or methods so that if there are requirements changes they are easily managed

we should evaluate some open source software/stack overflow for each function to ensure we consider edge cases.

We should not consider 'super' large numbers, anything over INT64_MAX is out of scope.

This _could_ all be done with strings... and we could have just a simple table that changes the decimal place based on the length of the string... hmmm.




# Evaluation
## truncate
The truncate discussions on stack overflow (https://stackoverflow.com/questions/783897/truncating-floats-in-python) brought out the fact that many formatters automatically round, but there is some control with the rounding methods (rounding=ROUND_DOWN).  This truncate module actually just uses the string form of the number and just 
