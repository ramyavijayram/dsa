class ArrayStack:
	def __init__(self):
		self._stack=[]

	def isempty(self):
		if len(self._stack)==0:
			return True
		else:
			return False

	def push(self, num):
		self._stack.append(num)

	def pop(self):
		return self._stack.pop(-1)

	def top(self):
		return self._stack[-1]

	def repr(self):
		return self._stack
