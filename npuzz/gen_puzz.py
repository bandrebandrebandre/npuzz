from utilities import *
import random
from sets import Set
import copy


class MoveGenerator:
    def __init__(self):
        self.bad_moves = Set([down, right]) #blank always starts in bottom right
        self.all_moves = Set([up, down, left, right])
        self.inverse_move_lookup = {up: down, left: right, down: up, right: left}

    def get_move(self, state):
        remaining_moves = self.all_moves.difference(self.bad_moves)
        while True:
            try:
                candidate_move = random.sample(remaining_moves, 1)[0]
                result = candidate_move(state)
                self.bad_moves = Set([self.inverse_move_lookup[candidate_move]])
                # ^Don't do the inverse of the move you just did next time.
                return result
            except ImpossibleMove:
                self.bad_moves.add(candidate_move)
                continue


def generate_state(n, moves):
    state = load_state('src/npuzz/npuzz/puzzle_states/%s' % n)
    gen = MoveGenerator()
    for i in range(0, moves):
        state = gen.get_move(state)
    return state
