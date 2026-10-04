import unittest
from unittest.mock import patch

import game


class GuessingGameTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["hello", "20", "7"])
    def test_get_guess_rejects_invalid_input(self, _mock_input):
        self.assertEqual(game.get_guess(1, 10), 7)

    @patch("builtins.input", side_effect=["9", "2"])
    def test_get_difficulty_rejects_invalid_choice(self, _mock_input):
        self.assertEqual(game.get_difficulty(), game.DIFFICULTIES["2"])

    @patch("builtins.input", side_effect=["1", "6"])
    @patch("game.random.randint", return_value=6)
    def test_player_can_win(self, _mock_random, _mock_input):
        self.assertTrue(game.play_round())


if __name__ == "__main__":
    unittest.main()
