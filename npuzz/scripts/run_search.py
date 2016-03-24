from npuzz.search import *
from npuzz.utilities import *
from npuzz.gen_puzz import *

def run_search(n, moves, heuristic):
    state = generate_state(n=n, moves=moves)
    print 'Running search on the following: '
    print prettify_state(state)
    if heuristic == total_out_of_place:
        print 'Using the "Total Moves Out Of Place" heuristic.'
        solution = search(state, total_out_of_place)
    elif heuristic == num_tiles_not_in_position:
        print 'Using the "Number of Tiles In Correct Position" heuristic.'
        solution = search(state, num_tiles_not_in_position)
    print 'Here is the solution: '
    for i in solution['path']:
        print prettify_state(i.state)
    print 'Path length: ' + str(len(solution['path']))
    print 'Total unique states visited: %s' % str(solution['unique visited'])
    print 'Total nodes expanded (nonunique included): %s' \
        % str(solution['total expanded'])

def run_search_one():
    """
    Run search on a randomly generated N-puzzle using the "Total Moves 
    Out Of Place" heuristic.

    Usage:
      run_search <n> <moves>

    Options:
      -h --help               Show this screen.
    """
    from docopt import docopt

    args = docopt(run_search_one.__doc__)
    n = args['<n>']
    moves = int(args['<moves>'])
    run_search(n=n, moves=moves, heuristic=total_out_of_place)


def run_search_two():
    """
    Run search on a randomly generated N-puzzle using the "Number of Tiles
    in Correct Position" heuristic.

    Usage:
      run_search <n> <moves>

    Options:
      -h --help               Show this screen.
    """
    from docopt import docopt

    args = docopt(run_search_two.__doc__)
    n = args['<n>']
    moves = int(args['<moves>'])
    run_search(n=n, moves=moves, heuristic=num_tiles_not_in_position)


def compile_stats():
    state = generate_state(n=n, moves=moves)
    if heuristic == total_out_of_place:
        solution = search(state, total_out_of_place)
    elif heuristic == num_tiles_not_in_position:
        solution = search(state, num_tiles_not_in_position)
