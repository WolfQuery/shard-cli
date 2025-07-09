# config.py
import toml            # pip install toml
from pathlib import Path

# 1. Where our config lives
CONFIG_DIR  = Path.home() / ".config" / "shard-cli"
CONFIG_FILE = CONFIG_DIR / "config.toml"

# 2. Default settings
DEFAULTS = {
    "vault_path": str(Path.home() / "Documents" / "zettel"),
    "open_cmd":   "nano",
    "kasten_list": ["INBOX", "REFERENCE", "PERMANENT"],
}

def load_config() -> dict:
    """
    Ensure config file exists, then load and return it.
    """
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_FILE.exists():
        # write defaults
        with open(CONFIG_FILE, "w") as f:
            toml.dump(DEFAULTS, f)

    # read whatever’s in there
    return toml.load(CONFIG_FILE)

# 3. Load and expose
_conf = load_config()

vault_path   = Path(_conf["vault_path"])
open_cmd     = _conf["open_cmd"]
kasten_list  = _conf["kasten_list"]
