"""
Various utilities
"""
import pprint
import copy

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


class ImpossibleMove(Exception):
    pass


def swap(state, one, the_other):
    """
    Takes a n-puzzle state and two tupples as arguements. Swaps the contents
    of one coordinate with the other. Returns the result.
    """
    x1, y1 = one[0], one[1]
    x2, y2 = the_other[0], the_other[1]
    state[x1][y1], state[x2][y2] = state[x2][y2], state[x1][y1]
    return state

def left(state):
    """
    Attempts to move the blank tile (*) left and return the new state.
    """
    for row_num in range(0, len(state)):
        if '*' in state[row_num]:
            blank = (row_num, state[row_num].index('*'),)#coordinates of the *
    left_coord = (blank[0], blank[1] - 1)
    if left_coord[1] < 0:
        raise ImpossibleMove()
    else:
        return swap(copy.copy(state), blank, left_coord)


def right(state):
    """
    Attempts to move the blank tile (*) right and return the new state.
    """
    for row in state:
        if row[-1:] == '*':
            raise ImpossibleMove()


def up(state):
    """
    Attempts to move the blank tile (*) up and return the new state.
    """
    if '*' in state[0]:
        raise ImpossibleMove()


def down(state):
    """
    Attempts to move the blank tile (*) down and return the new state.
    """
    if '*' in state[-1:]:
        raise ImpossibleMove()



print prettify_state(left(load_state('/home/benjamin/npuzz/puzzle_states/1')))
