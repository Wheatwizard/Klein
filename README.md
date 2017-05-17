# Klein

Klein is a 2 dimensional language that can be embedded on various topological
surfaces.

# Surfaces

Currently Klein supports 8 distinct topological surfaces (eventually it should support at least 12).
A topology is denoted by 3 bits.  Each of the surfaces is represented by a
[fundamental square](https://en.wikipedia.org/wiki/Fundamental_polygon).

## First bit

The first bit represents whether the 4 edges map to their opposites or to their
adjacents.  If it is 0 each edge maps to its opposite, (that is a pointer
moving off the west will appear on the east and a pointer moving off
the top will appear on the west).  If it is 1 each edge will map to its
adjacent edge, (east goes to south, west goes to north)

## Second bit

This determines the whether the west edge has the same direction as its match.
If it is 0 the directions match other wise the directions are opposite.

## Third bit

This determines the whether the north edge has the same direction as its match.
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

## Operations

- `+` Adds the north two numbers

- `*` Multiplies the top two numbers

- `-` Multiplies the top by -1

## Control

- `@` Ends execution
