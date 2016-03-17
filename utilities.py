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
            result.append(line.split())
    return result 


def print_state(state):
    """
    Prittily returns a puzzle state (a 2D array)
    """
    return pprint.pformat(state)


print print_state(load_state('/home/benjamin/npuzz/puzzle_states/1'))
