import typer
from rich import print
import subprocess
import time 
from pathlib import Path
from enum import Enum

from config import vault_path, open_cmd, kasten_list, load_config



app = typer.Typer()

config.load_config()

vault_path = config.vault_path  # Assuming it's defined in config
gen_vault_path = Path.home() / (vault_path if vault_path else "Documents/zettel")

Kasten = Enum("Kasten", {name: i + 1 for i, name in enumerate(config.kasten_list)})

gen_vault_path.mkdir(parents=True, exist_ok=True)

@app.command()
def new(
    name: str,
    tags: str,
    kasten: int = typer.Option(1, "--kasten", "-k", help="Zettelkasten category number"),
    wiki_links: str = typer.Option(None, "--wiki-links", "-w", help="Comma-separated wiki links"),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite existing file without prompt")
):
    path: Path = gen_vault_path / f"{name}.md"


    try:
        text_kasten = Kasten(kasten).name
    except ValueError:
        raise typer.BadParameter(f"Kasten number '{kasten}' is invalid. Choose one of: {[k.value for k in Kasten]}")

    if not path.exists():
        overwrite_note()

    elif force:
        overwrite_note()

    else:
        print("File with this name already exists. Would you like to edit it? [y/n]")
        choice = input()
        while choice.lower != "y" and choice.lower != "n":
            print("please chooe y [yes] or n [no]")
            choice = input()
        if choice.lower == "y":
            subprocess.run([config.open_cmd, str(path)])
        else:
            raise typer.Exit(code=0)



@app.command
def remove():
    
def overwrite_note():
    path.write_text(f"""\
---
tags: {tags}
kasten: {text_kasten}
wiki_links: {wiki_links}
---
""")
    subprocess.run([config.open_cmd, str(path)])

if __name__ == "__main__":
    app()