#############
# config.py #
#############

import toml
from pathlib import Path

CONFIG_DIR  = Path.home() / ".config" / "shard-cli"
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULTS = {
    "vault_path": str(Path.home() / "Documents" / "zettel"),
    "open_cmd":   "nano",
    "kasten_list": ["INBOX", "REFERENCE", "PERMANENT"],
}

def load_config() -> dict:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w") as f:
            toml.dump(DEFAULTS, f)
    return toml.load(CONFIG_FILE)

_conf       = load_config()
vault_path  = Path(_conf["vault_path"])
open_cmd    = _conf["open_cmd"]
kasten_list = _conf["kasten_list"]
