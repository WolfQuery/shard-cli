###############
# __main__.py #
###############

from shard_cli.config import load_config
from shard_cli import commands
import typer


# load the default config into the proper directory
# ~/.config/shard/ for unix users
#
config = load_config()
print(config["vault_path"])      # pathlib.Path with expanded home
print(config["editor_cmd"])      # e.g. "nano"
print(config["kasten"])          # dict of kasten ids and names
print(config["general"]["date_format"])

app = typer.Typer()
app.add_typer(commands.app, name="new")

if __name__ == "__main__":
    app()