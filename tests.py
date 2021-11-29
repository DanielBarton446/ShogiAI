import unittest
import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import random

# Note: methods you want to be tested MUST start with test
# To run tests, in console type 
#    python3 -m unittest <testFile>

class TestAlphaBeta(unittest.TestCase):
    def setUp(self):
        self.board = ps.Board()

    def test_finds_checkmate_in_one(self):
        self.board.push_usi('7g7f')
        self.board.push_usi('3c3d')
        self.board.push_usi('8h2b+')
        self.board.push_usi('4a5b')
        self.board.push_usi('B*4b')
        self.board.push_usi('5a4a')
        move,_ = ab.alpha_beta(self.board, 3, True, \
                               float('-inf'), float('inf'))
        self.assertEqual('2b3a', str(move))
        
 
    

class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.board = ps.Board()

######################### EVALUATOR TESTING ####################################

    def test_evaluator_from_initial_board(self):
        self.assertEqual(0.0, evlt.evaluator(self.board))

    def test_white_checkmate_evaluation(self):
        self.board.push_usi('7g7f')
        self.board.push_usi('3c3d')
        self.board.push_usi('8h2b+')
        self.board.push_usi('4a5b')
        self.board.push_usi('B*4b')
        self.board.push_usi('5a4a')
        self.board.push_usi('2b3a')
        self.assertEqual(round(float('inf'), 3), evlt.evaluator(self.board))

######################### SUBROUTINE TESTING ###################################

    def test_count_material_extra_black_pieces(self):
        for piece_type in ps.PIECE_TYPES_WITHOUT_KING:
            self.board.add_piece_into_hand(piece_type, ps.BLACK)
            self.assertEqual(mc.IN_HAND_VALUES.get(piece_type), \
                             evlt.count_material(self.board))
            self.board.reset()

    def test_count_material_two_extra_black_pawns(self):
        self.board.add_piece_into_hand(ps.PAWN, ps.BLACK)
        self.board.add_piece_into_hand(ps.PAWN, ps.BLACK)
        self.assertEqual(2 * mc.IN_HAND_VALUES.get(ps.PAWN), \
                         evlt.count_material(self.board))
    
    def test_count_mobility_from_initial_board(self):
        self.assertEqual(0.0, evlt.count_mobility(self.board))

    def test_count_mobility_with_extra_black_pawn(self):
        self.board.add_piece_into_hand(ps.LANCE, ps.BLACK)

        black_move_count = 0.0
        white_move_count = 0.0
        for _ in self.board.generate_legal_moves():
            black_move_count += 1.0
        self.board.turn = not self.board.turn
        for _ in self.board.generate_legal_moves():
            white_move_count += 1.0
        self.board.turn = not self.board.turn

        total = black_move_count + white_move_count
        difference = black_move_count - white_move_count
        ratio = difference / total

        expected = evlt.mobility_weight * ratio
        self.assertEqual(round(expected,evlt.sig_figs), \
                         evlt.count_mobility(self.board)) 
