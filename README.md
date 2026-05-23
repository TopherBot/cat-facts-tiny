# cat-facts-tiny

A **tiny** command‑line utility that prints a random cat fact.

## Why?
Because cat facts are fun, lightweight, and they make terminal sessions a little brighter.

## Installation
```bash
# Clone the repo (or just copy the file)
git clone https://github.com/yourusername/cat-facts-tiny.git
cd cat-facts-tiny

# (Optional) Create a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Install dependencies (none required for the core script)
```

## Usage
```bash
python3 cat_facts.py
```

You’ll see something like:
```
Did you know? A group of kittens is called a kindle.
```

## Extending
Add more facts to the `facts` list in `cat_facts.py` or replace it with an external JSON/CSV source.

## License
MIT – see LICENSE file.
