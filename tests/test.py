import unittest
import helper


class TestHelperFunctions(unittest.TestCase):
    def test_add(self):
        str = "Test Item"
        helper.add("Test Item")
        self.assertEqual(helper.todos[-1].title, str)

    def test_update(self):
        helper.todos.append(helper.todo("Sample Item"))
        helper.update(0)
        self.assertTrue(helper.todos[0].isCompleted)

    def test_bbb(self):
        helper.add("b")
        self.assertEqual(helper.todos[-1].title, "bbb")

    def test_Bbb(self):
        helper.add("B")
        self.assertEqual(helper.todos[-1].title, "Bbb")

    def test_Bbb_in_word(self):
        helper.add("Baden")
        self.assertEqual(helper.todos[-1].title, "Bbbaden")


if __name__ == "__main__":
    unittest.main()
