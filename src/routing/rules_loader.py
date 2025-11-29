import yaml

class RulesLoader:
    """
    Loads routing rules from YAML.
    """

    def __init__(self, path="config/routing_rules.yaml"):
        with open(path, "r") as f:
            self.rules = yaml.safe_load(f)

    def get_rules(self):
        return self.rules
