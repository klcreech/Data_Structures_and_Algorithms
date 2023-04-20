# Lesson 1 - Binary Search, Linked Lists and Complexity
# the following is a test function for the binary search used to test various queries

# Problem:

# Alice has some cards with numbers written on them. She arranges the cards in decreasing
# order, and lays them out face down in a sequence on a table. She challenges Bob to pick
# out the card containing a given number by turning over as few cards as possible. Write
# a function to help Bob locate the card.


# - The Method

# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.


# Step 1

# We need to write a program to find the position of a given number in a list
# of numbers arranged in decreasing order. We also need to minimize the number
# of times we access elements from the list. Identify input and output formats.

import timeit

# Test Function ( Step 1 )

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

# Function (linear search) ( Step 4 )
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# Function (binary search) ( Step 7, 8, 9 )
def locate_card_binary(cards, query):
    
    def first_position(nums, target):
        def condition(mid):
            if nums[mid] == target:
                if mid > 0 and nums[mid-1] == target:
                    return 'left'
                return 'found'
            elif nums[mid] < target:
                return 'right'
            else:
                return 'left'
        return binary_search(0, len(nums)-1, condition)

    def last_position(nums, target):
        def condition(mid):
            if nums[mid] == target:
                if mid < len(nums)-1 and nums[mid+1] == target:
                    return 'right'
                return 'found'
            elif nums[mid] < target:
                return 'right'
            else:
                return 'left'
        return binary_search(0, len(nums)-1, condition)

    def first_and_last_position(nums, target):
        return first_position(nums, target), last_position(nums, target)

# Step 2 

# Come up with some example inputs & outputs. Try to cover all edge cases.


tests = [
    # base test
   {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
    },
     # query occurs in the middle
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
    },
    'output': 6
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
    # issue with test 6
    # Come up with a correct solution for the problem. State it in plain English

    # 1. Create a variable position with the value 0.
    # 2. Check whether the number at index position in card equals query.
    # 3. If it does, position is the answer and can be returned from the function
    # 4. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
    # 5. If the number was not found, return -1.

    # Step 4. 

    # Implement the solution and test it using example inputs. Fix bugs, if any

    # Test Function corrected ( No Bugs ) - Continue

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
    },
    # query occurs multiple times
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 6
       },
        'output': 2
    }
  

]

# Run test cases and handle index errors ( bugs fixed )

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

    

    
# Step 5

    # Analyze the algorithm's complexity and identify inefficiencies, if any.

    # Instead of using brute force linear search find solution for binary search

# Step 6

  #  Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.  

# Step 3
 
  # Come up with a correct solution for the problem. State it in plain English

   # 1. Find the middle element of the list.
   # 2. If it matches queried number, return the middle position as the answer.
   # 3. If it is less than the queried number, then search the first half of the list
   # 4. If it is greater than the queried number, then search the second half of the list

# Step 4

  # Implement the solution and test it using example inputs. Fix bugs, if any.



# Test cases
tests = [
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
        },
        'output': 3
    },
    {
        'input': {
            'cards': list(range(100000, 0, -1)),
            'query': 2
        },
        'output': 99998
    }
]

# Step 5

 # Analyze the algorithm's complexity and identify inefficiencies, if any.

 
# new ( Binary Search ) vs ( Linear Search ) test

# Run test cases and print execution times
for i, test in enumerate(tests):
    cards = test['input']['cards']
    query = test['input']['query']
    expected_output = test['output']

    # Test locate_card_linear function
    print(f"\nTest {i+1} for locate_card_linear:\n{'-'*30}")
    print(f"Expected Output: {expected_output}")

    locate_card_linear_time = timeit.timeit(lambda: locate_card_linear(cards, query), number=10000)
    print(f"Execution time for locate_card_linear: {locate_card_linear_time:.8f} seconds")

    # Test locate_card_binary function
    print(f"\nTest {i+1} for locate_card_binary:\n{'-'*30}")
    print(f"Expected Output: {expected_output}")

    locate_card_binary_time = timeit.timeit(lambda: locate_card_binary(cards, query), number=10000)
    print(f"Execution time for locate_card_binary: {locate_card_binary_time:.8f} seconds")

    # Compare the execution times
    if locate_card_linear_time < locate_card_binary_time:
        print("The locate_card_linear function is faster.")
    elif locate_card_linear_time > locate_card_binary_time:
        print("The locate_card_binary function is faster.")
    else:
        print("Both functions have the same execution time.")



