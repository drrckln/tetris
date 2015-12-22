from __future__ import print_function
from block import blocks as blocks
from copy import deepcopy

# physical constants
height = 20
width = 20
start_position = [9, 0]

# GameState -> IO Image
# there is a bug where things are shifted too much to the right
def render(gamestate):
    """ Renders the game board, settled pieces, and the current moving block """
    currentblock, settled = gamestate
    currentblock_positions = calculate_positions(currentblock)
    positions_to_draw = deepcopy(settled)

    for pos in currentblock_positions:
        positions_to_draw.append(pos)

    shifted_positions = rendering_shift(positions_to_draw)

    for y in range(height):
        # construct the line and print it
        line = ""

        for x in range(width):
            if (x,y) in shifted_positions:
                line += "*"
            else:
                line += " "

        line = "*" + line + "*"
        print(line)

    # print the floor
    last_line = ""
    for x in range(width+2):
        last_line += "*"
    print(last_line)

# List-of-Positions -> List-of-Positions
def rendering_shift(positions):
    """ Moves all positions rightward 1, to accomodate the border """
    return [(x+1, y) for (x,y) in positions]

# CurrentBlock -> List-of-Positions
def calculate_positions(currentblock):
    """ Finds all the Positions of the CurrentBlock supplied """
    b, f, r = currentblock
    m, n = f

    return [(x+m, y+n) for (x,y) in blocks[b][r]]
