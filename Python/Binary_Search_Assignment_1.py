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

import timeit

# From this we create the base function:

def count_rotations(nums):
    pass


# Step 4 - Test Linear Seach Function
 
def count_rotations_linear(nums):
    position = 0       # What is the intial value of position?
    
    while position<len(nums):    # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it

        if position > 0 and nums[position] < nums[position -1]:   # How to perform the check?
            return position
        
        # Move to the next position
        position += 1
    
    return 0       # What if none of the positions passed the check 

# Step 4 ( Binary Search )

def count_rotations_binary(nums):
    lo = 0       
    hi = len(nums)-1
    
    while lo <= hi:
       mid = (lo + hi) // 2
       mid_number = nums[mid]
       #uncomment the next line for logging the values and fixing errors
       # print( "lo:", lo, ", hi:", hi, ",mid:" ",mid_number:", mid)

    if mid > 0 and mid_number < nums[mid-1]:
        # the mid position is the answer 
        return mid  
         
    elif mid_number < nums[hi]:
        # Answer lies on the left half
        hi = mid - 1
        
    else:
        # Answer lies in the right half
        lo = mid + 1
    
    return 0          


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
    

    # A list with multiple rotations.
    {'input': {'nums': [7, 8, 9, 1, 2, 3, 4, 5, 6]}, 'output': 3}

]


# Run test cases and handle index errors ( bugs fixed )

for i, test in enumerate(tests):
    input_nums = test['input']['nums']
    expected_output = test['output']

    start_time = timeit.default_timer()
    actual_output = count_rotations_linear(input_nums) # modify which test function to use here
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


# Step 3 

    # Come up with a correct solution for the problem. State it in plain English.

    # Problem

    # Coming up with the correct solution is quite easy, and it's based on this insight:
    # If a list of sorted numbers is rotated k times, then the smallest number in the list
    # ends up at position k (counting from 0). Further, it is the only number in the list
    # which is smaller than the number before it. Thus, we simply need to check for each
    # number in the list whether it is smaller than the number that comes before it 
    # (if there is a number before it). Then, our answer i.e. the number of rotations 
    # is simply the position of this number is . If we cannot find such a number, 
    #  then the list wasn't rotated at all.

       # Example: In the list [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], 
       # the number 3 is the only number smaller than its predecessor.
       # It occurs at the position 3 (counting from 0), hence the array was rotated 3 times.
    
    # Describe the linear search solution explained above problem in your own words.
       
       # 1. Create  a variable position with value 1
       # 2. Compare the number at current position to the number before it.
       # 3. If the number is smaller than its predecessor, then return position.
       # 4. Otherwise, increment position and repeat until we exhaust all the numbers.


# Step 4

    # Implement the solution and test it using example inputs. Fix bugs, if any.
    # Implement the solution ( Correct Function )  described in step 3

# Step 5 

   # Analyze the algorithm's complexity and identify inefficiencies, if any.

      # Q. What is the worst-case complexity (running time) of the algorithm
      # expressed in the Big O Notation? Assume that the size of the list is N (uppercase)?

      # A: linear_search_complexity = "O(N)"

# Step 6

    # Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

    # Problem - Binary Search

    # The key question we need to answer in binary search is: Given the middle element, 
    # how to decide if it is the answer (smallest number), or whether the answer lies 
    # to the left or right of it.

    # If the middle element is smaller than its predecessor, then it is the answer. 
    # However, if it isn't, this check is not sufficient to determine whether the answer
    # lies to the left or the right of it. Consider the following examples.

    # [7, 8, 1, 3, 4, 5, 6] (answer lies to the left of the middle element)

    # [1, 2, 3, 4, 5, -1, 0] (answer lies to the right of the middle element)

    # Here's a check that will help us determine if the answer lies to the left or
    # the right: If the middle element of the list is smaller than the last element 
    # of the range, then the answer lies to the left of it. Otherwise, the answer
    # lies to the right.

    # Step 3 ( Binary Search )

    # Come up with a correct solution for the above problem. State it in plain English.

         # 1. Start by setting the left index to the first element of the list and the 
         #    right index to the last element.

         # 2. Check to see if the middle element is less than its predessessor.

         # 3. if istep 2 is not then check to see if the middle element is smaller
         #    than the last  element of the list, if so you know the answer is to the
         #    left of the middle number.

         # 4. However if the middle number is greater than the last elemnt in the list then the
         #    correct element should be at the right based on a rotated sorted list.

  
   # Step 4 ( Binary Search )

   

   # Implement the solution and test it using example inputs. Fix bugs, if any.
   # Binary Search Placed under linear function all test cases pass

