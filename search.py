import Queue
import copy
from utilities import *


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

class PuzzleSolution:
    """
    This is the "scratchpad" that search uses to build up the path 
    to a solution.
    """
    def __init__(self):
        self.path = []

    def __init__(self, state):
        self.path = [state]

    def cost(self):
        return len(self.path)

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


class NoSolution(Exception):
    pass


def search(state):
    """
    Searches for the goal state. Returns the path to it from state.
    """
    visited = []

    Q = Queue.PriorityQueue()
    Q.put((0, PuzzleSolution(state)))
    while not Q.empty():
        G = Q.get()
        visited.append(G[1].path[-1:])
        if check_goal(G[1].path[-1:]):
            return G[1].path
        node = G[1].path[-1:]
        traveled = G[1].cost() + 1
        for move in [up, down, left, right]:
            try:
                print prettify_state(node)
                new_node = move(node)
                estimate = out_of_place(new_node)
                solution = copy.copy(G[1])
                solution.append(new_node)
                Q.put((traveled + estimate, solution))
            except ImpossibleMove:
                continue
    raise NoSolution()



