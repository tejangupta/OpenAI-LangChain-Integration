import unittest
from unittest.mock import patch
from src.langchain_util.langchain_helpers import LangChainHelpers


class TestLangChainHelpers(unittest.TestCase):
    @patch('src.langchain_util.langchain_helpers.LangchainOpenAI')
    def test_query_llm(self, mock_llm):
        # Mock the Langchain LLM's invoke method
        mock_llm.return_value.invoke.return_value = 'mocked llm response'

        langchain_helper = LangChainHelpers()
        response = langchain_helper.query_llm("Test prompt")

        # Check if the response is as expected
        self.assertEqual(response, 'mocked llm response')

        # Check if the invoke method was called with correct parameters
        mock_llm.return_value.invoke.assert_called_with("Test prompt")

    @patch('src.langchain_util.langchain_helpers.ChatOpenAI')
    def test_query_chat_model(self, mock_chat_model):
        # Mock the Langchain ChatModel's invoke method
        mock_chat_model.return_value.invoke.return_value = 'mocked chat model response'

        langchain_helper = LangChainHelpers()
        response = langchain_helper.query_chat_model(["Test message"])

        # Check if the response is as expected
        self.assertEqual(response, 'mocked chat model response')

        # Check if the invoke method was called with correct parameters
        mock_chat_model.return_value.invoke.assert_called_with(["Test message"])


if __name__ == '__main__':
    unittest.main()
