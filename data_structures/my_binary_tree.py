# April 23, 2022

"""Practice implementation and functions with binary trees in Python"""

import my_stack as stack
import my_queue as queue

class TreeNode:
	"""Node of a binary tree"""
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __repr__(self):
		return f"({self.data} -> l:{str(self.left.data)}, r: {str(self.right.data)})"

	def isLeaf(self):
		return self.left is None and self.right is None

class BinaryTree:
	"""Representation of a binary tree using Node objects"""

	def __init__(self, root_value=0):
		self.root = TreeNode(root_value)

	def traverse(self, order='pre', implementation='rec'):
		if order == 'level':
			return self.level_order()
		if order not in ['pre', 'in', 'post']:
			return f'Error: Traversal order "{order}" is not supported.'
		if implementation not in ['rec', 'iter']:
			return f'Error: Implementation must be "rec" or "iter" (not "{implementation}")'
		if order == 'post' and implementation == 'iter':
			return f'Error: Iterative Postorder traversal is not yet supported.'
		f = getattr(self, order + '_order_' + implementation)
		return f(t.root)[:-1]

	def pre_order_rec(self, node, traversal=''):
		if node:
			traversal += str({node.data}) + '-'
			traversal += self.pre_order_rec(node.left)
			traversal += self.pre_order_rec(node.right)
		return traversal

	def pre_order_iter(self, cur, traversal=''):
		s = stack.Stack()
		while True:
			while cur is not None:
				traversal += str({cur.data}) + '-'
				s.push(cur)
				cur = cur.left
			if s.isEmpty():
				break
			else:
				cur = s.pop().value
				cur = cur.right
		return traversal

	def in_order_rec(self, node, traversal=''):
		if node:
			traversal += self.in_order_rec(node.left)
			traversal += str({node.data}) + '-'
			traversal += self.in_order_rec(node.right)
		return traversal

	def in_order_iter(self, cur, traversal=''):
		s = stack.Stack()
		while True:
			while cur is not None:
				s.push(cur)
				cur = cur.left
			if s.isEmpty():
				break
			else:
				cur = s.pop().value
				traversal += str({cur.data}) + '-'
				cur = cur.right
		return traversal

	def post_order_rec(self, node, traversal=''):
		if node:
			traversal += self.post_order_rec(node.left)
			traversal += self.post_order_rec(node.right)
			traversal += str({node.data}) + '-'
		return traversal

	# def post_order_iter(self, cur, traversal=''):
		# Cannot implement without creating a Parent method of a TreeNode

	def level_order(self, traversal=''):
		# Use a queue to store the left & right nodes before taking the root
		q = queue.Queue()
		cur = self.root
		q.enqueue(cur)
		while cur is not None:
			cur = q.dequeue()
			# Add left and right nodes to queue
			if cur.left:
				q.enqueue(cur.left)
			if cur.right:
				q.enqueue(cur.right)
			traversal += str({cur})
		return traversal

def map_to_tree(map):
	"""
	Build a binary tree from a map

	:param dict map: key = node index: value = node data
	:return tree: tree object populated with map key-value pairs
	"""
	t = BinaryTree()
	for i, value in map.items():
		new_node = TreeNode(value)
		if i == 1:
			t.root = new_node
		if 2*i in map:
			new_node.left = TreeNode(map[2 * i])
		if 2*i + 1 in map:
			new_node.right = TreeNode(map[2 * i + 1])

	return t


if __name__ == "__main__":

	# Demonstrate populating a Binary Tree and traversing it
	#				1
	#			 /     \
	#		    2       3
	#		  /  \    /  \
	#		 4   5   6    7

	print('-'*45)
	print('Populate a Binary Tree and traverse it:')
	t = BinaryTree(1)
	t.root.left = TreeNode(2)
	t.root.right = TreeNode(3)
	t.root.left.left = TreeNode(4)
	t.root.left.right = TreeNode(5)
	t.root.right.left = TreeNode(6)
	t.root.right.right = TreeNode(7)
	print('  Pre-Order (Recursive):', t.traverse('pre'))
	print('  Pre-Order (Iterative):', t.traverse('pre', 'iter'))
	print('  In-Order (Recursive):', t.traverse('in'))
	print('  In-Order (Iterative):', t.traverse('in', 'iter'))
	print('  Post-Order (Recursive):', t.traverse('post'))
	print('  Post-Order (Iterative):', t.traverse('post', 'iter'))
	print('  Level-Order:', t.traverse('level'))

	# Demonstrate populating a Binary Tree from a dictionary
	#				a
	#			 /     \
	#		    b       c
	#		  /  \    /  \
	#		 d   e   f    g

	print('-' * 45)
	print('Populate a Binary Tree from a dictionary:')
	tree_mapping = {
		1:'a',
		2:'b',
		3:'c',
		4:'d',
		5:'e',
		6:'f',
		7:'g',
		8:'h',
	}
	t = map_to_tree(tree_mapping)
	print('  Preorder:', t.traverse('pre'))
	print('  Inorder:', t.traverse('in'))
	print('  Postorder:', t.traverse('post'))

	print('-' * 45)

	# TODO: change shortcut for move up/down lines
