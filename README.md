# mprettifier
example prettifier code for fun and profit

# description
Take an input of an integer and get rid of the insignificant digits to make it look better.   It should truncate, not round, numbers and should not show .0

# Examples
```input: 1000000
output: 1M

input: 2500000.34
output: 2.5M

input: 532
output: 532

input: 1123456789
output: 1.1B
```


# Documentation
Documentation for the project is in the ./docs directory

# Running tests
The py.test suite is built into python3 so just run:
`py.test`
