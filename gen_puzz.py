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


def generate_state(moves):
    state = load_state('/home/benjamin/npuzz/puzzle_states/1')
    for i in range(0, moves):
        state = random_move(state)
    return state
