from src.common.logger import CustomLogger


class ModelUtils:
    @staticmethod
    def preprocess_input(text):
        """
        Preprocesses input text before sending it to the model.
        Trims whitespace and limits length to a reasonable size.
        """
        return text.strip()[:1000]

    @staticmethod
    def postprocess_output(text):
        """
        Postprocesses the model's output. Removes extra spaces and corrects common formatting issues.
        """
        return ' '.join(text.split())

    @staticmethod
    def handle_model_errors(response):
        """
        Handle any errors in the model's response.
        """
        if 'error' in response:
            logger = CustomLogger(__name__).get_logger()
            logger.error(f"Model returned an error: {response['error']['message']}")
            raise Exception(f"Model Error: {response['error']['message']}")
        return response

    @staticmethod
    def extract_relevant_information(response):
        """
        Extracts and formats relevant information from the model's response.
        """
        return response.get('choices', [{}])[0].get('text', '').strip()
