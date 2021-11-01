# Fibonacci Sequence
# Write a function that takes a number as an argument
# the function should return the "nth" number of the Finonacci sequence


def fib(n):
    if n <= 2:  # The first 2 numbers of the fib sequence are just 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # Recursive functions
        # We use recursion to figure out the previous 2 numbers in the sequence


#print(fib(7), "\n")
#print(fib(50), "\n")  # Will not calculate, takes too long and too many calculations


# Think of this recursive function as a tree.
#
# If n=7, then (n-1) + (n-2) only equals 11.
# Yet fib(n=7) returns 13. How?
# Because of our recursive function, fib(7) will actually create 2 branches (line 13).
#
# fib(7) will create fib(6) and fib(5), which will continue to create branches
# until we get to our base case of 1 or 2 (line 10).
#
# Any time either of these recursive functions get to a 1 or 2, it will return 1.
# It adds each of these 1s to return the final solution.
#
# So, fib(7) creates 13 base cases (13 1s are returned),
# but it takes a long time to calculate because the computer has to
# go through each of these functions and their recursive functions.


#-------------------------------------------------------------------------


# In this variation of the above function, we will utilize memoization


def fibn(n, memo = {}):  # Defining empty database "memo" in argument
    if n in memo:  # If the nth number of the fib seq. is in memo, then...
        return memo[n]  # ... return that stored value INSTEAD of calculating it.
    elif n <= 2:
        return 1
    else:
        memo[n] = fibn(n - 1, memo) + fibn(n - 2, memo)
        # Store the calculation in memo as a key
        # It will calculate the first new iterations, then remember the duplicates
        return memo[n]


print(fibn(7), "\n")
print(fibn(50), "\n")  # Now this number will be calculated in a timely manner
print(fibn(1048), "\n")  # It can't calculate past this number, but it does it very fast.


# Remember, "memo" is just a way of storing information.
# We're using the dictionary-type data structure named "memo"
# to store all return values of the function "fibn"
#
# By storing these return values, the function can remember the
# values and then skip the calculation entirely to save time
# and be efficient.










