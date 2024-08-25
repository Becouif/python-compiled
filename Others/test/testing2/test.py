import unittest
import index

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = index.run_guess(answer, guess)
        self.assertTrue(result)

    def test_wrong_input(self):
        answer = 5
        guess = 10
        result = index.run_guess(answer, guess)
        self.assertFalse(result)

    def test_wrong_input2(self):
        answer = 5
        guess = 'hello'
        result = index.run_guess(answer, guess)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()