import unittest
from unittest.mock import patch

import main_menu
from main_menu import menu


class test_menu(unittest.TestCase):
    
    def test_allowed_guesses(self):
        self.assertEqual(self.main_menu.ALLOWED_GUESSES, 5)

    def test_initial_sign_in_status(self):
        self.assertEqual(self.main_menu.signed_in, False)

