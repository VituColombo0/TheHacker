import subprocess
import os
from .base import BaseTool

class GitleaksWrapper(BaseTool):
    @property
    def name(self) -> str:
        return "Gitleaks"

    def run(self):
        if self.target.startswith("http"):
            print(f"[Gitleaks] Skipping {self.target} (not a local directory)")
            return

        print(f"[Gitleaks] Scanning {self.target} for secrets...")
        report_path = os.path.abspath(f"reports/gitleaks_report.json")
        cmd = ["gitleaks", "detect", "--source", self.target, "--report-format", "json", "--report-path", report_path]
        print(f"[Gitleaks] Executing: {' '.join(cmd)}")
        print("[Gitleaks] Simulated scan complete.")
