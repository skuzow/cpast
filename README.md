# 🕓 Cpast

[![python](https://img.shields.io/badge/python->=%203.7%20-blue)](https://www.python.org/downloads)
[![pypi](https://img.shields.io/pypi/v/cpast)](https://pypi.org/project/cpast)
[![license](https://img.shields.io/github/license/skuzow/cpast.svg)](https://github.com/skuzow/cpast/blob/main/LICENSE)
[![release](https://github.com/skuzow/cpast/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/skuzow/cpast/actions/workflows/release.yml)
[![test](https://github.com/skuzow/cpast/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/skuzow/cpast/actions/workflows/test.yml)

Git commit in the past.

## 🗿 Usage

```bash
  python -m cpast -d DATE -t TIME -m MESSAGE
```

- Date format: `YYYY-MM-DD`
- Time format: `HH:MM:SS`

## ⚙️ Options

- `-h, --help` Show help message and exit
- `-d DATE, --date DATE` Commit date, example: 2021-12-25
- `-t TIME, --time TIME` Commit time, example: 22:13:05
- `-m MESSAGE, --message MESSAGE` Commit message, example: "init :)"

## 🧩 Install

### [uv](https://docs.astral.sh/uv)

Global tool:

```bash
uv tool install cpast
```

Current project:

```bash
uv add cpast
```

### [pip](https://pip.pypa.io)

Global tool:

```bash
pip install --user cpast
```

Current project:

```bash
pip install cpast
```

## 🚀 Development

Install [uv](https://docs.astral.sh/uv/), then from the repository root:

Install project + dev tools:

```bash
uv sync
```

Build the distribution artifacts:

```bash
uv build
```

Verify package metadata and README rendering:

```bash
uv run twine check dist/*
```

Lint the source and tests:

```bash
uv run flake8 cpast tests
```

Run the test suite:

```bash
uv run pytest tests
```
