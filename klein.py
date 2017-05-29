import argparse
from interpreter import Interpreter
from KleinException import KleinException

# Checks the surface parameter is in the proper format
def surface(start):
	if len(start) == 4:
		pass
	elif len(start) == 3:
		a=map(int,start)
		if a[0] > 2:raise argparse.ArgumentTypeError("The first number should be at most 2")
		if a[1] > 1:raise argparse.ArgumentTypeError("The second number should be at most 1")
		if a[2] > 1:raise argparse.ArgumentTypeError("The second number should be at most 1")
	else:
		raise argparse.ArgumentTypeError("%s is improper improper length"%start)
	return a

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
	"-a",
	"--ASCII-in",
	action = "store_true",
	help = "Takes input as ASCII code points"
)

parser.add_argument(
	"-A",
	"--ASCII-out",
	action = "store_true",
	help = "Outputs as ASCII code points"
)

parser.add_argument(
	"-c",
	"--ASCII",
	action = "store_true",
	help = "Takes input and outputs by ASCII code points"
)

parser.add_argument(
	"source",
	metavar = "Source",
	help = "The name of the file from which the source is read."
)

parser.add_argument(
	"topology",
	metavar = "Topology",
	type = surface,
	help = "Three bits that denote the topology. (Temporary)"
)

parser.add_argument(
	"input",
	metavar = "Input",
	nargs = "*",
	help = "Integer input."
)

args = parser.parse_args()

with open(args.source) as file:
	source = file.read()

if args.ASCII or args.ASCII_in:
	a=Interpreter(source,map(int,args.topology),map(ord," ".join(args.input)))
else:
	a=Interpreter(source,map(int,args.topology),map(int,args.input))

if args.debug:
	curselib = None
	try:
		import curses
		curselib = curses
	except ImportError:
		try:
			import unicurses
			curselib = unicurses
		except ImportError:
			raise KleinException("Cannot use debug mode without a curses library.  Try installing either curses or unicurses.")
	screen = curselib.initscr()
	curselib.start_color()
	curselib.use_default_colors()
	curselib.init_pair(1, curselib.COLOR_RED, -1)
	while a.direction != [0,0]:
		a.output(screen,0,0)
		try:
			screen.addstr(a.dim,0," ".join(map(str,a.memory)))
		except:pass
		screen.refresh()
		screen.getch()
		try:
			screen.addstr(a.dim,0," "*len(" ".join(map(str,a.memory))))
		except:pass
		a.action()
		a.move()
		curselib.endwin()

else:
	while a.direction != [0,0]:
		a.action()
		a.move()

if args.ASCII or args.ASCII_out:
	print "".join(map(chr,a.memory))
else:	
	print " ".join(map(str,a.memory))
