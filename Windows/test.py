import unittest

from Options.module import Module


class PathTests(unittest.TestCase):
    def test_path(self):
        self.assertEqual(type(Module.get_default()), type(dict()))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(PathTests("test_path"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())