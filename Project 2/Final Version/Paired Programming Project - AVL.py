#Paired Programming Project 

#Group Members:
#Tyler Nelson
#Robbie Raftis

#Question 2

#Imports 

import sys
import math 
import random
import time

outputdebug = False 

def debug(msg):
	if outputdebug:
		print (msg)

#----------NODE CLASS--------------------------------------------------------------------------

class Node():
	def __init__(self, key):
		self.key = key
		self.left = None 
		self.right = None 


#----------AVL TREE CLASS--------------------------------------------------------------------------

class AVLTree():
	def __init__(self, *args):
		self.node = None 
		self.height = -1  
		self.balance = 0; 

		if len(args) == 1: 
			for i in args[0]: 
				self.insert(i)

	def height(self):
		if self.node: 
			return self.node.height 
		else: 
			return 0 
    
	def is_leaf(self):
		return (self.height == 0) 

 #----------SEARCH--------------------------------------------------------------------------

	def search(self, val):
		current = self.node.key
		#Goes left/right down the binary tree depending on whether val is greater/lower
		if self.node != None:
			if val < current:
				self.node.left.search(val)
			elif val > current:
				self.node.right.search(val)
			else:
				return True


 #----------INSERT NODE--------------------------------------------------------------------------

	def insert(self, key):
		tree = self.node
		
		newnode = Node(key)
		
		if tree == None:
			self.node = newnode 
			self.node.left = AVLTree() 
			self.node.right = AVLTree()
		
		elif key < tree.key: 
			self.node.left.insert(key)
			
		elif key > tree.key: 
			self.node.right.insert(key)
		
		else: 
			print("ERROR: Node key already exists in the AVL Tree!")
			
		self.rebalance() 
	
	#----------DELETE NODE--------------------------------------------------------------------------

	def deleteAVLnode(self):
		val = int(input('Please Enter Node to Delete: '))

		if self.search(val) is False:
			print('ERROR: Node ' + str(val) + ' Not Found!')
			return 

		self.deleteAVLnodeAssist(val)
		self.rebalance() 
		print('Node ' + str(val) + ' has been deleted, and the tree has been rebalanced accordingly')

	def deleteAVLnodeAssist(self, val):
    		
		if self.node is None:
			return self.node


		if val < self.node.key:
			self.node.left.deleteAVLnodeAssist(val)

		elif val > self.node.key:
			self.node.right.deleteAVLnodeAssist(val)

		else:

			if self.node.left is None:
				temp = self.node.right
				self.node = None
				return temp

			elif self.node.right is None:
				temp = self.node.left
				self.node = None
				return temp

			temp = self.node.right.minValueNode()

			self.node = temp

			if self.node != None:
				self.node.right.deleteAVLnodeAssist(temp)

		return self.node

	def minValueNode(self):
    		
		if self.node != None:
			if self.node.left:
				self.node.left.minValueNode()
	

		return self.node
#----------REBALANCE TREE--------------------------------------------------------------------------

	def getValue(self):
    		return self.node.key

	def rebalance(self):
		''' 
		Rebalance a particular (sub)tree
		''' 
		# key inserted. Let's check if we're balanced
		self.update_heights(False)
		self.update_balances(False)
		while self.balance < -1 or self.balance > 1: 
			if self.balance > 1:
				if self.node.left.balance < 0:  
					self.node.left.lrotate() # we're in case II
					self.update_heights()
					self.update_balances()
				self.rrotate()
				self.update_heights()
				self.update_balances()
				
			if self.balance < -1:
				if self.node.right.balance > 0:  
					self.node.right.rrotate() # we're in case III
					self.update_heights()
					self.update_balances()
				self.lrotate()
				self.update_heights()
				self.update_balances()

#----------ROTATE RIGHT--------------------------------------------------------------------------
            
	def rrotate(self):
		# Rotate left pivoting on self
		debug ('Rotating ' + str(self.node.key) + ' right') 
		A = self.node 
		B = self.node.left.node 
		T = B.right.node 
		
		self.node = B 
		B.right.node = A 
		A.left.node = T 


#----------ROTATE LEFT--------------------------------------------------------------------------  

	def lrotate(self):
		# Rotate left pivoting on self
		debug ('Rotating ' + str(self.node.key) + ' left') 
		A = self.node 
		B = self.node.right.node 
		T = B.left.node 
		
		self.node = B 
		B.left.node = A 
		A.right.node = T 
		
 #----------UPDATE HEIGHT--------------------------------------------------------------------------  

	def update_heights(self, recurse=True):
		if not self.node == None: 
			if recurse: 
				if self.node.left != None: 
					self.node.left.update_heights()
				if self.node.right != None:
					self.node.right.update_heights()
			
			self.height = max(self.node.left.height,
								self.node.right.height) + 1 
		else: 
			self.height = -1 
			

#----------UPDATE BALANCE--------------------------------------------------------------------------	

	def update_balances(self, recurse=True):
		if not self.node == None: 
			if recurse: 
				if self.node.left != None: 
					self.node.left.update_balances()
				if self.node.right != None:
					self.node.right.update_balances()

			self.balance = self.node.left.height - self.node.right.height 
		else: 
			self.balance = 0 

#----------FIND LARGEST NODE IN LEFT CHILD--------------------------------------------------------------------------	

	def logical_predecessor(self, node):
		''' 
		Find the biggest valued node in LEFT child
		''' 
		node = node.left.node 
		if node != None: 
			while node.right != None:
				if node.right.node == None: 
					return node 
				else: 
					node = node.right.node  
		return node 


#----------FIND SMALLEST NODE IN RIGHT CHILD--------------------------------------------------------------------------

	def logical_successor(self, node):
		''' 
		Find the smallest valued node in RIGHT child
		''' 
		node = node.right.node  
		if node != None: # just a sanity check  
			
			while node.left != None:
				debug("LS: traversing: " + str(node.key))
				if node.left.node == None: 
					return node 
				else: 
					node = node.left.node  
		return node 

#----------CHECK FOR BALANCE--------------------------------------------------------------------------

	def check_balanced(self):
		if self == None or self.node == None: 
			return True
		
		# We always need to make sure we are balanced 
		self.update_heights()
		self.update_balances()
		return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
		

#----------IN-ORDER TRAVERSAL--------------------------------------------------------------------------

	def inorderTraversal(self):
		if self.node == None:
			return [] 
		
		inlist = [] 
		l = self.node.left.inorderTraversal()
		for i in l: 
			inlist.append(i) 

		inlist.append(self.node.key)

		l = self.node.right.inorderTraversal()
		for i in l: 
			inlist.append(i) 

		return inlist 


#----------DISPLAY TREE--------------------------------------------------------------------------

	def display(self, level=0, pref=''):
		'''
		Display the whole tree (but turned 90 degrees counter-clockwisely). Uses recursive def.
		'''        
		self.update_heights()  # Must update heights before balances 
		self.update_balances()  
		if(self.node != None): 
			print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')    
			if self.node.left != None: 
				self.node.left.display(level + 1, '<')
			if self.node.left != None:
				self.node.right.display(level + 1, '>')
        

#----------PRINT LEAF NODES---------------------------------------------------------------------

	def printLeafNodes(self):

		if self.node != None:
			if self.is_leaf():
				print(self.node.key, end = " ")
			if self.node.left:
				self.node.left.printLeafNodes()
			if self.node.right:
				self.node.right.printLeafNodes() 



#----------PRINT NON-LEAF NODES--------------------------------------------------------------------------

	def printNonLeafNodes(self):

		if self.node != None:
			if not self.is_leaf():
				print(self.node.key, end = " ")
			if self.node.left:
				self.node.left.printNonLeafNodes()
			if self.node.right:
				self.node.right.printNonLeafNodes()   


#----------MAIN PROGRAM--------------------------------------------------------------------------


def main():
	
	print('\nYou have started the AVL Tree Application\n')
	print('------------------------------------------')
		
	values = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
	#time.sleep(2)

	#Display values
	print ("\n\nThe following values have been inserted:")
	for i in values:
		print(i, end=" ")

	#Insert all values 
	Tree = AVLTree() 
	for val in values: 
		Tree.insert(val) 
	
	while True:
		print('\n\nPlease select from the  following options: ')
		print('Options (Input respected number')
		print('(1) Insert A New Integer Key Into The AVL Tree')
		print('(2) Delete An Integer Key From The AVL Tree')
		print('(3) Print the In-Order Traversal Sequence Of The AVL Tree')
		print('(4) Print All Leaf Nodes Of The AVL Tree, And All Non-Leaf Nodes (Separately)')
		print('(5) Display The AVL Tree, Showing Height and Balance Factor For Each Node')
		print('(6) Exit')
		choice2 = str(input('Please enter  your choice here: '))
		time.sleep(0.5)


				
		if choice2 == '1':
			print('\nYou Have Chosen To Insert A New Value Into The AVL Tree')
			time.sleep(0.5)
			while True:
				try:
					AVLInput = int(input("Please Enter A Positive Integer: "))
					break
				except ValueError or AVLInput < 1:
					print("Invalid Input.")
					continue
			Tree.insert(AVLInput)
			print()
				
		elif choice2 == '2':
			Tree.deleteAVLnode()
			time.sleep(0.5)
			print()

		elif choice2 == '3':
			print('\nDisplaying AVL Tree in In-Order...')
			print(Tree.inorderTraversal())

			time.sleep(0.5)
				
		elif choice2 =='4':
			print('\nDisplaying all Leaf/non-leaf nodes seperately...')
			time.sleep(0.5)
			print('Leaf Nodes in Tree...')
			Tree.printLeafNodes()
			print('\n\nNon-Leaf Nodes in Tree...')
			Tree.printNonLeafNodes()
				
		elif choice2 =='5':
			print('\nDisplaying AVL Tree')
			Tree.display()
			time.sleep(0.5)
				
		elif choice2 == '6':
			sys.exit('\nExiting...')
			
		else:
			print('\nInvalid choice\n')
			time.sleep(2)
			pass

if __name__ == "__main__":
	main() 