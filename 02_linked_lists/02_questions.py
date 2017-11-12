import numpy as np

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def add_to_end(self, new_node):
        n = self
        while n.next_node != None:
            n = n.next_node
        n.next_node = new_node


def printLinkedList(first_node):
    current_node = first_node
    while current_node is not None:
        print "node:", current_node.data
        current_node = current_node.next_node


def removeDuplicates(first_node):
    """
    Question 2.1
    Remove duplicates from an unsorted linked list
    Uses an array as temporary buffer
    """
    values = [first_node.data]
    current_node = first_node
    while current_node.next_node is not None:
        next_node = current_node.next_node
        if next_node.data in values:
            # delete node
            current_node.next_node = next_node.next_node
            if current_node.next_node is None:
                break # done
            next_node.next_node = None
        else:
            values.append(next_node.data)
            current_node = current_node.next_node


def findKtoLast(first_node, k):
    """
    Question 2.2
    Find the kth to last element of a singly linked list
    """
    listLength = 0
    current_node = first_node
    while current_node is not None:
        listLength += 1
        current_node = current_node.next_node
    
    if k > listLength:
        return None
    
    nodeCount = 0
    current_node = first_node
    while current_node is not None:
        nodeCount += 1
        if nodeCount == listLength-k+1:
            return current_node
        current_node = current_node.next_node


