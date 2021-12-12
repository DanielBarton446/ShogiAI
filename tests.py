import unittest
import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import alpha_beta as ab
import generators as gens
import game as gm
import Agent as a

# Note: methods you want to be tested MUST start with test
# To run tests, in console type 
#    python3 -m unittest <testFile>

# class TestGeneratorFunctions(unittest.TestCase):
    # def setUp(self):
        # self.board = ps.Board()

    # def test_generate_tsume_moves_no_moves(self):
        # gen = gens.generate_tsume_moves(self.board)
        # try:
            # next(gen)
            # self.assertTrue(False)
        # except:
            # self.assertTrue(True)

    # def test_one_legal(self):
        # self.board = ps.Board("lnsgkgsnl/1r5b1/ppppppppp/7P1/9/9/PPPPPPP1P/1B5R1/LNSGKGSNL b - 1")
        # move = None
        # # Only one move in the generator
        # for mv in gens.generate_attacking_moves(self.board):
            # move = str(mv)
        # self.assertEqual("2d2c", move)

    # def test_attacking_from_hand(self):
        # self.board = ps.Board("k8/9/9/9/9/9/9/9/K8 b N 1")
        # move = None
        # # There is only one move in the generator
        # for mv in gens.generate_attacking_moves(self.board):
            # move = str(mv)
        # self.assertEqual("N*8c", move)

    # def test_legal_moves_in_check(self):
        # self.board = ps.Board("3k5/9/9/9/9/3l5/2P1P4/2LKL4/2S1S4 b N 1")
        # move = None
        # # Only legal move is N*6g
        # for mv in gens.generate_qualifying_moves(self.board):
            # move = mv
        # self.assertEqual("N*6g", str(move))


# class TestAlphaBeta(unittest.TestCase):
    # def setUp(self):
        # self.board = ps.Board()

    # def test_finds_checkmate_in_one(self):
        # self.board.push_usi('7g7f')
        # self.board.push_usi('3c3d')
        # self.board.push_usi('8h2b+')
        # self.board.push_usi('4a5b')
        # self.board.push_usi('B*4b')
        # self.board.push_usi('5a4a')
        # move,val = ab.finale_alpha_beta(self.board, 3, True, \
                               # float('-inf'), float('inf'),
                               # gens.generate_tsume_moves, 
                               # evlt.evaluator)
        # self.assertEqual(float('inf'), val)
        # self.assertEqual('2b3a', str(move))
    
    # def test_gen_function(self):
        # self.board = ps.Board("ln1g4l/1r1sk4/2p1p1+Pp1/p7p/4B1p2/2PP5/P3PP2P/2+pS2S2/LN2KG2L b BGN2Prgsn2p 1")
        # # for mv in gens.generate_tsume_moves(self.board):
            # # print(mv)

    # def test_finds_checkmate_in_three(self):
        # self.board = ps.Board("ln1g4l/1r1sk4/2p1p1+Pp1/p7p/4B1p2/2PP5/P3PP2P/2+pS2S2/LN2KG2L b BGN2Prgsn2p 1")
        # move,val = ab.finale_alpha_beta(self.board, 3, True, \
                               # float('-inf'), float('inf'),
                               # gens.generate_tsume_moves, 
                               # evlt.evaluator)
        # self.assertEqual(float('inf'), val)

    # def test_finds_checkmate_in_three_1(self):
        # self.board = ps.Board("l2+R3nl/3ngsgb1/4pp1p1/p1Pk2PPp/6+b2/PPpPGP2P/2GS4N/1K7/L3r3L b N3P2sp 1")
        # move,val = ab.finale_alpha_beta(self.board, 3, True, \
                               # float('-inf'), float('inf'),
                               # gens.generate_tsume_moves, 
                               # evlt.evaluator)
        # self.assertEqual(float('inf'), val)

    # def test_finds_checkmate_in_five(self):
        # self.board = ps.Board("6snl/2+P1k1g2/p1+B1pp1p1/3pl1p1p/1p3S1P1/3+b2Pl1/PP3PK1P/7R1/5+s1NL b 2G2Prg2snp 1")
        # move,val = ab.finale_alpha_beta(self.board, 5, True, \
                               # float('-inf'), float('inf'),
                               # gens.generate_tsume_moves, 
                               # evlt.evaluator)
        # self.assertEqual(float('inf'), val)

    # def test_finds_checkmate_in_seven(self):
        # self.board = ps.Board("6snl/2+P1k1g2/p1+Bppp1p1/4l1p1p/1p3S1P1/3+b2Pl1/PP3PK1P/7R1/5+n1NL b 2GN3Prg2sp 1")
        # move,val = ab.finale_alpha_beta(self.board, 5, True, \
                               # float('-inf'), float('inf'),
                               # gens.generate_tsume_moves, 
                               # evlt.evaluator)
        # self.assertEqual(float('inf'), val)


# class TestEvaluator(unittest.TestCase):

    # def setUp(self):
        # self.board = ps.Board()

# ######################### EVALUATOR TESTING ####################################

    # def test_evaluator_from_initial_board(self):
        # self.assertEqual(0.0, evlt.evaluator(self.board))

    # def test_white_checkmate_evaluation(self):
        # self.board.push_usi('7g7f')
        # self.board.push_usi('3c3d')
        # self.board.push_usi('8h2b+')
        # self.board.push_usi('4a5b')
        # self.board.push_usi('B*4b')
        # self.board.push_usi('5a4a')
        # self.board.push_usi('2b3a')
        # self.assertEqual(float('inf'), evlt.evaluator(self.board))

# ######################### SUBROUTINE TESTING ###################################

    # def test_count_material_extra_black_pieces(self):
        # for piece_type in ps.PIECE_TYPES_WITHOUT_KING:
            # self.board.add_piece_into_hand(piece_type, ps.BLACK)
            # self.assertEqual(mc.IN_HAND_VALUES.get(piece_type), \
                             # evlt.count_material(self.board))
            # self.board.reset()

    # def test_count_material_two_extra_black_pawns(self):
        # self.board.add_piece_into_hand(ps.PAWN, ps.BLACK)
        # self.board.add_piece_into_hand(ps.PAWN, ps.BLACK)
        # self.assertEqual(2 * mc.IN_HAND_VALUES.get(ps.PAWN), \
                         # evlt.count_material(self.board))
    
    # def test_count_mobility_from_initial_board(self):
        # self.assertEqual(0.0, evlt.count_mobility(self.board))

    # def test_count_mobility_with_extra_black_pawn(self):
        # self.board.add_piece_into_hand(ps.LANCE, ps.BLACK)

        # black_move_count = 0.0
        # white_move_count = 0.0
        # for _ in self.board.generate_legal_moves():
            # black_move_count += 1.0
        # self.board.turn = not self.board.turn
        # for _ in self.board.generate_legal_moves():
            # white_move_count += 1.0
        # self.board.turn = not self.board.turn

        # total = black_move_count + white_move_count
        # difference = black_move_count - white_move_count
        # ratio = difference / total

        # expected = evlt.mobility_weight * ratio
        # self.assertEqual(round(expected,evlt.sig_figs), \
                         # evlt.count_mobility(self.board)) 

class TestAgentAbility(unittest.TestCase):
    def setUp(self):
        self.board = ps.Board()

    def test_random_versus_random(self):
        agent1 = a.Agent(self.board.generate_legal_moves)
        agent2 = a.Agent(self.board.generate_legal_moves)
        gm.play_game(self.board, agent1, agent2)

    # def test_random_versus_ab_standard(self):
        # agent1 = a.Agent(self.board.generate_legal_moves)
        # eval_flags = [1,1,1,1]
        # agent2 = a.AlphaBetaAgent(gens.generate_qualifying_moves, 3, eval_flags)
        # gm.play_game(self.board, agent1, agent2)

    # def test_random_versus_ab_no_king_safety(self):
        # agent1 = a.Agent(self.board.generate_legal_moves)
        # eval_flags = [1,1,1,0]
        # agent2 = a.AlphaBetaAgent(gens.generate_qualifying_moves, 3, eval_flags)
        # gm.play_game(self.board, agent1, agent2)











