from .rules_loader import RulesLoader
from .semantic_router import SemanticRouter
from .density_router import DensityRouter

class Router:
    """
    Final routing logic combining:
    - Hard-coded rules (YAML)
    - Semantic similarity
    - Density heuristic
    """

    def __init__(self):
        self.rules = RulesLoader().get_rules()
        self.semantic = SemanticRouter()
        self.density = DensityRouter()

    def route(self, chunk):
        text = chunk["text"]

        # 1. RULE-BASED (highest priority)
        for keyword, category in self.rules.get("keyword_rules", {}).items():
            if keyword.lower() in text.lower():
                return category

        # 2. STRUCTURAL RULES
        if chunk.get("type") == "table_row":
            return "evidence"

        # 3. DENSITY-BASED (quick heuristic)
        density_category = self.density.route(chunk)

        # 4. SEMANTIC ROUTER (deep analysis)
        semantic_category = self.semantic.best_category(text)

        # Final Hybrid Decision
        if semantic_category == density_category:
            return semantic_category

        # If conflicting → prefer semantic for long text, density for short
        if len(text.split()) > 30:
            return semantic_category
        return density_category
