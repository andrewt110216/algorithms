# April 24, 2022

"""Practice implementation and functions with queues in Python"""

class QueueNode:
	"""Node of a queque represented as a singly-linked list"""

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __repr__(self):
		return f'({self.value})->({self.next.value})'

class Queue:
	""""Representation of a queue as a singly-linked list"""

	def __init__(self, capacity=False):
		# pointers for the first node (head) and last node (tail) in queue
		self.head = None
		self.tail = None

		# maximum length of the queue
		self.CAPACITY = capacity

	def __repr__(self):
		if self.getSize == 0:
			return 'Queue(Empty)'
		out = 'Queue('
		cur = self.head
		while cur is not None:
			out += str(cur.value) + '->'
			cur = cur.next
		return out[:-2] + ')'

	def enqueue(self, node_value):
		# Check if queue is full
		if self.isFull():
			print('ERROR: Queue is full. Cannot enqueue.')
			return False
		new_node = QueueNode(node_value)
		# If empty, new node becomes head and tail
		if self.isEmpty():
			self.head = new_node
			self.tail = new_node
		# Otherwise, new node becomes tail
		else:
			self.tail.next = new_node
			self.tail = new_node

	def dequeue(self):
		# If empty, cannot dequeue
		if self.isEmpty():
			print('ERROR: Queue is empty. Cannot dequeue.')
			return False
		# Otherwise, return head node and move head pointer to next node
		dequeued = self.head
		self.head = self.head.next
		return dequeued

	def getSize(self):
		# Use accumulation to count each node
		cur = self.head
		count = 0
		while cur is not None:
			count += 1
			cur = cur.next
		return count

	def isEmpty(self):
		return self.getSize() == 0

	def isFull(self):
		if not self.CAPACITY:
			return False
		return self.getSize() >= self.CAPACITY

	def getPosition(self, value):
		"""Search the queue for the first occurrence of the search value"""
		position = 0
		cur = self.head
		# Iterate over each node until match is found or end of queue
		while cur:
			position += 1
			if cur.value == value:
				return position
			cur = cur.next
		# Return False if no match found
		return False

# Driver Code
if __name__ == "__main__":

	from random import randint

	# Demonstrate the functionality of a Queue

	print('-' * 45)
	print('Enqueue and Dequeue:')
	q = Queue()
	for i in range(1, 11):
		q.enqueue(i)
	print(' Queue:', q)
	print(' Length:', q.getSize())
	print(' Capacity:', q.CAPACITY)
	print(' Is Queue Full?:', ['No', 'Yes'][q.isFull()])
	print(' Dequeue some elements:')
	for _ in range(5):
		print('  Dequeue:', q.dequeue().value)
	print(' Queue:', q)

	# Now use some random values for nodes
	print('-' * 45)
	q = Queue(20)
	for _ in range(20):
		q.enqueue(randint(1, 40))
	print(' Queue:', q)
	print(' Try to add to the Full Queue:')
	q.enqueue(5)
	print(' Search for a random number in the random Queue:')
	target = randint(1, 40)
	print('  Target Value:', target)
	print('  Search Result:', q.getPosition(target))
	print('-' * 45)
