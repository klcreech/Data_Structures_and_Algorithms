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

# new

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card_new(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


# Test cases with various included edge cases

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

    # Come up with a correct solution for the problem. State it in plain English


    # 1. Create a variable position with the value 0.
    # 2. Check whether the number at index position in card equals query.
    # 3. If it does, position is the answer and can be returned from the function
    # 4. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
    # 5. If the number was not found, return -1.

    # Step 4. 

    # Implement the solution and test it using example inputs. Fix bugs, if any

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

# Step 7
 
  # Come up with a correct solution for the problem. State it in plain English

   # 1. Find the middle element of the list.
   # 2. If it matches queried number, return the middle position as the answer.
   # 3. If it is less than the queried number, then search the first half of the list
   # 4. If it is greater than the queried number, then search the second half of the list
   # 5. If no more elements remain, return -1.
 





