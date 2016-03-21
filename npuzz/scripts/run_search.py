from npuzz.search import *
from npuzz.utilities import *
from npuzz.gen_puzz import *

def run_search(n, moves):
    state = generate_state(n=n, moves=moves)
    print 'Running search on the following: '
    print prettify_state(state)
    solution = search(state)
    print 'Here is the solution: '
    for i in solution:
        print prettify_state(i.state)

def main():
    """
    Run search on a randomly generated N-puzzle.

    Usage:
      run_search <n> <moves>

    Options:
      -h --help               Show this screen.
    """
    from docopt import docopt

    args = docopt(main.__doc__)
    n = args['<n>']
    moves = int(args['<moves>'])
    run_search(n=n, moves=moves)         
