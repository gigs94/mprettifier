# Business Case

The customer has asked to display numbers in a more elegant way.   They have asked to truncate numbers to 1 decimal place unless that truncated number is an integer.   It should support 10^6, 10^9, and 10^12 number sizes.


# Acceptance Criteria
* accept a number and return a simplified version
* convert number based on ranges for millions(M), billions(B), and trillions(T)
  * change numbers based on M, B, and T by removing the non-significant digits up to 1/10th of the base range
  * add the number identifier to the end of the number based on the range (M, B, T)
  * do not add an identifier to any number not in a range alone
* truncate and trim numbers
  * if number is an integer after truncation, don't display the '.0'
  * numbers should not be rounded as stated in the problem statement


# Questions to the Customer
* Should numbers really be rounded?
* Should floats less than 1M keep all significant digits?
* Should we keep the # of sig digits the same?   e.g.   we are only keeping 1-2 when the number is near a boundary (1,000,000 => 1M; 14000000 => 1.4M) but we are keeping up to 4 when it's near a second boundary (or 6 when it's under 1M),  (123,400,000 => 123.4M;  should this be 120M?)
* Should the input be able to take differnet forms?   1,000,000, 1M, 1000000, 1.0e6(actually this works because python accepts this)
* Should we be able to 'unconvert' from mpretty to int?
* Should we add more types and micro types?   https://en.wikipedia.org/wiki/Metric_prefix
