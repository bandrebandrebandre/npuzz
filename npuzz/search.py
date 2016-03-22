import Queue
import copy
from utilities import *
import time

def total_out_of_place(state):
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
            except ValueError: #blank tile
                continue
            total += abs(row.index(tile)-x)
            total += abs(state.index(row)-y)
    return total


def num_tiles_not_in_position(state):
    """
    Calculates and returns the number of tiles which are not in their
    final positions.
    """
    n = len(state)
    total = 0
    for row in state:
        for tile in row:
            try:
                y = int(math.floor(float(tile)/n - (float(1)/n)))
                x = (tile - 1) % n
            except ValueError: #blank tile
                continue
            if row.index(tile) - x != 0 or state.index(row) - y != 0:
               total += 1
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


def get_path(node):
    n = node
    path = [node]
    while n.parent != None:
        n = n.parent
        path.insert(0, n)
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


def search(state, heuristic):
    """
    Searches for the goal state. Returns the path to it from state.

    This is A* search.

    Uses "heuristic" as the function for providing underestimates.
    """
    if check_goal(state):
        return [Node(state=state)]
    visited = {}
    Q = Queue.PriorityQueue()
    root_tuple = (heuristic(state), Node(state=state,)) #(priority, data,)
    Q.put(root_tuple)
    while not Q.empty():
        best_node = Q.get()[1]
        for move in [up, down, left, right]:
            try:
                child = Node(parent=best_node)
                child.state = move(best_node.state)
                if check_goal(child.state):
                    return get_path(child)
                estimate = heuristic(child.state)
                from_root = len(get_path(child))
                child_tuple = (estimate + from_root, child) #(priority, data,)
                state_tuple = tupleify_state(child.state)
                if state_tuple not in visited:
                    visited[state_tuple] = len(get_path(child))
                elif visited[state_tuple] < child_tuple[0]:
                    visited[state_tuple] = child_tuple[0]
                else: #We're stuck in a loop, so bail
                    continue
                print estimate
                Q.put(child_tuple)
            except ImpossibleMove:
                continue
    raise NoSolution()
