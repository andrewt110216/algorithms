# April 7, 2022

"""Practice implementation and functions with linked lists in Python"""

class Node:
	"""Node of a singly-linked list"""

	def __init__(self, data, next_node=None):
		self.data = data
		self.next = next_node

	def __repr__(self):
		return f"{{Node (data={self.data}, next={self.next})}}"


class LinkedList:
	"""Represent a linked list of one or more Nodes"""

	def __init__(self, root=None):
		self.root = root

	def __repr__(self):
		node_values = []
		cur_node = self.root
		while cur_node.next:
			node_values.append(str(cur_node.data))
			cur_node = cur_node.next
		node_values.append(str(cur_node.data))
		return "LinkedList [" + ", ".join(node_values) + "]"

	def add_to_start(self, new_val):
		"""Add a new node as the root of the List and push all other nodes"""
		new_node = Node(new_val)
		new_node.next = self.root
		self.root = new_node

	def add_to_end(self, new_val):
		"""Add a new node to the end of the list"""
		new_node = Node(new_val)
		cur_node = self.root
		while cur_node.next:
			cur_node = cur_node.next
		cur_node.next = new_node

	def insert_after(self, ref_node, new_val):
		"""Insert a new node after a specified node"""
		cur_node = self.root
		while cur_node != ref_node:
			cur_node = cur_node.next
		after_node = cur_node.next
		cur_node.next = Node(new_val)
		cur_node.next.next = after_node

	def get_length(self):
		if not self.root:
			return 0
		cur_node = self.root
		length = 1
		while cur_node.next:
			cur_node = cur_node.next
			length += 1
		return length


if __name__ == "__main__":
	node1 = Node(5)
	mylist = LinkedList(node1)
	node2 = Node(12)
	node1.next = node2
	node3 = Node(2)
	node2.next = node3
	print(mylist)
	print('Adding Node [0] to the beginning of the list...')
	mylist.add_to_start(0)
	print(mylist)
	print('Adding Node [99] at the end of the list...')
	mylist.add_to_end(99)
	print(mylist)
	print('Inserting Node[3] after Node[5]...')
	mylist.insert_after(node1, 3)
	print(mylist)
	print(f'The length of mylist is {mylist.get_length()} nodes.')
	new_nodes = [8, 11, 32, 75]
	print(f'Adding new nodes to the end of the list as follows: {new_nodes}...')
	for value in new_nodes:
		mylist.add_to_end(value)
	print('Done!')
	print(mylist)
	

