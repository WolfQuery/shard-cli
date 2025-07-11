# Shard CLI
[![Publish to AUR](https://github.com/WolfQuery/shard-cli/actions/workflows/aur-publish.yml/badge.svg?branch=main)](https://github.com/WolfQuery/shard-cli/actions/workflows/aur-publish.yml)
[![Pylint](https://github.com/WolfQuery/shard-cli/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/WolfQuery/shard-cli/actions/workflows/pylint.yml)

**A CLI note-taking tool inspired by Zettelkasten, designed for terminal users and Linux setups.**

---

## Features

* Create Markdown notes with automatic unique IDs based on customizable date/time formats
* Notes named by their titles (slugified) for easy navigation
* Assign notes to user-configurable "kasten" collections (e.g., inbox, literature notes, etc.)
* Add tags and backlinks (links to other notes by ID, tag, or title)
* Customizable config for:

  * Vault path (where notes are stored)
  * Date/time format for note IDs and timestamps
  * Kasten collections with numeric IDs and names
  * Preferred terminal text editor command to open notes (e.g., `vim`, `nano`, `tini`)
* Automatic creation of config file on first run, cross-platform (`~/.config/shard-cli/config.toml` on Unix, app data folder on Windows)
* Simple Git integration planned (e.g., `shard push` to commit & push changes)
* Designed for efficient Zettelkasten workflows but flexible for any note organization

---

## Installation

Install via PyPI:

```bash
pip install shard-cli
```

[NOT YET IMPLEMENTED] Or from AUR (Arch Linux User Repository):

```bash
yay -S shard-cli
```

---

## Usage

### Create a new note

```bash
shard new "My Note Title" -t biology,chemistry -k 1 -l tag1,1234,OtherNote
```

Options:

* `-t`, `--tags`: Comma-separated list of tags
* `-k`, `--kasten`: Numeric ID of the kasten collection
* `-l`, `--links`: Comma-separated list of linked note IDs, tags, or note titles

### Config file

The config file is automatically created on first run at:

* Unix: `~/.config/shard-cli/config.toml`
* Windows: `%APPDATA%\shard-cli\config.toml`

Example config snippet:

```toml
vault_path = "~/zettelkasten"
editor_cmd = "vim"
date_format = "%Y%m%d%H%M%S"

[kasten]
1 = "Inbox"
2 = "Literature Notes"
3 = "Permanent Notes"
```

---

## Planned Features

* Git integration commands (`shard push` etc.) for easy version control and backup
* Enhanced backlinks visualization and navigation
* Support for additional note formats and metadata
* More powerful tagging and filtering capabilities

---

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or pull request.

---

## License

[CC BY-NC-SA 4.0](LICENSE)
