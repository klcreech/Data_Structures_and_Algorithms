
# Lesson 1 - Binary Search, Linked Lists and Complexity
# the following is a test function for the binary search used to test various queries

# Step 1

# We need to write a program to find the position of a given number in a list
# of numbers arranged in decreasing order. We also need to minimize the number
# of times we access elements from the list. Identifu input and output formats.

# Step 2 

# Come up with some example inputs & outputs. Try to cover all edge cases.

import timeit


# Function

def locate_card(cards, query):
     # Create a variable position with the value 0
    position = 0
    # Set up a loop for repetition that also test empty array
    while position < len(cards):
        # Check if element at the current position matches the query
        if cards[position] == query:
            # Answer found! Return and exit..
            return position
        # Increment the position
        position += 1
    # Number not found, return -1
    return -1


# Test cases with various included edge cases

tests = [
    # query occurs in the middle
    {
        'input': { 
            'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
            'query': 7
        },
        'output': 3
    },
    # query is the first element
    {
        'input': {
            'cards': [4, 2, 1, -1],
            'query': 4
        },
        'output': 0
    },
    # query is the last element
    {
        'input': {
            'cards': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
    },
     # cards contains just one element
    {
        'input': {
            'cards': [6],
            'query': 6
        },
        'output': 0
    },

    # Step 3

    # Come up with a correct solution for the problem. State it in plain English


    # 1. Create a variable position with the value 0.
    # 2. Check whether the number at index position in card equals query.
    # 3. If it does, position is the answer and can be returned from the function
    # 4. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
    # 5. If the number was not found, return -1.

    # cards does not contain query
    {
        'input': {
           'cards': [9, 7, 5, 2, -9],
            'query': 4
    },
        'output': -1
    },
     # cards is empty
    {
        'input': {
            'cards': [],
             'query': 7
        },
        'output': -1
    },
     # numbers can repeat in cards
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 7
    }
    # query occurs multiple times
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 0
    }

]

# Run test cases and handle index errors

for i, test in enumerate(tests):
    try:
        stmt = "locate_card(**tests[{}]['input'])".format(i)
        setup = "from __main__ import locate_card, tests"
        time_elapsed = timeit.timeit(stmt, setup=setup, number=1000)
        expected_output = test['output']
        actual_output = locate_card(**test['input'])
        print("Test case ", i+1, " - Input: ", test['input'])
        print("Expected output: ", expected_output)
        print("Actual output: ", actual_output)
        print("Execution time: {:.2f} ms".format(time_elapsed * 1000))
        if actual_output == expected_output:
            print("\033[92mTest result: Passed\033[0m")
        else:
            print("\033[91mTest result: Failed\033[0m")
    except Exception as e:
        print("\033[91mTest case ", i+1, " - Failed: ", e, "\033[0m")

