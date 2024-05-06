import unittest
from unittest.mock import patch
from sign_up_sign_in import account_manipulation

class TestSignUpOrIn(unittest.TestCase):
    @patch('account_manipulation')
    def test_sign_up_or_in_sign_up(self, mock_handle_inputs):
        mock_handle_inputs.return_value = 'N'
        result = account_manipulation().sign_up_or_in()
        self.assertEqual(result, 'sign up')

    @patch('account_manipulation')
    def test_sign_up_or_in_sign_in(self, mock_handle_inputs):
        mock_handle_inputs.return_value = 'Y'
        result = account_manipulation().sign_up_or_in()
        self.assertEqual(result, 'sign in')