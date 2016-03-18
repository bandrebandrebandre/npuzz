from search import *
from utilities import *
from gen_puzz import *

def run_search():
    state = generate_state(300)
    print 'Running search on the following: '
    print prettify_state(state)
    solution = search(state)
    print 'Here is the solution: '
