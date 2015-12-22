from graphics import calculate_positions, start_position
from block import blocks
from copy import deepcopy
import random

# Move GameState -> GameState
def update(move, gs):
    """ Gives the new GameState, supplying a new random block if needed """
    next_gs = next_gamestate(move, gs)
    moved_block, settled = next_gs

    if block_settling(moved_block, settled):
        new_block = (random.choice(blocks.keys()), start_position, "identity")
        for pos in calculate_positions(moved_block):
            settled.append(pos)
        next_gs = (new_block, settled)

    return next_gs

# Move GameState -> GameState
def next_gamestate(move, gs):
    """ Calculates the next GameState, no settling check """
    currentblock, settled = gs
    b, f, r = deepcopy(currentblock)
    f = move_focal(move, f) # moves focal point downward by 1, possibly also left or right
    r = rotate(r, move) # applies the rotation
    moved_block = (b, f, r)
    return (moved_block, settled)

# Move Focal -> Focal
def move_focal(move, f):
    """ Moves the focal point downward, also left or right as determined by the Move """
    if move == "a":
        f = f[0] - 1, f[1] + 1
    elif move == "d":
        f = f[0] + 1, f[1] + 1
    else:
        f = f[0], f[1] + 1 # moves focal point downward by 1

    return f

# CurrentBlock List-of-Positions -> Boolean
def block_settling(moved_block, settled):
    """ Check for any settled blocks or the floor, under the newly moved block """
    moved_block_positions = calculate_positions(moved_block)
    to_check = [(x,y+1) for (x,y) in moved_block_positions] #bug

    for x,y in to_check:
        if (x,y) in settled:
            return True
        elif y == 20:
            return True

    return False

# Rotation Move -> Rotation
def rotate(current_rotation, move):
    if move in ["a", "d", " "]: # doesn't rotate
        return current_rotation

    rotations = ["identity", "clockwise", "half-turn", "counterclockwise"]
    current_index = rotations.index(current_rotation)
    if move == "w":
        current_index -= 1
    elif move == "s":
        current_index += 1

    return rotations[current_index % 4]
