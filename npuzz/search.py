import Queue
import copy
from utilities import *
import time

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


def get_path(node, path=[]):
    path.insert(0, node)
    if node.parent != None:
        return get_path(node.parent, path)
    else:
        return path

class Node:
    """
    A node to be used in the search tree.
    """
    def __init__(self, 
                 state=None, 
                 parent=None):
        self.state = state
        self.parent = parent


class NoSolution(Exception):
    pass


def search(state):
    """
    Searches for the goal state. Returns the path to it from state.
    """
    Q = Queue.PriorityQueue()
    root_tuple = (out_of_place(state), Node(state=state,)) #(priority, data,)
    Q.put(root_tuple)
    while not Q.empty():
        best_node = Q.get()[1]
        print prettify_state(best_node.state)
        for move in [up, down, left, right]:
            try:
                child = Node(parent=best_node)
                child.state = move(best_node.state)
                if check_goal(child.state):
                    return get_path(child)
                estimate = out_of_place(child.state)
                from_root = len(get_path(child))
                child_tuple = (estimate + from_root, child) #(priority, data,)
                Q.put(child_tuple)
            except ImpossibleMove:
                continue
    raise NoSolution()
