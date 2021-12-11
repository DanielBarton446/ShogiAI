import unittest
import king_safety as ks
import python_shogi.shogi as ps


class TestKingSafety(unittest.TestCase):
    def setUp(self):
        self.board = ps.Board()

    def test_center(self):
        self.board = ps.Board("9/9/9/9/4K4/9/9/9/9 b - 1")
        expected_square_indexes = [30,31,32,
                                   39,   41,
                                   48,49,50]
                                  
        adjacent_tiles = ks.find_adjacent(self.board.king_squares[ps.BLACK], 1)
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









