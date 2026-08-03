from .providers.base import LLMProvider


class AIService:

    def __init__(self, provider: LLMProvider):

        self.provider = provider

    def analyze(self, prompt: str):

        return self.provider.analyze_alert(prompt)