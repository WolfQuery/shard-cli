import typer
from rich import print
import subprocess
from pathlib import Path
from enum import Enum
from datetime import datetime

import config  # 👍 stick with full import for clarity

app = typer.Typer()

# Initialize vault directory
vault_path = config.vault_path
if not vault_path.is_absolute():
    vault_path = Path.home() / vault_path
vault_path.mkdir(parents=True, exist_ok=True)

# Build Kasten enum from config.kasten_list
Kasten = Enum("Kasten", {name: i + 1 for i, name in enumerate(config.kasten_list)})

def overwrite_note(
    path: Path,
    tags: str,
    text_kasten: str,
    wiki_links: str
):
    zettel_id = datetime.now().strftime("%Y%m%d%H%M%S")
    path.write_text(f"""\
---
tags: {tags}
kasten: {text_kasten}
wiki_links: {wiki_links}
id: {zettel_id}
---
""")
    subprocess.run([config.open_cmd, str(path)])


@app.command()
def new(
    name: str = typer.Argument(..., help="Filename without .md"),
    tags: str = typer.Option(..., "--tags", "-t", help="Comma-separated tags"),
    kasten: int = typer.Option(1, "--kasten", "-k", help="Zettelkasten category number"),
    wiki_links: str = typer.Option(None, "--wiki-links", "-w", help="Comma-separated wiki links"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite without confirmation")
):
    path = vault_path / f"{name}-{kasten}.md"

    try:
        text_kasten = Kasten(kasten).name
    except ValueError:
        valid = ", ".join(str(k.value) for k in Kasten)
        raise typer.BadParameter(f"Invalid kasten '{kasten}'. Valid values: {valid}")

    if not path.exists() or force:
        overwrite_note(path, tags, text_kasten, wiki_links)
    else:
        print(f"[yellow]'{path.name}' already exists.[/yellow]")
        if typer.confirm("Edit anyway?", default=False):
            subprocess.run([config.open_cmd, str(path)])
        else:
            raise typer.Exit()


@app.command()
def open(
    name: str = typer.Argument(..., help="Filename without .md"),
    kasten: int = typer.Option(..., "--kasten", "-k", help="Kasten number (required)")
):
    path = vault_path / f"{name}-{kasten}.md"
    if path.exists():
        subprocess.run([config.open_cmd, str(path)])
    else:
        typer.secho(f"File not found: {path.name}", fg="red")
        raise typer.Exit(code=1)


@app.command()
def remove(
    name: str = typer.Argument(..., help="Filename without .md"),
    kasten: int = typer.Option(..., "--kasten", "-k", help="Kasten number (required)"),
    force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation")
):
    path = vault_path / f"{name}-{kasten}.md"
    if not path.exists():
        typer.secho(f"No such file: {path.name}", fg="red")
        raise typer.Exit(code=1)

    if force or typer.confirm(f"Delete '{path.name}'?"):
        path.unlink()
        typer.secho(f"Deleted: {path.name}", fg="green")
    else:
        typer.secho("Deletion canceled", fg="yellow")
        raise typer.Exit()


if __name__ == "__main__":
    app()
