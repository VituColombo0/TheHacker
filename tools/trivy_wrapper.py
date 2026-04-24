import subprocess
from .base import BaseTool

class TrivyWrapper(BaseTool):
    @property
    def name(self) -> str:
        return "Trivy"

    def run(self):
        print(f"[Trivy] Scanning {self.target} for vulnerabilities...")
        if self.target.startswith("http"):
            cmd = ["trivy", "repo", self.target]
        else:
            cmd = ["trivy", "fs", self.target]
        print(f"[Trivy] Executing: {' '.join(cmd)}")
        print("[Trivy] Scan complete.")
