import unittest
from unittest.mock import patch
from interaction.db_interaction import database_manager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db = database_manager(':memory:')  # Use an in-memory database for testing

    @patch('interaction.db_interaction.database_manager')
    def test_insert_user(self, mock_db):
        mock_db.insert_user.return_value = None
        mock_db.get_users.return_value = [(1, 'test_user', 'password')]
        self.db.insert_user('test_user', 'password')
        users = self.db.get_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], 'test_user')
        self.assertEqual(users[0][2], 'password')

if __name__ == '__main__':
    unittest.main()