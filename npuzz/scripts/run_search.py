from npuzz.search import *
from npuzz.utilities import *
from npuzz.gen_puzz import *
import csv
from docopt import docopt

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
    args = docopt(run_search_two.__doc__)
    n = args['<n>']
    moves = int(args['<moves>'])
    run_search(n=n, moves=moves, heuristic=num_tiles_not_in_position)


def compile_stats():
    """
    Compile a lot of data using both heuristics

    Usage:
      compile_stats <path_to_output_1> <path_to_output_2>

    Options:
      -h --help               Show this screen.
    """
    args = docopt(compile_stats.__doc__)
 
    repeats = 6
    random_range = 101
    n_range = 10
    results = {}
    heuristic = total_out_of_place
    out = open(args['<path_to_output_1>'], 'w')
    writer = csv.writer(out)
    writer.writerow(['N', 'Level of Randomization', 'Repetition', 'Path Length', 'Unique Nodes Visited', 'Total Nodes Expanded'])
    for n in range(2, n_range):
        results[n] = {}
        for steps in range(1, random_range):
            results[n][steps] = {}
            for repeat in range(1, repeats):
                print 'heuristic= %s n=%i random moves=%i repetition=%i' \
                    % (str(heuristic), n, steps, repeat,)
                solution = search(generate_state(n, steps), heuristic)
                writer.writerow([str(n), 
                                 str(steps), 
                                 str(repeat), 
                                 str(len(solution['path'])),  
                                 str(solution['unique visited']), 
                                 str(solution['total expanded'])
                ])
    out.close()
    heuristic = num_tiles_not_in_position
    out = open(args['<path_to_output_2>'], 'w')
    writer = csv.writer(out)
    writer.writerow(['N', 'Level of Randomization', 'Repetition', 'Path Length', 'Unique Nodes Visited', 'Total Nodes Expanded'])
    for n in range(2, n_range):
        results[n] = {}
        for steps in range(1, random_range):
            results[n][steps] = {}
            for repeat in range(1, repeats):
                solution = search(generate_state(n, steps), heuristic)
                print 'heuristic= %s n=%i random moves=%i repetition=%i' \
                    % (str(heuristic), n, steps, repeat)
                writer.writerow([str(n),
                                 str(steps),
                                 str(repeat),
                                 str(len(solution['path'])),
                                 str(solution['unique visited']),
                                 str(solution['total expanded'])
                ])
    out.close()
