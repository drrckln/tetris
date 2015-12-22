from update import next_gamestate
from graphics import calculate_positions
from copy import deepcopy

# Move GameState -> Boolean
def valid(move, gs):
    """
    Is the candidate move valid?
    checks against 3 sides and settled blocks, but not top
    """
    return move in valid_moves(gs)

# GameState -> Boolean
def valid_move_possible(gs):
    """ If no valid moves, return False """
    return bool(valid_moves(gs))

# GameState -> List-of-Moves
def valid_moves(gs):
    """
    Applies the move and checks to see whether the new block positions
    would exit the board (top is OK) or be interfered with by a settled block
    """
    moves = ["a", "w", "s", "d", " "]
    valid_moves = []
    settled = gs[1]

    for move in moves:
        next_gs = next_gamestate(move, gs)
        moved_block = next_gs[0]
        move_good = True
        for x,y in calculate_positions(moved_block):
            if (x,y) in settled:
                move_good = False
            elif x < 0 or x > 20:
                move_good = False
            elif y > 20:
                move_good = False
        if move_good == True:
            valid_moves.append(move)

    return valid_moves
