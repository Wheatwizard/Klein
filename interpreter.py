from Stack import Stack

class Interpreter(object):
	def __init__(self,source,config,input):
		source = source.strip().split("\n")
		self.dim = max(map(len,source)+[len(source)])
		self.source = [list(x.ljust(self.dim,"."))for x in source]+[["."]*self.dim]*(self.dim-len(source))
		self.direction = [0,1]
		self.location = [0,0]
		self.memory = Stack(input)
		self.scope = Stack()
		self.read = False
		# (matching, >, >>)
		self.config = config
	def wrapAround(self, coord, match, twist):
		if twist:self.location[1 - coord] = (~self.location[1 - coord]) % self.dim
		if match == 1:
			self.location = self.location[::-1]
			self.direction = self.direction[::-1]
		if match == 2:
			self.location = self.location[::-1]
			self.location[coord] = self.dim - self.location[coord] - 1
			if self.location[1-coord] < 0:
				self.location[1-coord] += 1
			else:
				self.location[1-coord] -= 1
			self.direction = map(lambda x:-x,self.direction[::-1])
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
			if self.config[0] == 2:
				self.wrapAround(1,self.config[0],self.config[2])
			else:
				self.wrapAround(1,self.config[0],self.config[1])
		if self.location[0] >= self.dim:
			if self.config[0] == 0:
				self.wrapAround(0,self.config[0],self.config[2])
			else:
				self.wrapAround(0,self.config[0],self.config[1])
		if self.location[1] >= self.dim:
			if self.config[0] == 1:
				self.wrapAround(1,self.config[0],self.config[2])
			else:
				self.wrapAround(1,self.config[0],self.config[1])
	def character(self):
		return self.source[self.location[0]][self.location[1]]
	def action(self):
		if self.read:
			if self.character() == '"':
				self.read = False
			else:
				self.memory.append(ord(self.character()))
		elif self.character() == "/":
			self.direction = map(lambda x:-x,self.direction[::-1])
		elif self.character() == "\\":
			self.direction = self.direction[::-1]
		elif self.character() == "|":
			self.direction[1] *= -1
		elif self.character() == ">":
			self.direction = [0,1]
		elif self.character() == "<":
			self.direction = [0,-1]
		elif self.character() == "@":
			self.direction = [0,0]
		elif self.character() == "[":
			if self.direction[1] == 1:
				self.direction[1] = -1
			if self.direction[1]:
				self.source[self.location[0]][self.location[1]] = "]"
		elif self.character() == "]":
			if self.direction[1] == -1:
				self.direction[1] = 1
			if self.direction[1]:
				self.source[self.location[0]][self.location[1]] = "["
		elif self.character() in "0123456879":
			self.memory.append(int(self.character()))
		elif self.character() == "+":
			self.memory.append(self.memory.pop()+self.memory.pop())
		elif self.character() == "*":
			self.memory.append(self.memory.pop()*self.memory.pop())
		elif self.character() == "-":
			self.memory.append(-self.memory.pop())
		elif self.character() == ":":
			self.memory.append(self.memory[-1])
		elif self.character() == "$":
			a,b=self.memory.pop(),self.memory.pop()
			self.memory.append(a)
			self.memory.append(b)
		elif self.character() == "!":
			self.move()
		elif self.character() == "?":
			if self.memory.pop():
				self.move()
		elif self.character() == "(":
			self.scope.append(self.memory.pop())
		elif self.character() == ")":
			self.memory.append(self.scope.pop())
		elif self.character() == '"':
			self.read = True
	def output(self,screen,a,b):
		try:
			import curses
			curselib = curses
		except ImportError:
			import unicurses
			curselib = unicurses

		for x in range(self.dim):
			for y in range(self.dim):
				try:
					if [x,y] == self.location:
						if curselib.has_colors():
							screen.addstr(a+x,b+y*2,"X",curselib.color_pair(1))
						else:
							screen.addstr(a+x,b+y*2,"X")
					else:
						screen.addstr(a+x,b+y*2,self.source[x][y])
				except:pass
