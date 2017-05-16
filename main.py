from interpreter import Interpreter
source = """./.....
.>..?\@
.....1.
.......
.\...\.
......."""
a=Interpreter(source,(0,1,1))
while a.direction != [0,0]:
	raw_input()
	print a
	a.action()
	a.move()

print "".join(map(str,a.memory))
