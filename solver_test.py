from solver import Square, Nine, Puzzle
import unittest

class TestSquare(unittest.TestCase):

    def setUp(self):
        self._base_square = Square()

    def test_square_has_9_possibilities(self):
        expected_possibilities = 9
        actual_possibilities = len(self._base_square.possibilities)
        
        self.assertEqual(expected_possibilities, actual_possibilities)

class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self._empty_puzzle = Puzzle()
        
    def test_puzzle_has_nine_rows(self):
        expected = 9
        actual = len(self._empty_puzzle.rows)

        self.assertEqual(expected, actual)
    
    def test_puzzle_has_nine_columns(self):
        expected = 9
        actual = len(self._empty_puzzle.columns)

        self.assertEqual(expected, actual)

    def test_puzzle_has_nine_grids(self):
        expected = 9
        actual = len(self._empty_puzzle.grids)

        self.assertEqual(expected, actual)

class TestNine(unittest.TestCase):
    def setUp(self):
        self._nine = Nine([Square() for i in range(0, 9)])
    
    def test_nine_has_9_items(self):
        expected = 9
        actual = len(self._nine._squares)

        self.assertEqual(expected, actual)

    def test_nine_is_missing_everything(self):
        expected = set((1, 2, 3, 4, 5, 6, 7, 8, 9))
        actual = self._nine.missing
        
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()