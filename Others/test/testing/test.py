import unittest
# import the file we wanna test
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        # do_stuff is d function in main that we wanna test
        result = main.do_stuff(num)
        # then we assert that the answer is equal to 20
        # in here i can test my code
        self.assertEqual(result,20)

    def test_stuff(self):
        test_param = 'word word'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)

    def test_stuff2(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')


unittest.main()