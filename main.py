import curses
import argparse
from interpreter import Interpreter

parser = argparse.ArgumentParser(description="Klein Interpreter")

parser.add_argument(
	"-v",
	"--version",
	action = "version",
	version = "%(prog)s 0.0",
	help = "Prints the version number of the interpreter."
)
parser.add_argument(
	"-d",
	"--debug",
	action = "store_true",
	help = "Runs the interpreter in debug mode."
)


parser.add_argument(
	"source",
	metavar = "Source",
	help = "The name of the file from which the source is read."
)

parser.add_argument(
	"topology",
	metavar = "Topology",
	help = "Three bits that denote the topology. (Temporary)"
)

parser.add_argument(
	"input",
	metavar = "Input",
	type = int,
	nargs = "*",
	help = "Integer input."
)

args = parser.parse_args()

with open(args.source) as file:
	source = file.read()

a=Interpreter(source,map(int,args.topology),args.input)

if args.debug:
	screen = curses.initscr()

	while a.direction != [0,0]:
		screen.addstr(0,0,str(a))
		screen.refresh()
		a.action()
		a.move()
		screen.getch()

	curses.endwin()
else:
	while a.direction != [0,0]:
		a.action()
		a.move()
	
print "".join(map(str,a.memory))
