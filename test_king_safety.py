import unittest
import king_safety as ks
import python_shogi.shogi as ps


class TestAdjacentSquares(unittest.TestCase):
    def setUp(self):
        self.board = ps.Board()

    def test_center(self):
        self.board = ps.Board("9/9/9/9/4K4/9/9/9/9 b - 1")
        expected_square_indexes = [30,31,32,
                                   39,   41,
                                   48,49,50]
                                  
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_center_radius_2(self):
        self.board = ps.Board("9/9/9/9/4K4/9/9/9/9 b - 1")
        expected_square_indexes = [20,21,22,23,24,
                                   29,30,31,32,33,
                                   38,39,   41,42,
                                   47,48,49,50,51,
                                   56,57,58,59,60]
                                  
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 2)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_left_side_center(self):
        self.board = ps.Board("9/9/9/9/K8/9/9/9/9 b - 1")
        expected_square_indexes = [27, 28,
                                       37,
                                   45, 46]
                                  
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_right_side_center(self):
        self.board = ps.Board("9/9/9/9/8K/9/9/9/9 b - 1")
        expected_square_indexes = [34, 35,
                                   43, 
                                   52, 53]
                                  
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_top_side_center(self):
        self.board = ps.Board("4K4/9/9/9/9/9/9/9/9 b - 1")
        expected_square_indexes = [ 3,    5,
                                   12,13,14]
                                  
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_bottom_side_center(self):
        self.board = ps.Board("9/9/9/9/9/9/9/9/4K4 b - 1")
        expected_square_indexes = [66,67,68,
                                   75,   77]
                                 
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_bottom_side_center_radius_2(self):
        self.board = ps.Board("9/9/9/9/9/9/9/9/4K4 b - 1")
        expected_square_indexes = [56,57,58,59,60,
                                   65,66,67,68,69,
                                   74,75,   77,78]
                                 
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 2)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_bottom_side_center_radius_4(self):
        self.board = ps.Board("9/9/9/9/9/9/9/9/4K4 b - 1")
        expected_square_indexes = [36,37,38,39,40,41,42,43,44,
                                   45,46,47,48,49,50,51,52,53,
                                   54,55,56,57,58,59,60,61,62,
                                   63,64,65,66,67,68,69,70,71,
                                   72,73,74,75,77,78,79,80]
                                 
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 4)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_bottom_side_center_absurd_radius(self):
        self.board = ps.Board("9/9/9/9/9/9/9/9/4K4 b - 1")
        expected_square_indexes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
                                   26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
                                   51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,77,
                                   78,79,80]
                                 
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 9)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)




    def test_bottom_left_corner(self):
        self.board = ps.Board("9/9/9/9/9/9/9/9/K8 b - 1")
        expected_square_indexes = [ 63, 64,
                                        73,]
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_bottom_right_corner(self):
        self.board = ps.Board("9/9/9/9/9/9/9/9/8K b - 1")
        expected_square_indexes = [ 70, 71,
                                    79,   ]
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)

    def test_top_right_corner(self):
        self.board = ps.Board("8K/9/9/9/9/9/9/9/9 b - 1")
        expected_square_indexes = [ 7, 
                                    16, 17]
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)


    
    def test_top_left_corner(self):
        self.board = ps.Board("K8/9/9/9/9/9/9/9/9 b - 1")
        expected_square_indexes = [     1,
                                    9, 10]
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
        self.assertCountEqual(expected_square_indexes, adjacent_tiles)




class TestKingSafety(unittest.TestCase):
    def setUp(self):
        self.board = ps.Board()

    @unittest.skip("no reason")
    def test_my_king_safety(self):
        ks.king_safety(self.board, 1)
        print(ks.king_safety(self.board, 2))

    @unittest.skip("no reason")
    def test_my_king_safety_from_attacks(self):
        self.board = ps.Board("9/9/9/4k4/9/9/4S1N2/9/5L3 b - 1")
        print(ks.king_safety(self.board, 2))

    @unittest.skip("no reason")
    def test_my_king_safety_with_alot(self):
        self.board = ps.Board("9/9/9/4k4/9/4S4/6N2/3R5/5L3 b - 1")
        print(ks.king_safety(self.board, 2))

    @unittest.skip("no reason")
    def test_my_king_safety_attacks_king(self):
        self.board = ps.Board("9/9/9/4k4/9/5N3/9/9/9 b - 1")
        print(ks.king_safety(self.board, 2))
