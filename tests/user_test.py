import unittest
from user import user

class TestUser(unittest.TestCase):

    def set_up(self):
        self.user = user("testuser", "password1", 1)

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), "testuser")

    def test_compare_password(self):
        self.assertTrue(self.user.compare_password("password1"))

if __name__ == '__main__':
    unittest.main()