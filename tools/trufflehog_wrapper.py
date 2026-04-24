import subprocess
from .base import BaseTool

class TruffleHogWrapper(BaseTool):
    @property
    def name(self) -> str:
        return "TruffleHog"

    def run(self):
        print(f"[TruffleHog] Scanning {self.target} for leaked credentials...")
        if self.target.startswith("http"):
            cmd = ["trufflehog", "git", self.target]
        else:
            cmd = ["trufflehog", "filesystem", self.target]
        print(f"[TruffleHog] Executing: {' '.join(cmd)}")
        print("[TruffleHog] Scan complete.")
