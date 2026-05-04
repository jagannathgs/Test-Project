# Test-Project

Learning — web test automation with **Python + Playwright + pytest**.

## Setup (first time only)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
playwright install
```

## Run tests

```bash
.venv\Scripts\activate
pytest                          # run all tests (headless)
pytest --headed                 # see the browser while tests run
pytest tests/test_example.py    # run one file
pytest -k login                 # run tests whose name contains "login"
```

## Project layout

```
tests/             pytest test files (test_*.py)
requirements.txt   Python dependencies
pytest.ini         pytest config
```
