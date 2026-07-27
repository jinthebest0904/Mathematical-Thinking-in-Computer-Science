# Mathematical-Thinking-in-Computer-Science
Self-learning repository

Algorithm Optimization

First digit = N
Remainder = R

N x 10^k + R = 57R
N x 10^k = 56R

# divide it by 8 on LHS and RHS
N x 10^k-3 x 125 = 7R

# Regard n is 7 since LHS 125 and 10^k-3 cannot be divided by 7
7 x 10^k-3 x 125 = 7R
R = 10^k-3 x 125
R = 125 # The samllest
R = 125 / N = 7

Result = 7125
