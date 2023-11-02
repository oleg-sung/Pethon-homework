import unittest
from main import add_folder, delete_folder


class TestYaApi(unittest.TestCase):

    def test_success_create_folder(self):
        self.assertEqual(add_folder('test'), 201)

    @unittest.expectedFailure
    def test_passed_create_folder(self):
        self.assertEqual(add_folder('test_passed'), 409)

    def tearDown(self):
        delete_folder('test')


if __name__ == '__main__':
    unittest.main()
