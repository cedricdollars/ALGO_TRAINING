import unittest
import solution


class testSolution(unittest.TestCase):

    def test_changeName(self):
        self.assertEqual(solution.changeUsername("face"), "YES")
        self.assertEqual(solution.changeUsername("foo",), "NO")
        self.assertEqual(solution.changeUsername(""), None)


if __name__ == "__main__":
    unittest.main()
