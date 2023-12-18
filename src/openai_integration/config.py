class OpenAIConfig:
    # OpenAI API settings
    MODEL_NAME = "text-davinci-003"  # Replace with your preferred model
    MAX_TOKENS = 150  # Maximum number of tokens per request
    TEMPERATURE = 0.7  # Adjust to control the randomness of the output
    TOP_P = 1  # Nucleus sampling parameter
    FREQUENCY_PENALTY = 0  # Adjust to penalize new tokens based on frequency
    PRESENCE_PENALTY = 0  # Adjust to penalize new tokens based on presence
