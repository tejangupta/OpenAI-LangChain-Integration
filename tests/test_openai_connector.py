import unittest
from unittest.mock import patch, MagicMock
from src.openai_integration.openai_connector import OpenAIConnector


class TestOpenAIConnector(unittest.TestCase):
    @patch('src.openai_integration.openai_connector.openai.Completion.create')
    def test_query_model(self, mock_create):
        # Mocking the OpenAI API response
        mock_create.return_value = MagicMock(choices=[MagicMock(text='mocked response')])

        connector = OpenAIConnector()
        response = connector.query_model("Test prompt")

        # Check if the response is as expected
        self.assertEqual(response, 'mocked response')

        # Check if the API was called with correct parameters
        mock_create.assert_called_with(engine="text-davinci-003", prompt="Test prompt")


if __name__ == '__main__':
    unittest.main()
