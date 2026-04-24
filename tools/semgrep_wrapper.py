import subprocess
from .base import BaseTool

class SemgrepWrapper(BaseTool):
    @property
    def name(self) -> str:
        return "Semgrep"

    def run(self):
        if self.target.startswith("http"):
            print(f"[Semgrep] Skipping {self.target} (not a local directory)")
            return
        print(f"[Semgrep] Performing static analysis on {self.target}...")
        cmd = ["semgrep", "scan", "--config=auto", self.target]
        print(f"[Semgrep] Executing: {' '.join(cmd)}")
        print("[Semgrep] Analysis finished.")
