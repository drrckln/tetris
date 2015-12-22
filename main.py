from block import blocks
from graphics import render, start_position
from update import update
from validity import valid, valid_move_possible
import random

# copyright Derrick Lin, 2015

# a CurrentBlock is (Block Focal Rotation)
# Block is one of: "I", "L", "rL", "Z", "S"
# Focal is a (x, y) position
# Rotation is one of: "identity", "clockwise", "counterclockwise", "half-turn"
# Blocks are the independent unit, Focal where it is translated to, and
# Rotation the rotation applied


# a GameState is (CurrentBlock, Settled)
# Settled is a list of (x,y) positions
# Move is one of "a", "w", "s", "d", " " (added for debugging convenience)

def main():
    currentblock = (random.choice(blocks.keys()), start_position, "identity")
    settled = [] # all settled positions on the board, initialized with none
    gamestate = (currentblock, settled)

    while valid_move_possible(gamestate):
        render(gamestate)
        move = raw_input("Your move? (a,w,s,d) >> ")
        if move == "x":
            break
        if move not in ["a", "w", "s", "d", " "]:
            print "Invalid input"
            continue
        elif valid(move, gamestate):
            gamestate = update(move, gamestate)
        else:
            print "Your move is invalid"

    print "Game over"

if __name__ == "__main__":
    main()
