from .strix_wrapper import StrixWrapper
from .nuclei_wrapper import NucleiWrapper
from .gitleaks_wrapper import GitleaksWrapper
from .shannon_wrapper import ShannonWrapper
from .mobsf_wrapper import MobSFWrapper
from .trufflehog_wrapper import TruffleHogWrapper
from .trivy_wrapper import TrivyWrapper
from .semgrep_wrapper import SemgrepWrapper

class ToolFactory:
    TOOLS = {
        "strix": StrixWrapper,
        "nuclei": NucleiWrapper,
        "gitleaks": GitleaksWrapper,
        "shannon": ShannonWrapper,
        "mobsf": MobSFWrapper,
        "trufflehog": TruffleHogWrapper,
        "trivy": TrivyWrapper,
        "semgrep": SemgrepWrapper
    }

    @staticmethod
    def get_tool(name, target):
        tool_class = ToolFactory.TOOLS.get(name.lower())
        if tool_class:
            return tool_class(target)
        return None

    @staticmethod
    def list_available_tools():
        return list(ToolFactory.TOOLS.keys())
