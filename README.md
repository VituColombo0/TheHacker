# TheHacker: Security Scan Orchestration Engine

A modular command-line orchestration engine for automated security testing across web applications, mobile packages, and local source repositories.

[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CLI: Rich](https://img.shields.io/badge/Interface-Rich%20CLI-blueviolet.svg)](https://github.com/Textualize/rich)
[![Docker: Required](https://img.shields.io/badge/Containers-Docker%20Sandboxed-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

**TheHacker** unifies heterogeneous security scanners into a single execution pipeline. It automatically identifies the target type (URL, mobile binary, or source directory), resolves applicable analyzers through a declarative factory pattern, and runs the assessment sequentially with real-time status tracking and report aggregation.

```
                     Target Input (URL, Directory, APK/IPA)
                                       │
                                       ▼
                            [ Target Detection ]
                         Auto-identifies target type
                                       │
                                       ▼
                       [ Configuration & Factory ]
                      Loads config/default.yaml or CLI
                                       │
         ┌─────────────────────────────┼─────────────────────────────┐
         ▼                             ▼                             ▼
    [ Web / API ]                 [ Mobile ]                  [ SAST / Secrets ]
   Nuclei, Strix,             MobSF (Docker)               Semgrep, Gitleaks,
   Shannon                                                 TruffleHog, Trivy
         │                             │                             │
         └─────────────────────────────┼─────────────────────────────┘
                                       │
                                       ▼
                             [ Rich Execution Engine ]
                                Progress & Logging
                                       │
                                       ▼
                               [ reports/ Directory ]
```

---

## Tool Matrix

| Domain | Scanner | Purpose | Runtime |
| :--- | :--- | :--- | :--- |
| **Web / API** | **Nuclei** | Template-driven protocol and vulnerability scanning | Native binary / Go |
| **Web / API** | **Strix** | Autonomous agent-assisted dynamic penetration testing | Docker container |
| **Web / API** | **Shannon** | White-box source security analysis and verification | Docker container |
| **Mobile** | **MobSF** | Static (SAST) and dynamic analysis for Android (.apk) & iOS (.ipa) | Docker container |
| **Secrets** | **Gitleaks** | Pattern matching for hardcoded secrets in git history | Native binary / Go |
| **Secrets** | **TruffleHog** | High-entropy secret and credential scanning with API verification | Native binary / Go |
| **Code (SAST)**| **Semgrep** | Fast semantic static analysis for vulnerability patterns | Python / Native |
| **Containers** | **Trivy** | Vulnerability scanning for dependencies, SBOMs, and misconfigurations | Native binary / Go |

---

## Prerequisites

- **Python 3.10** or higher
- **Docker Engine** running locally (required for sandboxed scanners like MobSF and Strix)
- **Git**

---

## Installation

```bash
# Clone the repository
git clone https://github.com/VituColombo0/TheHacker.git
cd TheHacker

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Command-Line Arguments

```text
usage: main.py [-h] [--target TARGET] [--config CONFIG] [--interactive]

TheHacker - Advanced Security Orchestration

options:
  -h, --help       show this help message and exit
  --target TARGET  Target URL, Directory, or Mobile App file
  --config CONFIG  Path to YAML config file (default: config/default.yaml)
  --interactive    Interactively select which tools to execute
```

### Examples

**Analyze a Web Application:**
```bash
python main.py --target https://example.com
```

**Audit a Local Repository:**
```bash
python main.py --target /path/to/source-code
```

**Scan an Android Package:**
```bash
python main.py --target ./dist/app.apk
```

**Interactive Tool Selection:**
```bash
python main.py --interactive
```

---

## Configuration

Custom tool chains are configured in YAML format. Default behavior can be overridden via `config/default.yaml` or a custom configuration file:

```yaml
# config/custom.yaml
tools:
  - nuclei
  - gitleaks
  - semgrep
  - trufflehog
  # Exclude heavy runners when running in lightweight CI:
  # - mobsf
  # - strix
```

Pass the custom file using the `--config` flag:
```bash
python main.py --target ./src --config config/custom.yaml
```

---

## Architecture & Adding New Scanners

The orchestration engine uses a pluggable `ToolFactory` pattern. To add a new scanner:

1. Create a wrapper file in `tools/` (e.g., `tools/my_scanner.py`):
   ```python
   from tools.base import BaseTool

   class MyScanner(BaseTool):
       name = "my_scanner"

       def run(self):
           # Implement scan invocation and report generation
           pass
   ```
2. Inherit from `BaseTool` and implement required execution methods.
3. Register the class in `tools/factory.py`.
4. Add the tool identifier to `config/default.yaml`.

---

## Project Structure

```text
TheHacker/
├── config/
│   └── default.yaml         # Toolchain configuration
├── tools/
│   ├── base.py              # BaseTool abstract interface
│   ├── factory.py           # ToolFactory dynamic loader
│   ├── nuclei.py            # Nuclei wrapper
│   ├── mobsf.py             # MobSF container wrapper
│   └── ...                  # Additional scanner modules
├── reports/                 # Output artifacts and scanner logs
├── main.py                  # CLI entrypoint and argument parser
├── requirements.txt         # Python package dependencies
└── README.md                # Documentation
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
