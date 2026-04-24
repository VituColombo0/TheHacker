import subprocess
import os
from .base import BaseTool

class StrixWrapper(BaseTool):
    @property
    def name(self) -> str:
        return "Strix"

    def run(self):
        print(f"[Strix] Scanning {self.target}...")
        if not os.getenv("LLM_API_KEY"):
            print("[Strix] Warning: LLM_API_KEY not set.")
        cmd = ["strix", "-n", "--target", self.target]
        print(f"[Strix] Executing: {' '.join(cmd)}")
        print("[Strix] Simulated scan complete.")
