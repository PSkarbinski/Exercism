from typing import Literal

"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

def is_sublist(first_list: list[int], second_list: list[int]) -> bool:
    for i in range(0, len(first_list) + 1):
        if not second_list or second_list == first_list[i:i + len(second_list)]:
            return True
    return False

def sublist(list_one: list[int], list_two: list[int]) -> Literal[1, 2, 3, 0]:
    if list_one == list_two:
        return 3
    if is_sublist(list_one, list_two):
        return 2
    if is_sublist(list_two, list_one):
        return 1
    return 0
