# Business Case

The customer has asked to display numbers in a more elegant way.   They have asked to truncate numbers to 1 decimal place unless that truncated number is an integer.   It should support 10^6, 10^9, and 10^12 number sizes.


# Acceptance Criteria
* accept a number and return a simplified version
* convert number based on ranges for millions(M), billions(B), and trillions(T)
 * change numbers based on M, B, and T by removing the non-significant digits up to 1/10th of the base range
 * add the number identifier to the end of the number based on the range (M, B, T)
 * do not add an identifier to any number not in a range alone
* truncate and trim numbers
** if number is an integer after truncation, don't display the '.0'
** numbers should not be rounded as stated in the problem statement


# Questions to the Customer
* Should numbers really be rounded?
* Should floats less than 1M keep all significant digits?
