import unittest
from src.openai_integration.model_utils import ModelUtils


class TestModelUtils(unittest.TestCase):
    def test_preprocess_input(self):
        # Test trimming and length limiting
        input_text = "   This is a test text   "
        expected_output = "This is a test text"
        self.assertEqual(ModelUtils.preprocess_input(input_text), expected_output)

    def test_postprocess_output(self):
        # Test removing extra spaces
        output_text = "This  is   a   test    text"
        expected_output = "This is a test text"
        self.assertEqual(ModelUtils.postprocess_output(output_text), expected_output)

    def test_handle_model_errors(self):
        # Test error handling
        response_with_error = {"error": {"message": "Test error"}}
        with self.assertRaises(Exception) as context:
            ModelUtils.handle_model_errors(response_with_error)

        self.assertTrue("Test error" in str(context.exception))

    def test_extract_relevant_information(self):
        # Test extracting relevant information
        response = {"choices": [{"text": "Extracted text"}]}
        self.assertEqual(ModelUtils.extract_relevant_information(response), "Extracted text")

        # Test with empty response
        empty_response = {}
        self.assertEqual(ModelUtils.extract_relevant_information(empty_response), "")


if __name__ == '__main__':
    unittest.main()
