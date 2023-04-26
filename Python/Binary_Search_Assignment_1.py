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


# From this we create the base function:
import timeit

def count_rotations(nums):
    pass


# Step 2

# Come up with some example inputs & outputs. Try to cover all edge cases.


tests = [
    # A list of size 10 rotated 3 times.
    {'input': {'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output': 3},

    # A list of size 8 rotated 5 times
    {'input': {'nums': [4, 5, 6, 7, 8, 1, 2, 3]}, 'output': 5},

    # A list that wasn't rotated at all.
    {'input': {'nums': [1, 2, 3, 4, 5, 6, 7, 8]}, 'output': 0},

    # A list that was rotated just once
    {'input': {'nums': [8, 1, 2, 3, 4, 5, 6, 7]}, 'output': 1},

    # A list that was rotated n-1 times, where n is the size of the list.
    {'input': {'nums': [5, 6, 7, 8, 1, 2, 3, 4]}, 'output': 4},

    # A list that was rotated n times (do you get back the original list here?)
    {'input': {'nums': [3, 5, 7, 8, 9, 10]}, 'output': 0},    

    # An empty list.
    {'input': {'nums': []}, 'output': 0},

    # A list containing just one element.
    {'input': {'nums': [42]}, 'output': 0},

    # (more)

    # A list containing multiple identical elements
    {'input': {'nums': [3, 3, 3, 1, 2]}, 'output': 3},

    # A list containing only decreasing elements
    {'input': {'nums': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]}, 'output': 9}
]


# Run test cases and handle index errors ( bugs fixed )

for i, test in enumerate(tests):
    input_nums = test['input']['nums']
    expected_output = test['output']

    start_time = timeit.default_timer()
    actual_output = count_rotations(input_nums)
    end_time = timeit.default_timer()

    if actual_output == expected_output:
        print("\033[92mTest result: Passed\033[0m")
        print("Input:", input_nums)
        print("Expected output:", expected_output)
        print("Actual output:", actual_output)
        print("Execution time:", (end_time - start_time) * 1000, "ms\n")
    else:
        print("\033[91mTest case ", i+1, " - Failed: ", "\033[0m")
        print("Input:", input_nums)
        print("Expected output:", expected_output)
        print("Actual output:", actual_output)
        print("Execution time:", (end_time - start_time) * 1000, "ms\n") 
