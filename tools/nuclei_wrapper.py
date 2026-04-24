import subprocess
from .base import BaseTool

class NucleiWrapper(BaseTool):
    @property
    def name(self) -> str:
        return "Nuclei"

    def run(self):
        print(f"[Nuclei] Scanning {self.target}...")
        flag = "-u" if self.target.startswith("http") else "-target"
        cmd = ["nuclei", flag, self.target]
        print(f"[Nuclei] Executing: {' '.join(cmd)}")
        print("[Nuclei] Simulated scan complete.")
