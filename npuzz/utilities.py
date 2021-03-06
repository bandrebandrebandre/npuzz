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


def tupleify_state(state):
    """
    Returns the state as a tuple
    """
    temp = []
    for row in state:
        temp.append(tuple(row))
    return tuple(temp)


def prettify_state(state):
    """
    Returns a prettified puzzle state (or a 2D array in general)
    """
    return '\n\n'.join([''.join(['{:4}'.format(str(item)) for item in row]) 
        for row in state]).join('\n\n')


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
        return swap(copy.deepcopy(state), blank, left_coord)


def right(state):
    """
    Attempts to move the blank tile (*) right and return the new state.
    """
    blank = find_blank(state)
    right_coord = (blank[0], blank[1] + 1)
    if right_coord[1] == len(state):
        raise ImpossibleMove('Can\'t move right, blank tile is on right edge.')
    else:
        return swap(copy.deepcopy(state), blank, right_coord)



def up(state):
    """
    Attempts to move the blank tile (*) up and return the new state.
    """
    blank = find_blank(state)
    up_coord = (blank[0] - 1, blank[1])
    if up_coord[0] < 0:
        raise ImpossibleMove('Can\'t move up, blank tile is on top edge.')
    else:
        return swap(copy.deepcopy(state), blank, up_coord)


def down(state):
    """
    Attempts to move the blank tile (*) down and return the new state.
    """
    blank = find_blank(state)
    down_coord = (blank[0] + 1, blank[1])
    if down_coord[0] == len(state):
        raise ImpossibleMove('Can\'t move down, blank tile is on bottom edge.')
    else:
        return swap(copy.deepcopy(state), blank, down_coord)

