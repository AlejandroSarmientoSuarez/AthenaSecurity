from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def analyze_alert(self, prompt: str) -> str:
        """Analyze a security alert."""
        raise NotImplementedError