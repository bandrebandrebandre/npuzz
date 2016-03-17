"""
Various utilities for the n-puzzle proceedings.
"""
import pprint
import copy
import math

def load_state(path):
    """
    Load an n-puzzle state from a file into an array and return it.
    """
    result = []
    with open(path) as f:
        for line in f:
            result.append([])
            for square in line.split():
                try:
                    result[-1].append(int(square))
                except ValueError: #if it's a * character
                    result[-1].append(square)
    return result 


def prettify_state(state):
    """
    Returns a prettified puzzle state (or a 2D array in general)
    """
    return '\n'.join([''.join(['{:4}'.format(str(item)) for item in row]) 
        for row in state])


def check_goal(state):
    """
    Returns True if state is the goal state. Otherwise, returns False.
    """
    n = len(state[0])
    for i in range(0, n):
        for j in range(0, n):
            if state[i][j] != (j + 1) + (i * n):
                if not(i == j == (n - 1) and state[i][j] == '*'): 
                    return False
    return True


def out_of_place(state):
    """
    Calculates and returns the number of positions "out of place" each tile
    is. For example, if the 1 tile is at the top-right corner position of an
    8-puzzle, then it would be "2" out of place. If it was in the top left, 
    it would be 0.
    """
    n = len(state)
    total = 0
    for row in state:
        for tile in row:
            try:
                y = int(math.floor(float(tile)/n - (float(1)/n)))
                x = (tile - 1) % n
            except ValueError:
                continue
            total += abs(row.index(tile)-x)
            total += abs(state.index(row)-y)
    return total

class ImpossibleMove(Exception):
    pass


class MalformedPuzzle(Exception):
    pass


def swap(state, one, the_other):
    """
    Takes a n-puzzle state and two tupples as arguments. Swaps the contents
    of one coordinate with the other. Returns the result.
    """
    x1, y1 = one[0], one[1]
    x2, y2 = the_other[0], the_other[1]
    state[x1][y1], state[x2][y2] = state[x2][y2], state[x1][y1]
    return state


def find_blank(state):
    """
    Finds the blank square in a puzzle state
    """
    for row_num in range(0, len(state)):
        if '*' in state[row_num]:
            return (row_num, state[row_num].index('*'),)#coordinates of the *
    else:
        raise MalformedPuzzle('No blank tile found.')


def left(state):
    """
    Attempts to move the blank tile (*) left and return the new state.
    """
    blank = find_blank(state)
    left_coord = (blank[0], blank[1] - 1)
    if left_coord[1] < 0:
        raise ImpossibleMove('Can\'t move left, blank tile is on left edge.')
    else:
        return swap(copy.copy(state), blank, left_coord)


def right(state):
    """
    Attempts to move the blank tile (*) right and return the new state.
    """
    blank = find_blank(state)
    right_coord = (blank[0], blank[1] + 1)
    if right_coord[1] > len(state):
        raise ImpossibleMove('Can\'t move right, blank tile is on right edge.')
    else:
        return swap(copy.copy(state), blank, right_coord)



def up(state):
    """
    Attempts to move the blank tile (*) up and return the new state.
    """
    blank = find_blank(state)
    up_coord = (blank[0] - 1, blank[1])
    if up_coord[0] < 0:
        raise ImpossibleMove('Can\'t move up, blank tile is on top edge.')
    else:
        return swap(copy.copy(state), blank, up_coord)


def down(state):
    """
    Attempts to move the blank tile (*) down and return the new state.
    """
    blank = find_blank(state)
    down_coord = (blank[0] + 1, blank[1])
    if down_coord[0] > len(state):
        raise ImpossibleMove('Can\'t move down, blank tile is on bottom edge.')
    else:
        return swap(copy.copy(state), blank, down_coord)


print out_of_place(load_state('/home/benjamin/npuzz/puzzle_states/1'))
