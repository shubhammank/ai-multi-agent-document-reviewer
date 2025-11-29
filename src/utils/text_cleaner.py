import re

class TextCleaner:
    """
    Cleans text for LLM/RAG usage.
    - Removes weird whitespace
    - Converts unicode spaces
    - Standardizes newlines
    """

    @staticmethod
    def clean(text: str):
        if not text:
            return ""

        text = text.replace("\u00A0", " ")     # non-breaking space
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        return text
