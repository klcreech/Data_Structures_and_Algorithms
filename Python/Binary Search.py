#this is a python course by Jovian as I go through the courses I poost them here
# Lesson 1 - Binary Search, Linked Lists and Complexity

# - The Method

# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.


# Assignemnt Problem:

# QUESTION 1: 

# Alice has some cards with numbers written on them. She arranges
# the cards in decreasing order, and lays them out face down in a sequence on 
# a table. She challenges Bob to pick out the card containing a given number
# by turning over as few cards as possible. Write a function to help Bob locate
# the card.



import timeit



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



cards = ['2C', '4D', '6H', '8S', '10C', 'QD', 'KH']
query = '8S'

print("Searching for card:", query)
index = locate_card(cards, query)
if index != -1:
    print("Card found at index:", index)
else:
    print("Card not found in list.")