from Stack import Stack

class Interpreter(object):
	def __init__(self,source,config,input):
		source = source.strip().split("\n")
		self.dim = max(map(len,source)+[len(source)])
		self.source = [list(x.ljust(self.dim,"."))for x in source]+[["."]*self.dim]*(self.dim-len(source))
		self.direction = [0,1]
		self.location = [0,0]
		self.memory = Stack(input)
		# (matching, >, >>)
		self.config = config
	def wrapAround(self, coord, matching, twist):
		if twist:self.location[1 - coord] = ~self.location[1 - coord]
		if matching:
			self.location = self.location[::-1]
			self.direction = self.direction[::-1]
		self.location[0] %= self.dim
		self.location[1] %= self.dim
	def move(self):
		self.location = [
			self.location[0]+self.direction[0],
			self.location[1]+self.direction[1]
		]
		#Important bit
		if self.location[0] < 0:
			self.wrapAround(0,self.config[0],self.config[2])
		if self.location[1] < 0:
			self.wrapAround(1,self.config[0],self.config[1])
		if self.location[0] >= self.dim:
			self.wrapAround(0,self.config[0],self.config[2-self.config[0]])
		if self.location[1] >= self.dim:
			self.wrapAround(1,self.config[0],self.config[1+self.config[0]])
	def character(self):
		return self.source[self.location[0]][self.location[1]]
	def action(self):
		if self.character() == "/":
			self.direction = map(lambda x:-x,self.direction[::-1])
		if self.character() == "\\":
			self.direction = self.direction[::-1]
		if self.character() == "|":
			self.direction[1] *= -1
		if self.character() == ">":
			self.direction = (0,1)
		if self.character() == "<":
			self.direction = (0,-1)
		if self.character() == "@":
			self.direction = [0,0]
		if self.character() == "[":
			if self.direction[1] == 1:
				self.direction[1] = -1
			if self.direction[1]:
				self.source[self.location[0]][self.location[1]] = "]"
		elif self.character() == "]":
			if self.direction[1] == -1:
				self.direction[1] = 1
			if self.direction[1]:
				self.source[self.location[0]][self.location[1]] = "["
		if self.character() in "0123456879":
			self.memory.append(int(self.character()))
		if self.character() == "+":
			self.memory.append(self.memory.pop()+self.memory.pop())
		if self.character() == "*":
			self.memory.append(self.memory.pop()*self.memory.pop())
		if self.character() == "-":
			self.memory.append(-self.memory.pop())
		if self.character() == ":":
			self.memory.append(self.memory[-1])
		if self.character() == "$":
			a,b=self.memory.pop(),self.memory.pop()
			self.memory.append(a)
			self.memory.append(b)
		if self.character() == "!":
			self.move()
		if self.character() == "?":
			if self.memory.pop():
				self.move()
	def __str__(self):
		#temporary (for debugging purposes)
		return "\n".join(" ".join("+"if [x,y]==self.location else self.source[x][y] for y in range(self.dim)) for x in range(self.dim))
