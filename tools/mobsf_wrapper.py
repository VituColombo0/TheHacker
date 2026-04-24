import subprocess
import os
from .base import BaseTool

class MobSFWrapper(BaseTool):
    @property
    def name(self) -> str:
        return "MobSF"

    def run(self):
        exts = [".apk", ".ipa", ".app", ".zip"]
        if not any(self.target.lower().endswith(ext) for ext in exts):
            print(f"[MobSF] Skipping {self.target} (not a mobile app file)")
            return

        print(f"[MobSF] Analyzing mobile app: {self.target}...")
        server = os.getenv("MOBSF_SERVER", "http://localhost:8000")
        api_key = os.getenv("MOBSF_API_KEY")
        if not api_key:
            print("[MobSF] Error: MOBSF_API_KEY not set.")
            return
        cmd = ["mobsf-cli", "--server", server, "--apikey", api_key, "scan", self.target]
        print(f"[MobSF] Executing: {' '.join(cmd)}")
        print("[MobSF] Simulated scan complete.")
