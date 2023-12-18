from langchain.llms import OpenAI as LangchainOpenAI
from langchain.chat_models import ChatOpenAI
from src.common.logger import CustomLogger


class LangChainHelpers:
    def __init__(self):
        self.logger = CustomLogger(__name__).get_logger()
        self.llm = LangchainOpenAI()
        self.chat_model = ChatOpenAI()

    def query_llm(self, text):
        """
        Queries Langchain's LLM with a string and returns a string response.
        """
        try:
            return self.llm.invoke(text)
        except Exception as e:
            self.logger.error(f"Error querying Langchain LLM: {e}")
            raise

    def query_chat_model(self, messages):
        """
        Queries Langchain's ChatModel with a list of messages and returns a message response.
        """
        try:
            return self.chat_model.invoke(messages)
        except Exception as e:
            self.logger.error(f"Error querying Langchain ChatModel: {e}")
            raise
