#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Delete the elements in an linked list whose sum is equal to zero
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_sublists_with_zero_sum(self):
        def get_prefix_sums():
            prefix_sum = 0
            prefix_sums = []
            current = self.head
            while current:
                prefix_sum += current.data
                prefix_sums.append(prefix_sum)
                current = current.next
            return prefix_sums

        prefix_sums = get_prefix_sums()
        prefix_sum_set = set()
        current = self.head
        previous = None

        for prefix_sum in prefix_sums:
            if prefix_sum in prefix_sum_set:
                previous.next = None
            else:
                prefix_sum_set.add(prefix_sum)
                previous = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def create_linked_list_from_input():
    linked_list = LinkedList()
    n = int(input("Enter the number of elements: "))
    for _ in range(n):
        data = int(input("Enter element: "))
        linked_list.insert(data)
    return linked_list

linked_list = create_linked_list_from_input()
print("Original Linked List:")
linked_list.display()

linked_list.delete_sublists_with_zero_sum()
print("Linked List after deleting sublists with zero sum:")
linked_list.display()


# In[2]:


#Reverse a linked list in groups of given size
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_in_groups(self, k):
        if k <= 1 or not self.head:
            return

        prev_group_tail = None
        current_group_head = self.head

        while current_group_head:
            prev = None
            current = current_group_head
            count = 0

            while current and count < k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count += 1

            if prev_group_tail:
                prev_group_tail.next = prev
            else:
                self.head = prev

            prev_group_tail = current_group_head
            current_group_head = current

if __name__ == "__main__":
    linked_list = LinkedList()
    
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input(f"Enter element {i + 1}: "))
        linked_list.append(data)
    
    k = int(input("Enter the group size for reversal: "))

    print("Original Linked List:")
    linked_list.display()

    linked_list.reverse_in_groups(k)

    print(f"Linked List after reversing in groups of {k}:")
    linked_list.display()


# In[4]:


#Merge a linked list into another linked list at alternate positions.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_linked_lists_alternate(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    merged_head = ListNode()  
    current = merged_head

    while head1 and head2:
        current.next = head1
        head1 = head1.next
        current = current.next
        current.next = head2
        head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    if head2:
        current.next = head2

    return merged_head.next 


def create_linked_list():
    values = input("Enter space-separated values for the linked list: ").split()
    head = None
    tail = None

    for val in values:
        new_node = ListNode(int(val))
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


print("Enter values for the first linked list:")
list1 = create_linked_list()

print("Enter values for the second linked list:")
list2 = create_linked_list()

merged_list = merge_linked_lists_alternate(list1, list2)

print_linked_list(merged_list)


# In[6]:


#In an array, Count Pairs with given sum
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def count_pairs_with_sum(head, target_sum):
    frequency = {}
    count = 0

    current = head

    while current:
        complement = target_sum - current.val

        if complement in frequency:
            count += frequency[complement]
        if current.val in frequency:
            frequency[current.val] += 1
        else:
            frequency[current.val] = 1

        current = current.next

    return count // 2  

def create_linked_list(values):
    head = None
    tail = None

    for val in values:
        new_node = ListNode(val)
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


values = input("Enter space-separated values for the linked list: ").split()
head = create_linked_list([int(val) for val in values])

target_sum = int(input("Enter the target sum: "))

pair_count = count_pairs_with_sum(head, target_sum)

print(f"Number of pairs with sum {target_sum}: {pair_count}")


# In[1]:


#Find duplicates in an array
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_duplicates_in_array(arr):
    linked_list = None
    duplicates = set()

    for val in arr:
        if val in duplicates:
            continue  # Skip duplicates that have already been added
        if contains(linked_list, val):
            duplicates.add(val)
        else:
            linked_list = insert(linked_list, val)

    return list(duplicates)

# 
def contains(head, val):
    current = head
    while current:
        if current.val == val:
            return True
        current = current.next
    return False

def insert(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

values = input("Enter space-separated values for the array: ").split()
array = [int(val) for val in values]

duplicate_elements = find_duplicates_in_array(array)

if not duplicate_elements:
    print("No duplicates found.")
else:
    print("Duplicate elements:", duplicate_elements)


# In[2]:


#Find the Kth largest and Kth smallest number in an array
import heapq

def find_kth_largest_and_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None

    min_heap = []
    max_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    kth_smallest = min_heap[0]
    kth_largest = -max_heap[0]

    return kth_smallest, kth_largest

# Example usage:
arr = list(map(int,input().split()))
k = int(input())
result = find_kth_largest_and_smallest(arr, k)
print(f"{k}th Smallest: {result[0]}, {k}th Largest: {result[1]}")


# In[3]:


#Move all the negative elements to one side of the array
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def move_negatives_to_one_side_ll(head):
    if head is None:
        return None

    negative_head = None
    positive_head = None
    negative_tail = None
    current = head

    while current:
        next_node = current.next
        if current.value < 0:
            if negative_head is None:
                negative_head = current
                negative_tail = current
            else:
                negative_tail.next = current
                negative_tail = current
            negative_tail.next = None
        else:
            if positive_head is None:
                positive_head = current
                positive_tail = current
            else:
                positive_tail.next = current
                positive_tail = current
            positive_tail.next = None
        current = next_node

    if negative_head:
        negative_tail.next = positive_head
        return negative_head
    else:
        return positive_head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
arr =list(map(int,input().split()))
head = ListNode(arr[0])
current = head
for value in arr[1:]:
    current.next = ListNode(value)
    current = current.next

print("Original Linked List:")
print_linked_list(head)

new_head = move_negatives_to_one_side_ll(head)
print("Modified Linked List:")
print_linked_list(new_head)


# In[4]:


#Reverse a string using a stack data structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_string = ""

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


input_string =input()
reversed_str = reverse_string(input_string)
print("Original String:", input_string)
print("Reversed String:", reversed_str)


# In[2]:


#Evaluate a postfix expression using stack
def evaluate_postfix(expression):
    stack = []
    operators = "+-*/"

    for token in expression:
        if token not in operators:
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if operand1 is None or operand2 is None:
                return "Invalid expression"

            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                if operand2 == 0:
                    return "Division by zero"
                result = operand1 / operand2

            stack.append(result)

    if len(stack) == 1:
        return stack[0]
    else:
        return "Invalid expression"

postfix_expression =input()
result = evaluate_postfix(postfix_expression)
print("Result:", result)


# In[2]:


class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return "Queue is empty"
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# Create a queue using stacks
queue = QueueUsingStacks()

while True:
    print("Queue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        item = input("Enter the item to enqueue: ")
        queue.enqueue(item)
        print(f"{item} enqueued.")
    elif choice == "2":
        item = queue.dequeue()
        if item:
            print(f"{item} dequeued.")
        else:
            print("Queue is empty.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


# 
