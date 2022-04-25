#Paired Programming Project 

#Group Members:
#Tyler Nelson
#Robbie Raftis

#Question 1

#Imports 

import sys
import math 
import random
import time

#Functions 
def createTree(values):
    pass

#Class/Functions
class BinarySearchTree:
    def __init__(self):
        self.root = None 
        self.size = 0

    #Create a new node
    def NewNode(self, value):
        return Node(value)

    #Display Pre-order of BST
    def preOrder(self):
        self.preOrderAssist(self.root)

    def preOrderAssist(self, root):
        if root != None:
            print(root.val, end = " ")
            self.preOrderAssist(root.left)
            self.preOrderAssist(root.right)

    #Display In-order of BST
    def inOrder(self, tree):
        pass

    #Display Post-order of BST
    def postOrder(self, tree):
        pass

    #Display leaf/non-leaf nodes 
    def leafNodes(self, tree):
        pass

    def nonLeafNodes(self, tree):
        pass 

    #Display total number of nodes in subtree 
    def NodeCount(self, tree):
        pass

    #Display depth of subtree at a particular node 
    def depthCalc(self, tree):
        pass 

    #Insert new integer key into BST
    def insertNew(self, value):
        if self.root == None:
            self.root = self.NewNode(value)
        else:
            parent = None 
            current = self.root
            while current != None:
                if value < current.val:
                    parent = current
                    current = current.left
                elif value > current.val:
                    parent = current 
                    current = current.left
                else:
                    return False
            if value < parent.val:
                parent.left = self.NewNode(value)
            else:
                parent.right = self.NewNode(value)
        self.size += 1
        return True

    def minimumValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    #Delete integer key from BST
    def delVal(self, root, value):
        if root is None:
            return root
        elif key > root.key:
            root.right = delVal(root.right, value)
        else:
            if root.left is None:
                temp = root.right 
                root = None 
                return temp 
            elif root.right is None:
                temp = root.left
                root = None 
                return temp
        temp = minimumValue(root.right)
        root.key = temp.key 
        root.right = delVal(root.right, temp.key)
        return root

    def NodeCount(self, root, value):
        pass

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

while True:
    print('\nYou have started the BST Application\nWould you like to pre-load values or use your own?')
    print('------------------------------------------')
    print('Options (Input respected number)\n(1) Pre-load a sequence of integers to build a BST\n(2) Manually enter integer values/keys, one by one, to build a BST\n(q) Quit application')
    choice1 = str(input('Please enter your choice here: '))

    if choice1 == '1':
        values = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
        print('You have selected to pre-load a set of values, which are: ' + values)
        time.sleep(1)
        print('Please select from the following options: ')
        print('Options (Input respected number)\n(1) Display Pre-Order of BST\n(2) Display In-Order of BST\n(3) Display Post-Order of BST\n(4) Display Leaf/non-leaf nodes (Seperately)\n(5) Display total number of nodes of a sub-tree\n(6) Display the depth of a subtree rooted at a particular node\n(7) Insert a new integer key\n(8) Delete an integer key\n(9) Exit')
        choice2 = str(input('Please enter your choice here: '))
        time.sleep(0.5)
        
        if choice2 == '1':
            print('\nDisplaying BST in Pre-Order...')
            time.sleep(0.5)
            print('Pre-Order Tree: \n' + preOrder(values))
        
        elif choice2 == '2':
            print('\nDisplaying BST in In-Order...')
            time.sleep(0.5)
            print('In-Order Tree: \n' + inOrder(values))

        elif choice2 == '3':
            print('\nDisplaying BST in Post-Order...')
            time.sleep(0.5)
            print('Post-Order Tree: \n' + postOrder(values))
        
        elif choice2 =='4':
            print('\nDisplaying all Leaf/non-leaf nodes seperately...')
            time.sleep(0.5)
            print('Leaf/non-leaf nodes in Tree: \n' + leafNodes(values))
        
        elif choice2 =='5':
            print('\nDisplaying total number of nodes in subtree...')
            time.sleep(0.5)
            print('Total number of nodes in subtree: \n' + leafNodes(values))

        elif choice2 == '6':
            print('\nDisplaying depth of subtree rooted at particular node...')
            time.sleep(0.5)
            print('Depth of subtree: \n' + depthCalc(values))
       
        elif choice2 == '7':
            print('\nInserting new integer into BST...')
            time.sleep(0.5)
            print('New BST: \n' + insertNew(value, values))

        elif choice2 == '8':
            print('\nDelete integer from BST...')
            time.sleep(0.5)
            print('New BST: \n' + delVal(value, values))
        
        elif choice2 == '9':
            print('\nExiting...')
            time.sleep(0.5)
            pass

    elif choice1 =='2':
        pass

    elif choice1 == 'q':
        print(' ')
        print('Shutting down...')
        print('Goodbye!')
        time.sleep(2)
        break

    else:
        print(' ')
        print('Invlide choice\n')
        time.sleep(2)
        pass
