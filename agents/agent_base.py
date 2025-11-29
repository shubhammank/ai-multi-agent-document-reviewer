import yaml
import json
import time
from openai import OpenAI
import anthropic

class AgentBase:
    """
    Base class for all review agents.
    Unified LLM calling, prompt construction, structured output, retry logic.
    """

    def __init__(self, role, system_prompt, config_path="config/llm.yaml"):
        with open(config_path, "r") as f:
            self.cfg = yaml.safe_load(f)

        self.role = role
        self.system_prompt = system_prompt
        self.backend = self.cfg["llm_backend"]
        self.model = self.cfg["llm_model"]

        if self.backend == "openai":
            self.client = OpenAI(api_key=self.cfg["openai_api_key"])
        elif self.backend == "anthropic":
            self.client = anthropic.Client(api_key=self.cfg["anthropic_api_key"])

    def call_llm(self, text):
        """
        Calls the LLM with structured JSON output.
        """

        prompt = f"""
You are an AI document review agent specializing in the category: {self.role}.

SYSTEM RULES:
- ALWAYS return JSON.
- NEVER include commentary outside the JSON.
- Output must include: "comment", "severity", and "justification".
- Ensure the comment is specific to the given chunk.

CHUNK:
{text}
"""

        for attempt in range(3):
            try:
                if self.backend == "openai":
                    response = self.client.chat.completions.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": self.system_prompt},
                            {"role": "user", "content": prompt}
                        ],
                        response_format={"type": "json_object"}
                    )
                    return json.loads(response.choices[0].message.content)

                elif self.backend == "anthropic":
                    response = self.client.messages.create(
                        model=self.model,
                        max_tokens=500,
                        system=self.system_prompt,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    return json.loads(response.content[0].text)

            except Exception:
                time.sleep(1)

        return {
            "comment": "",
            "severity": "low",
            "justification": "Agent failed to generate output after retries."
        }

    def run(self, chunk):
        return self.call_llm(chunk["text"])
