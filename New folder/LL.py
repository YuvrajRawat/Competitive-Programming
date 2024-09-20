import random

# Define a class for a Node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Create a linked list with 10 random elements
head = Node(random.randint(1, 100))  # Create the first node
current = head  # Initialize the current node

for _ in range(9):  # Create 9 more random nodes and link them
    new_node = Node(random.randint(1, 100))
    current.next = new_node
    current = new_node

# Print the linked list
print("Linked List:")
print_linked_list(head)
