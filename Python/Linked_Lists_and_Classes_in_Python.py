# Lesson 1.2 - Introduction to Linked Lists and Classes in Python - Jovian


# Problem:

  # Write a function to reverse a linked list


# Definition

  # A linked list is a data structure used for storing a sequence of elements. 
  # It's data with some structure (the sequence).

#create a class named Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
#create object node1
node1 = Node()
#create object node2
node2 = Node()