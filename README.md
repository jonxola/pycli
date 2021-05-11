**pycli** is a template for building CLI tools with Python.

The project is managed with [Poetry][1].

## Usage

Ideally, packages built with **pycli** are installed with [pipx][2]:
```
pipx install PACKAGE
```
This adds the entry points in `pyproject.toml` (listed under `tool.poetry.scripts`) to your PATH.

## Overview

`__init__.py` defines `run` — your package's main function. This is called by `__main__.py` when you run the package with `python -m PACKAGE`. It is also the entry point that is installed to your PATH.

`cli.py` is the module that handles CLI arguments. This is where the [`argparse`][3] module is used to define the package's interface. `cli.init()` returns an object holding the arguments.

`config.py` handles the configuration file — if you need that sort of thing. By default, this is a JSON file created at `~/.pycli/config.json`. The `config.init()` function returns an object containing the JSON data (or `None` if the file is invalid JSON).

`defaults.json` is the default configuration file that the `config` module creates when needed.

`run` is initiallly a barebones function that simply gathers the configuration values and CLI arguments. From there, you can do whatever you wish with your app.

[1]: https://python-poetry.org/
[2]: https://github.com/pipxproject/pipx
[3]: https://docs.python.org/3/library/argparse.html