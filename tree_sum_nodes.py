# Youtube Video: Introduction to Trees (DS & Algorithms #9). CS Dojo.
# Practice Question
# Solution by: Andrew Tracey
# 4/5/2022

# Find the sum of all nodes of a binary tree with O(n) time complexity

class Node():
	
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def find_sum(root):
	"""Find the sum of all nodes of a binary tree, given the root node"""
	
	# Complete this algorithm in Big O(n) time complexity
	#  Therefore, we can only visit each node once. In other words, we cannot
	#  traverse our way down the left side of the tree, then go back to the top
	#  and pick a different route.
	#
	# The solution appears to require recurison.
	# At each node, we will add the value of data to the total, and then do
	#  the same for the left and the right nodes of that node.
	# Any time we reach a node (left or right) that is None, we return 0.

	if root == None:
		return 0
	else:
		return root.data + find_sum(root.left) + find_sum(root.right)

# --- Run an Example ---
#        1
#       / \
#      2    3
#     / \  /
#    4  5 6

node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node2 = Node(2, node4, node5)
node3 = Node(3, node6)
my_root = Node(1, node2, node3)

my_tree_sum = find_sum(my_root)  # 21
print(my_tree_sum)
