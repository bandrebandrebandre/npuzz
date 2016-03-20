from npuzz.search import *
from npuzz.utilities import *
from npuzz.gen_puzz import *

def run_search():
    state = generate_state(0)
    print 'Running search on the following: '
    print prettify_state(state)
    solution = search(state)
    print 'Here is the solution: '
    for i in solution:
        print prettify_state(i.state)

run_search()
