# Lesson 1.2 - Introduction to Linked Lists and Classes in Python - Jovian


# Problem:

  # Write a function to reverse a linked list


# Definition

  # A linked list is a data structure used for storing a sequence of elements. 
  # It's data with some structure (the sequence).

#create a reverse linked list with class LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            
        current_node.next = new_node
    
    def show_elements(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

def reverse(l):
    if l.head is None:
        return
    
    current_node = l.head
    prev_node = None
    
    while current_node is not None:
        # Track the next node
        next_node = current_node.next
        
        # Modify the current node
        current_node.next = prev_node
        
        # Update prev and current
        prev_node = current_node
        current_node = next_node
        
    l.head = prev_node

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

reverse(list2)

list2.show_elements()


