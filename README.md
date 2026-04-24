# 🛡️ TheHacker - Advanced Security Orchestration Engine

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Security](https://img.shields.io/badge/security-orchestration-blueviolet.svg)

**TheHacker** is a powerful, all-in-one security orchestration platform designed to automate and simplify the process of vulnerability assessment across multiple domains. Whether you are testing a **Web Application**, a **Mobile App**, or a **Local Codebase**, TheHacker combines the world's best security tools into a single, unified workflow.

---

## ✨ Key Features

- **🚀 Multi-Target Support**: Automatically detects and handles Web URLs, Local Directories, and Mobile Files (.apk, .ipa).
- **🤖 AI-Powered Analysis**: Integrated with state-of-the-art AI pen-testing tools like Strix and Shannon.
- **🛠️ Extensible Tool Factory**: Modular architecture allowing for easy integration of any CLI-based security tool.
- **🎨 Premium CLI Interface**: Beautifully formatted output with progress bars, tables, and rich logging.
- **⚙️ Flexible Configuration**: Highly customizable toolchain through YAML configurations.

---

## 🛠️ Integrated Tools

| Category | Tool | Description |
| :--- | :--- | :--- |
| **Web / API** | **Strix** | AI-driven autonomous penetration testing and PoC validation. |
| **Web / API** | **Shannon** | Real-time AI white-box pentesting and source code analysis. |
| **Web / API** | **Nuclei** | Fast, template-based vulnerability scanning from the community. |
| **Mobile** | **MobSF** | Static and dynamic analysis for Android & iOS applications. |
| **Secrets** | **Gitleaks** | Find passwords, API keys, and tokens in your local code. |
| **Secrets** | **TruffleHog** | Scan for verified credentials leaked in Git history or filesystems. |
| **Code (SAST)** | **Semgrep** | Static analysis to find complex logic bugs and security flaws. |
| **Containers**| **Trivy** | Vulnerability scanner for OS packages, dependencies, and misconfigs. |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **Docker** (Required for Strix and MobSF sandboxes)
- **Git**

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VituColombo0/TheHacker.git
   cd TheHacker
   ```

2. Set up the virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

### Basic Usage

**Scan a Web Application:**
```bash
python main.py --target https://your-app.com
```

**Scan a Local Directory:**
```bash
python main.py --target ./path/to/source
```

**Scan a Mobile App:**
```bash
python main.py --target ./app.apk
```

**Interactive Mode:**
```bash
python main.py --interactive
```

---

## ⚙️ Configuration

You can customize the toolchain in `config/default.yaml`. Enable or disable tools based on your needs:

```yaml
tools:
  - strix
  - nuclei
  - trufflehog
  # - mobsf (disabled for local code scan)
```

---

## 🤝 Contributing

We welcome contributions! If you have a tool you'd like to integrate:
1. Create a new wrapper in `tools/`.
2. Inherit from `BaseTool`.
3. Register it in `ToolFactory`.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by VituColombo0
</p>
