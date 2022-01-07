import python_shogi.shogi as ps
import alpha_beta as ab
import evaluator as evlt
import random
import itertools

class Agent:

    def __init__(self, generator):
        self.gen = generator # This is a function pointer


    # Default is 
    def get_move_from_board_position(self, board : ps.Board):
        # based on self.board, generate the move for the agent
        moves = board.generate_legal_moves()
        length = sum(1 for _ in moves)
        moves = board.generate_legal_moves()
        index = random.randint(0,length - 1)
        move = next(itertools.islice(moves,index,None)).usi()
        return move


class AlphaBetaAgent(Agent):

    def __init__(self, generator, depth, evaluator_flags = [1,1,1,1]):
        self.gen = generator
        self.depth = depth
        self.evaluator_flags = evaluator_flags

    def compute_alpha_beta(self, board : ps.Board):
        # board.turn for player 1 is false, we need to pass in true
        # Thus, negate board.turn
        mv,_ = ab.finale_alpha_beta(board, self.depth, not board.turn, 
                             float('-inf'), float('inf'),
                             self.gen, evlt.evaluator, self.evaluator_flags)
        return mv

    def get_move_from_board_position(self, board : ps.Board):
        return self.compute_alpha_beta(board)



