# FizzBuzz Exercise
# The function fizz_buzz() takes an integer argument and returns it, BUT:
# - Fails on zero or negative numbers.
# - Instead returns “Fizz” on multiples of 3.
# - Instead returns “Buzz” on multiples of 5.
# - Instead returns “FizzBuzz” on multiples of 3 and 5.
# - Create an empty function fizz_buzz() and go through the conditions listed above, one by one:
#
# Write a test for the condition.
#
# Edit the fizz_buzz() function until the test passes.
# Then discuss together the different solutions.

import pytest


# Write a function to be tested
def FizzBazz(number):
    if number <= 0:
        raise ValueError("Negative number")
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


# Write the test
def test_FizzBazz():
    assert FizzBazz(1) == 1
    assert FizzBazz(4) == 4
    assert FizzBazz(6) == "Fizz"
    assert FizzBazz(10) == "Buzz"
    assert FizzBazz(15) == "FizzBuzz"
    with pytest.raises(ValueError, match=r"Negative number"):
        FizzBazz(0)
    with pytest.raises(ValueError, match=r"Negative number"):
        FizzBazz(-2)
