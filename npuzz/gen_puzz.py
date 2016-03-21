from utilities import *
from random import randint

def random_move(state):
    options = [up, down, left, right]
    try:
        option = options[randint(0, 3)]
        return option(state)
    except ImpossibleMove:
        try:
            options.remove(option)
            option = options[randint(0, 2)]
            return option(state)
        except ImpossibleMove:
            options.remove(option)
            option = options[randint(0, 1)]
            return option(state)


def generate_state(n=2, moves=0):
    state = load_state('src/npuzz/npuzz/puzzle_states/%s' % n)
    for i in range(0, moves):
        state = random_move(state)
    return state

