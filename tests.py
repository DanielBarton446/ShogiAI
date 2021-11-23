import unittest
import python_shogi.shogi as ps
import alpha_beta as ab
import material_consts as mc
import random

# Note: methods you want to be tested MUST start with test
# To run tests, in console type 
#    python3 -m unittest <testFile>

class TestLegalMoves(unittest.TestCase):

    def setUp(self):
        self.board = ps.Board()

    def test_legal_moves_from_inital_board(self):
        for mv in ab.legal_moves_for_current_player(self.board):
            self.assertEqual(ps.BLACK, self.board.piece_at(mv.from_square).color)

    def test_legal_moves_after_random_legal_move(self):
        moves = ab.legal_moves_for_current_player(self.board)
        self.board.push_usi(moves[random.randint(0, len(moves))].usi())
        for mv in ab.legal_moves_for_current_player(self.board):
            self.assertEqual(ps.WHITE, self.board.piece_at(mv.from_square).color)

    def test_legal_moves_after_any_legal_move(self):
        moves = ab.legal_moves_for_current_player(self.board)
        for mv in moves:
            self.board.push_usi(mv.usi())
            for mv in ab.legal_moves_for_current_player(self.board):
                self.assertEqual(ps.WHITE, self.board.piece_at(mv.from_square).color)
            self.board.reset()



class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.board = ps.Board()

    def test_evaluator_from_initial_board(self):
        self.assertEqual(0.0, ab.evaluator(self.board))

    def test_evaluator_with_extra_black_pawn_in_hand(self):
        self.board.add_piece_into_hand(ps.PAWN, ps.BLACK)
        self.assertEqual(mc.IN_HAND_VALUES.get(ps.PAWN), ab.evaluator(self.board))

    def test_evaluator_with_extra_black_any_piece_in_hand(self):
        for piece_type in ps.PIECE_TYPES_WITHOUT_KING:
            self.board.add_piece_into_hand(piece_type, ps.BLACK)
            evaluation = ab.evaluator(self.board)
            self.assertEqual(mc.IN_HAND_VALUES.get(piece_type), evaluation)
            self.board.reset()

    def test_evaluator_with_two_extra_black_pawns_in_hand(self):
        self.board.add_piece_into_hand(ps.PAWN, ps.BLACK)
        self.board.add_piece_into_hand(ps.PAWN, ps.BLACK)
        self.assertEqual(2 * mc.IN_HAND_VALUES.get(ps.PAWN), ab.evaluator(self.board))


