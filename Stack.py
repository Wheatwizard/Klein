class Stack(list):
	def __getitem__(self,key):
		try:
			return super(Stack, self).__getitem__(key)
		except IndexError:
			return 0
	def pop(self):
		try:
			return super(Stack, self).pop()
		except:
			return 0
