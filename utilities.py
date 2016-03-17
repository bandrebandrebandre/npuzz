"""
Various utilities
"""
import pprint

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
                except ValueError: #if its a * character
                    result[-1].append(square)
    return result 


def print_state(state):
    """
    Prittily returns a puzzle state (a 2D array)
    """
    return pprint.pformat(state)


def check_goal(state):
    """
    Returns True if state is the goal state. Otherwise, returns False.

    state is expected to be a 2D array.
    """
    n = len(state[0])
    for i in range(0, n):
        for j in range(0, n):
            if state[i][j] != (j + 1) + (i * n):
                if not(i == j == (n - 1) and state[i][j] == '*'): 
                    return False
    return True

print check_goal(load_state('/home/benjamin/npuzz/puzzle_states/1'))
