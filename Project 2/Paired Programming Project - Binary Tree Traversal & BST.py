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

#----------BINARY TREE CLASS--------------------------------------------------------------------------

class BinaryTree:	
	#Initialising Binary Tree || Empty root + Currently empty tree
	def __init__(self):
		self.root = None
		self.size = 0


#----------SEARCH FUNCTION--------------------------------------------------------------------------

	def search(self, val):
		current = self.root
		#Goes left/right down the binary tree depending on whether val is greater/lower
		while current != None:
			if val < current.element:
				current = current.left
			elif val > current.element:
				current = current.right
			else:
				return True 
		return False


#----------INSERT NODE--------------------------------------------------------------------------

	#Proceeds as if searching for element, if present, no insert is needed. If not present, the search leads to a link to a leaf node containing the element
	def insert(self, val):
		if self.root == None:
			self.root = self.NewNode(val) 
		else:
			parent = None
			current = self.root
			while current != None:
				if val < current.element:
					parent = current
					current = current.left
				elif val > current.element:
					parent = current
					current = current.right
				else:
					print("ERROR: node key already exists in the BST!")
					return False 

			if val < parent.element:
				parent.left = self.NewNode(val)
			else:
				parent.right = self.NewNode(val)

		self.size += 1 
		return True


#----------DELETE NODE--------------------------------------------------------------------------


	def delete(self):
		val = int(input('Please Enter Node to Delete: '))
		rootval = self.root

		if self.search(val) is False:
			print('ERROR: Node ' + str(val) + ' Not Found!')
			return 

		self.deleteAssist(rootval, val)
		print('Node ' + str(val) + ' has been deleted')

	def deleteAssist(self, rootval, val):
		if rootval.element == val:
			if rootval.right and rootval.left:
				parent, successor = rootval.right.findMin(rootval)
				if parent.left == successor:
					parent.left = successor.right
				else:
					parent.right = successor.left
				successor.left = rootval.left 
				successor.right = rootval.right
			else:
				if rootval.left:
					return rootval.left 
				else:
					return rootval.right
		else:
			if rootval.element  > val:
				if rootval.left:
					rootval.left = self.deleteAssist(rootval.left, val)
			else:
				if rootval.right:
					rootval.right = self.deleteAssist(rootval.right, val)

		return rootval
		
	
	def findMin(self, parent):
		if self.left:
			return self.left.findMin(self)
		else:
			return parent


#----------DELETE A NODE (ROBBIE)-------------------------------------------------------------------
	
	def deleteNode(self):
		current = self.root
		val = int(input('Please Enter Node To Delete')) 
		while current != None:
			if val < current.element:
				current = current.left
			elif val > current.element:
				current = current.right
			else:
				print('Deleting Node ' + str(self.countSubtreeAssist(current)))
				return     
		print('ERROR: Node ' + str(val) + ' not found!')

				  

#----------PRINT LEAF NODES---------------------------------------------------------------------

	def printLeafNodes(self):
		self.printLeafNodesAssist(self.root)

	def printLeafNodesAssist(self, rootval):
		if rootval != None:
			if rootval.left == None and rootval.right == None:
				print(rootval.element, end = " ")
			if rootval.left:
				self.printLeafNodesAssist(rootval.left)
			if rootval.right:
				self.printLeafNodesAssist(rootval.right)


#----------PRINT NON-LEAF NODES--------------------------------------------------------------------------

	def printNonLeafNodes(self):
		self.printNonLeafNodesAssist(self.root)

	def printNonLeafNodesAssist(self, rootval):
		if rootval != None:
			if rootval.left != None or rootval.right != None:
				print(rootval.element, end = " ")
			if rootval.left:
				self.printNonLeafNodesAssist(rootval.left)
			if rootval.right:
				self.printNonLeafNodesAssist(rootval.right)     

						
#----------POST-ORDER TRAVERSAL--------------------------------------------------------------------------    

	def postorder(self):
		self.postorderAssist(self.root)

	def postorderAssist(self, rootval):
		if rootval != None:
			self.postorderAssist(rootval.left)
			self.postorderAssist(rootval.right)
			print(rootval.element, end = " ")


#----------PRE-ORDER TRAVERSAL--------------------------------------------------------------------------

	def preorder(self):
		self.preorderAssist(self.root)
	
	def preorderAssist(self, rootval):
		if rootval != None:
			print(rootval.element, end = " ")
			self.preorderAssist(rootval.left)
			self.preorderAssist(rootval.right)

#----------IN-ORDER TRAVERSAL-------------------------------------------------------------------

	def inorder(self):
		self.inorderAssist(self.root)

	def inorderAssist(self, rootval):
		if rootval != None:
			self.inorderAssist(rootval.left)
			print(rootval.element, end = " ")
			self.inorderAssist(rootval.right)

#----------CALCULATE NUMBER OF NODES IN SUB-TREE--------------------------------------------------------------------------

	def countSubtree(self):
		current = self.root #55
		val = int(input('Please Enter Node to serve as root: ')) 
		while current != None:
			if val < current.element:
				current = current.left
			elif val > current.element:
				current = current.right
			else:
				print('Number of Nodes in Subtree: ' + str(self.countSubtreeAssist(current)))
				return     
		print('ERROR: Node ' + str(val) + ' not found!')

	def countSubtreeAssist(self, node):
		if node is None:
			return 0
		return 1 + self.countSubtreeAssist(node.left) + self.countSubtreeAssist(node.right)


#----------DEPTH OF SUBTREE--------------------------------------------------------------------------
	def getDepth(self):
		current = self.root #55
		val = int(input('Please Enter Node to serve as root: ')) 
		while current != None:
			if val < current.element:
				current = current.left
			elif val > current.element:
				current = current.right
			else:
				noNodes = self.getDepthAssist(current)
				depth = math.floor(math.log(noNodes, 2))
				#depth = noNodes - 1
				print(depth)
				return     
		print('ERROR: Node ' + str(val) + ' not found!')

	def getDepthAssist(self, node):
		if node is None:
			return 0
		return 1 + self.getDepthAssist(node.left) + self.getDepthAssist(node.right)

#----------MISC--------------------------------------------------------------------------
	def NewNode(self, val):
		return TreeNode(val)
	
	def getSize(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def clear(self):
		self.root == None
		self.size == 0

	def getRoot(self):
		return self.root


#----------NODE CLASS--------------------------------------------------------------------------

class TreeNode:
	def __init__(self, val):
		self.element = val
		self.left = None 
		self.right = None


#----------MAIN PROGRAM--------------------------------------------------------------------------


def main():
	
	print('\nYou have started the BST Application\n')
	print('------------------------------------------')
		
	values = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
	#time.sleep(2)

	#Display values
	print ("\n\nThe following values have been inserted:")
	for i in values:
		print(i, end=" ")

	#Insert all values 
	TreeVal = BinaryTree() 
	for val in values: 
		TreeVal.insert(val) 
	
	while True:
		print('\n\nPlease select from the  following options: ')
		print('Options (Input respected nu mber)\n(1) Display Pre-Order, In-oder and Post-order traversals of BST\n(2) Display Leaf/non-leaf nodes (Seperately)\n(3) Display total number of nodes of a sub-tree\n(4) Display the depth of a subtree rooted at a particular node\n(5) Insert a new integer key\n(6) Delete an integer key\n(7) Exit')
		choice2 = str(input('Please enter  your choice here: '))
		time.sleep(0.5)


				
		if choice2 == '1':
			print('Pre Order:')
			TreeVal.preorder()
			print('\nIn Order:')
			TreeVal.inorder()
			print('\nPost Order:')
			TreeVal.postorder()
			time.sleep(0.5)
			print()
				
		elif choice2 =='2':
			print('\nDisplaying all Leaf/non-leaf nodes seperately...')
			time.sleep(0.5)
			print('Leaf Nodes in Tree...')
			TreeVal.printLeafNodes()
			print('\n\nNon-Leaf Nodes in Tree...')
			TreeVal.printNonLeafNodes()
				
		elif choice2 =='3':
			print('\nDisplaying total number of nodes in subtree...')
			TreeVal.countSubtree()
			time.sleep(0.5)
				

		elif choice2 == '4':
			print('\nDisplaying depth of subtree rooted at particular node...')
			TreeVal.getDepth()
			time.sleep(0.5)
				
				
		elif choice2 == '5':
			while True:
				try:
					BSTInput = int(input("Please Enter A Positive Integer To Insert: "))
					print('\nInserting new integer into BST...')
					break
				except ValueError or BSTInput < 1:
					print("Invalid Input.")
					continue
			TreeVal.insert(BSTInput)
			time.sleep(0.5)


		elif choice2 == '6':
			print('\nDelete integer from BST...')
			TreeVal.delete()
			time.sleep(0.5)
			
				
		elif choice2 == '7':
			print('\nExiting...')
			time.sleep(0.5)
			pass
			
		else:
			print(' ')
			print('Invalid choice\n')
			time.sleep(2)
			pass

if __name__ == "__main__":
	main() 