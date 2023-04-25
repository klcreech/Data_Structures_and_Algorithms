# Jovian Course - Data Structures and Algorithms - Binary Search Assignment 1


# Problem

# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated
# to obtain the given list. Your function should have the worst-case complexity of O(log N), 
# where N is the length of the list. You can assume that all the numbers in the list are unique.

   # Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# We define "rotating a list" as removing the last element of the list and adding it before the
#  first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

   # "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

# Method

# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

# Step 1 

# State - the problem clearly

# We need to write a program that utilizes a function with a worst-case complexity
# of O(log N) that takes a list of unique numbers sorted an unknown number of times
# and determine the minimum number of times the original sorted list was rotated to
# obtain the given list

# State - input / output formats

    # Q: The function you write will take one input called nums. What does it represent? Give an example.

    # Input

        # nums: nums = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]

        # nums represents a list of numbers that has been obtained by rotating a sorted list an unknown number of times

    # Q: The function you write will return a single output called rotations. What does it represent? Give an example.

    # Output

        # rotations: rotations = count_rotations(nums)

        # rotations represents the minimum number of times the original sorted list was rotated to obtain the given list
