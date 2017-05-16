# Klein

Klein is a 2 dimensional language that can be embedded on various topologocal
surfaces.

# Surfaces

Currently Klein supports 8 distinct topological surfaces (eventually it should support at least 12).
A topology is denoted by 3 bits.  Each of the surfaces is represented by a
fundemental polygon.  

## First bit

The first bit represents whether the edges map to their opposites or to their
adjacents.  If it is 0 each edge maps to its opposite, (that is a pointer
moving off the left will appear on the right and a pointer moving off
the top will appear on the left).  If it is 1 each edge will map to its
adjacent edge, (right goes to bottom, left goes to top)

## Second bit

This determines the whether the left edge has the same direction as its match.
If it is 0 the directions match other wise the directions are opposite.

## Third bit

This determines the whether the top edge has the same direction as its match.
If it is 0 the directions match other wise the directions are opposite.

# Memory

The memory is stored as a stack.  The stack is padded with zeros at the bottom.
At the end of execution the contents of the stack are printed.

# Commands

## Mirrors

- `\` Swaps the x and y directions

- `/` Swaps the x and y directions and multiplies them by -1

- `|` Multiplies the horizontal direction by -1

## Directions

- `>` Tells the ip to move right

- `<` Tells the ip to move left

## Doors

- `[` Reflects ip moving right; becomes `]` if the ip is horizontal

- `]` Reflects ip moving left; becomes `[` if the ip is horizontal

## Jumps

- `!` Skips the next operation

- `?` Pops off the top of the stack and jumps if not zero

## Stack manipulation

- `:` Duplicates the tos

- `$` Swaps the top two items of the stack

## Literals

- `0`-`9` pushes n to the top of th stack

## Operations

- `+` Adds the top two numbers

- `*` Multiplies the top two numbers

- `-` Multiplies the top by -1

## Control

- `@` Ends execution
