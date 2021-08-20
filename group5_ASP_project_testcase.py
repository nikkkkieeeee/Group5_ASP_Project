import unittest
import group5_ASP_Project as prog

class MyTestCase(unittest.TestCase):
    def test_total(self):
        data = prog.top3
        result = prog.Test.sum(data)
        self.assertEqual(result, 60923003)

    def test_mean(self):
        data = prog.top3
        result = round(prog.Test.mean(data), 2)
        self.assertEqual(result, 20307667.67)


if _name_ == '_main_':
    unittest.main()