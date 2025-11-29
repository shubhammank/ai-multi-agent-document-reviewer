import re

class DensityAnalyzer:
    """
    Semantic density = (#keywords + #numbers + proper nouns) / total_tokens
    """

    KEYWORDS = ["emission", "policy", "strategy", "risk", "baseline", "target"]

    @staticmethod
    def score(text):
        tokens = text.split()
        if len(tokens) == 0:
            return 0

        score = 0

        # Keyword hits
        for kw in DensityAnalyzer.KEYWORDS:
            if kw in text.lower():
                score += 1

        # Numbers (e.g., KPIs)
        score += len(re.findall(r"\d+", text))

        return score / len(tokens)

    @staticmethod
    def add_density_scores(items):
        for i in items:
            i["density"] = DensityAnalyzer.score(i["text"])
