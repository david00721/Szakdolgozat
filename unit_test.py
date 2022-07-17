import unittest
import main_file

class TestUnittestFramework(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main_file.main(), "Basic main file to test workflow.")


if __name__ == '__main__':
    unittest.main()