import openai
import os
from src.common.logger import CustomLogger


class OpenAIConnector:
    def __init__(self):
        self.logger = CustomLogger(__name__).get_logger()
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            self.logger.error("No OpenAI API key found in environment variables")
            raise ValueError("No OpenAI API key found in environment variables")
        openai.api_key = self.api_key

    def query_model(self, prompt, model="text-davinci-003", **kwargs):
        try:
            response = openai.Completion.create(engine=model, prompt=prompt, **kwargs)
            return response.choices[0].text.strip()
        except Exception as e:
            self.logger.error(f"Error querying model: {e}")
            raise
