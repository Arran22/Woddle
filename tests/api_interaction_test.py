from unittest.mock import patch, Mock
import unittest
from interaction.word_api_interaction import *

class TestWordApiController(unittest.TestCase):
    @patch('requests.get')
    def test_get_random_word(self, mock_get):
        # Arrange
        mock_response = Mock()
        expected_length = 5
        mock_response.json.return_value = {
            'word': len(expected_word),
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Act
        rand_word = word_api_manipulator.get_word()

        # Assert
        self.assertEqual(len(rand_word), expected_length)