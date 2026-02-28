# gkm_engine

> A production-ready Python engine package — minimal, clean, and installable directly from GitHub.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Version](https://img.shields.io/badge/version-0.1.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Installation

### From GitHub
```bash
pip install git+https://github.com/<username>/gkm_engine.git
```

### For local development
```bash
git clone git@github.com:<username>/gkm_engine.git
cd gkm_engine
pip install -e .
```

---

## Usage

### Python API
```python
from gkm_engine import run

run()
```

### CLI
```bash
gkm
```

### Expected output
```
╔══════════════════════════════════════╗
║          gkm_engine  v0.1.0          ║
╚══════════════════════════════════════╝
  Python   : 3.11.4
  Platform : Linux 5.15.0
  Time     : 2025-01-01 12:00:00 UTC

  Engine started successfully. ✓
```

---

## Project Structure

```
gkm_engine/
├── gkm_engine/
│   ├── __init__.py       # Public API surface
│   └── core.py           # Core logic + CLI entry point
├── tests/
│   ├── __init__.py
│   └── test_core.py      # Unit tests
├── .gitignore
├── pyproject.toml        # PEP 621 packaging config
└── README.md
```

---

## Push to GitHub (SSH)

```bash
git init
git add .
git commit -m "Initial release: gkm_engine v0.1.0"
git remote add origin git@github.com:<username>/gkm_engine.git
git branch -M main
git push -u origin main
```

---

## Testing

```bash
pip install pytest
pytest tests/ -v
```

---

## Versioning

Follows [Semantic Versioning](https://semver.org/) — currently **0.1.0**.

---

## License

MIT © Your Name