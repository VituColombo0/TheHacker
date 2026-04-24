import argparse
import yaml
import os
import sys
from typing import List
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.prompt import Prompt

from tools.factory import ToolFactory

console = Console()

def detect_target_category(target: str) -> str:
    if target.startswith("http"):
        return "web"
    
    exts = [".apk", ".ipa", ".app", ".zip"]
    if any(target.lower().endswith(ext) for ext in exts):
        return "mobile"
    
    if os.path.isdir(target):
        return "local"
    
    return "unknown"

def main():
    parser = argparse.ArgumentParser(description="TheHacker - Advanced Security Orchestration")
    parser.add_argument("--target", help="Target URL, Directory, or Mobile App file")
    parser.add_argument("--config", default="config/default.yaml", help="Path to config file")
    parser.add_argument("--interactive", action="store_true", help="Choose tools interactively")
    args = parser.parse_args()

    console.print(Panel.fit(
        "[bold green]TheHacker[/bold green] - Advanced Security Orchestration",
        subtitle="v0.2.0 - All-in-One Security",
        border_style="magenta"
    ))

    target = args.target
    if not target:
        target = Prompt.ask("[bold yellow]Enter target (URL, Dir, or App file)[/bold yellow]")

    category = detect_target_category(target)
    console.print(f"[bold blue]Target:[/bold blue] {target} ([cyan]{category}[/cyan])")

    if category == "unknown":
        console.print("[bold red]Error: Target type not recognized.[/bold red]")
        sys.exit(1)

    # Load configuration
    available_tools = ToolFactory.list_available_tools()
    enabled_tools = []

    if args.interactive:
        console.print("\n[bold yellow]Select tools to run (comma separated):[/bold yellow]")
        for i, t in enumerate(available_tools):
            console.print(f"{i+1}. {t}")
        selection = Prompt.ask("Selection", default="all")
        if selection == "all":
            enabled_tools = available_tools
        else:
            indices = [int(x.strip()) - 1 for x in selection.split(",")]
            enabled_tools = [available_tools[i] for i in indices if 0 <= i < len(available_tools)]
    else:
        if os.path.exists(args.config):
            with open(args.config, 'r') as f:
                config = yaml.safe_load(f)
                enabled_tools = config.get("tools", available_tools)
        else:
            enabled_tools = available_tools

    # Instantiate tools
    tools = []
    for tool_name in enabled_tools:
        tool = ToolFactory.get_tool(tool_name, target)
        if tool:
            tools.append(tool)

    # Execution Table
    table = Table(title="Security Scan Workflow")
    table.add_column("Order", justify="center", style="cyan")
    table.add_column("Tool", style="green")
    table.add_column("Status", style="yellow")

    for i, tool in enumerate(tools):
        table.add_row(str(i+1), tool.name, "Pending")
    
    console.print(table)
    console.print("\n")

    # Run tools sequentially
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        for tool in tools:
            task_id = progress.add_task(description=f"Running {tool.name}...", total=None)
            try:
                tool.run()
                console.print(f"[bold green]✓[/bold green] {tool.name} analysis finished.")
                progress.remove_task(task_id)
            except Exception as e:
                console.print(f"[bold red]✗[/bold red] {tool.name} failed: {e}")
                progress.remove_task(task_id)

    console.print("\n[bold green]Orchestration complete.[/bold green] Check the [cyan]reports/[/cyan] directory for details.")

if __name__ == "__main__":
    main()
