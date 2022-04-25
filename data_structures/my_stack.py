# April 24, 2022

"""Practice implementation and functions with stacks in Python"""

class StackNode:
	"""Node of stack represented as a singly-linked list"""

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __repr__(self):
		return f'({self.value})->({self.next.value})'

class Stack:
	""""Representation of a stack as a singly-linked list"""

	def __init__(self, capacity=False):
		"""Use a dummy node for the head"""
		self.head = StackNode('head')
		self.head.next = None
		self.top = 0
		self.CAPACITY = capacity

	def __repr__(self):
		if self.top == 0:
			return 'Stack(Empty)'
		out = 'Stack('
		cur = self.head.next
		while cur is not None:
			out += str(cur.value) + '->'
			cur = cur.next
		return out[:-2] + ')'

	def push(self, value):
		if self.isFull():
			print('> Error: The stack is full. Cannot push additional items.')
			return False
		new_node = StackNode(value)
		new_node.next = self.head.next
		self.head.next = new_node
		self.top += 1

	def pop(self):
		if self.isEmpty():
			print('> Error: The stack is empty. Cannot pop.')
			return False
		removed = self.head.next
		self.head.next = self.head.next.next
		self.top -= 1
		return removed

	def peek(self):
		if self.isEmpty():
			print('>Error: Stack is empty. Cannot peek into it.')
			return False
		return self.head.next.value

	def getSize(self):
		return self.top

	def isEmpty(self):
		return self.top <= 0

	def isFull(self):
		if not self.CAPACITY:
			return False
		return self.top >= self.CAPACITY


# Driver Code
if __name__ == "__main__":

	from random import randint

	# Demonstrate the functionality of a Stack
	print('-' * 45)
	print('Push and Pop:')
	stack = Stack(10)
	for i in range(1, 11):
		stack.push(i)
	print(' Stack:', stack)
	for _ in range(5):
		print("   Pop:", stack.pop().value)
	print(' Stack:', stack)

	# New random stack to show additional functionality
	print('-' * 45)
	stack = Stack()
	for _ in range(10):
		stack.push(randint(1, 100))
	print(' Stack:', stack)
	print(' Peek:', stack.peek())
	print(' Capacity:', stack.CAPACITY)
	print(' Empty:', stack.isEmpty())
	print(' Size:', stack.getSize())
	print(' Full:', stack.isFull())
	print(' Attempt to add to the Stack while it is full...')
	stack.push(randint(1, 100))
	print(' Empty the stack...')
	for _ in range(11):
		print('  Pop:', stack.pop().value)
	print(' Stack:', stack)
	print(' Attempt to pop from the Stack while it is empty...')
	stack.pop()
