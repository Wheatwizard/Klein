# Klein

Klein is a 2 dimensional language that can be embedded on various topological
surfaces.

# Surfaces

Currently Klein supports 12 distinct topological surfaces.
A topology is denoted by 3 numbers.  Each of the surfaces is represented by a
[fundamental square](https://en.wikipedia.org/wiki/Fundamental_polygon).

## First number

The first bit represents which edges the north edge connects to.  If it is 0 the north edge connects to its
opposite, (that is a pointer moving off the north edge will appear on the south edge and a pointer moving off the west will appear on the east).
If it is 1 the north edge will be connected to the east edge.
If it is 2 the north edge connects to the west edge.

The other edges (not the north or the edge it connects to) will connect to each other.

## Third number

*We are going to skip the second number and come back to it hopefully this makes things clearer*

This determines the whether the north edge has the same direction as its match.
If it is 0 the directions match other wise the directions are opposite.

## Second number

This determines the whether the other pair of edges have the same direction.
If it is 0 the directions match other wise the directions are opposite.

# Memory

The memory is stored in a stack and a scope.  Both are stacks padded with zeros at the bottom.
At the end of execution the contents of the stack are printed.

Like most 2D languages the ip starts in the upper lefthand corner moving east.

# Commands

## Mirrors

- `\` Swaps the x and y directions

- `/` Swaps the x and y directions and multiplies them by -1

- `|` Multiplies the horizontal direction by -1

## Directions

- `>` Tells the ip to move east

- `<` Tells the ip to move west

## Doors

- `[` Reflects the ip if it is moving east; becomes `]` if the ip is moving horizontally

- `]` Reflects the ip if it is moving west; becomes `[` if the ip is moving horizontally

## Jumps

- `!` Skips the next operation

- `?` Pops off the top of the stack and jumps if not zero

## Stack manipulation

- `:` Duplicates the top of the stack

- `$` Swaps the top two items of the stack

- `(` Pops from the stack and pushes to the scope

- `)` Pops from the scope and pushes to the stack

## Literals

- `0`-`9` pushes n to the top of the stack

- `"` Starts and ends a string literal.  During a string literal commands are not run and instead their character values are pushed to the stack.

## Operations

- `+` Adds the top two numbers

- `*` Multiplies the top two numbers

- `-` Multiplies the top by -1

## Control

- `@` Ends execution
