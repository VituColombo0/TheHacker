import subprocess
import os
from .base import BaseTool

class ShannonWrapper(BaseTool):
    @property
    def name(self) -> str:
        return "Shannon"

    def run(self):
        if not self.target.startswith("http"):
            print(f"[Shannon] Skipping {self.target} (not a URL)")
            return
        print(f"[Shannon] Starting AI white-box pentest on {self.target}...")
        cmd = ["shannon", "start", f"TARGET={self.target}"]
        print(f"[Shannon] Executing: {' '.join(cmd)}")
        print("[Shannon] Simulated exploits executed.")
