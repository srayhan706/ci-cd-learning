# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose

A small learning repo for practicing CI/CD with GitHub Actions and Docker. The application code (`app.py`) is intentionally trivial (arithmetic functions); the real subject is the pipeline around it.

## Commands

```bash
pip install -r requirements.txt   # installs pytest and ruff (no app runtime deps)
ruff check .                      # lint — must pass in CI
pytest                            # run all tests
pytest tests/test_app.py::test_add  # run a single test
python app.py                     # run the app

docker build -t ci-cd-learning .
docker run --rm ci-cd-learning    # runs `python app.py` in python:3.12-slim
```

There is no ruff or pytest config file, so both run with defaults. Tests import from `app` directly, so run `pytest` from the repo root.

## CI pipeline

`.github/workflows/ci.yml` runs on pushes and PRs to `main`, with two independent jobs on Python 3.12:
- **lint**: `ruff check .`
- **test**: `pytest` (also echoes `$APP_ENV`, which the workflow does not currently define)

Work happens on feature branches (e.g. `feature/...`) merged into `main` via PR so CI runs.

## Notes

- Function names are used as-is by the tests, including the misspelling `multipication`. Renaming it requires updating `tests/test_app.py`.
- Any top-level code in `app.py` (such as the `print(...)` call) also runs when tests import the module.
