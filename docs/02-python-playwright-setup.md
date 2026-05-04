# 02 — Python, Playwright, and pytest setup

This is the complete record of how the test automation stack was installed.

## Stack chosen: Python + Playwright + pytest

For a learner doing web test automation, this stack was picked because:

- **Python**: cleanest syntax for beginners; testing community is huge.
- **Playwright**: modern browser automation; **auto-waits** for elements (fewer flaky tests than Selenium); supports Chromium, Firefox, and WebKit (Safari) in one library.
- **pytest**: industry-standard Python test runner.
- **pytest-playwright**: glue plugin that gives you a `page` fixture in tests automatically.

Alternatives considered: JavaScript+Playwright (good but async syntax is harder for beginners), Java+Selenium (lots of boilerplate), Cypress (JS-only, limited cross-browser).

## Pre-existing on the machine

```bash
python --version
# Python 3.14.4
```

`node` and `java` were not installed (we did not need them).

## Step 1 — Create a Python virtual environment

A "venv" is an isolated Python environment for this project. Why bother?

- Keeps Playwright/pytest dependencies out of your system Python.
- If you delete `.venv/` later, your global Python is untouched.
- Each project can pin its own versions.

```bash
python -m venv .venv
```

This creates a `.venv/` folder in the project. **Never commit `.venv/`** — it's machine-specific and huge. Our `.gitignore` already excludes it.

## Step 2 — Activate the venv

After activation, every `python` and `pip` command uses the venv's copies, not your system Python.

**Windows (cmd / PowerShell):**
```bash
.venv\Scripts\activate
```

**Git Bash / Linux / macOS:**
```bash
source .venv/bin/activate
```

You'll see `(.venv)` appear at the start of your prompt when activated.

> Note: in this initial setup, instead of activating, we ran the venv's Python directly with `.venv/Scripts/python.exe -m pip ...` — works the same, just more explicit.

## Step 3 — Upgrade pip, install dependencies

```bash
.venv/Scripts/python.exe -m pip install --upgrade pip
.venv/Scripts/python.exe -m pip install playwright pytest pytest-playwright
```

What got installed (key packages):

| Package | Purpose |
|---|---|
| `playwright` | The browser automation library |
| `pytest` | The test runner |
| `pytest-playwright` | Adds the `page` fixture to pytest tests |

A `requirements.txt` was created so the install can be repeated:

```bash
playwright>=1.59.0
pytest>=9.0.0
pytest-playwright>=0.7.2
```

To install from `requirements.txt` in the future:
```bash
pip install -r requirements.txt
```

## Step 4 — Download browser binaries

Playwright drives **real browsers**, not headless mocks. The browsers themselves are separate downloads (~400 MB total):

```bash
.venv/Scripts/python.exe -m playwright install
```

This downloaded:
- **Chromium** (used by Chrome/Edge)
- **Firefox**
- **WebKit** (used by Safari)

They went to `C:\Users\jagannath\AppData\Local\ms-playwright\` — outside the project folder, so multiple projects share them.

## Step 5 — Project structure created

```
Test-Project/
├── .git/                  # git's bookkeeping (never edit)
├── .gitignore             # tells git which files to ignore
├── .venv/                 # Python virtual env (ignored by git)
├── docs/                  # this documentation
├── tests/                 # pytest test files (named test_*.py)
│   └── test_example.py    # starter Playwright test — demonstrates the setup works
├── pytest.ini             # pytest configuration
├── README.md              # project intro and quick-start
├── requirements.txt       # Python dependencies (so others can `pip install -r`)
└── Test File              # original file from initial GitHub commit
```

### `pytest.ini` contents
```ini
[pytest]
testpaths = tests
addopts = -v --tb=short
```
- `testpaths = tests` → pytest only looks in `tests/` for test files.
- `addopts = -v --tb=short` → verbose output and short tracebacks (easier to read).

### `tests/test_example.py` contents

Two starter tests against playwright.dev — proved the whole stack works end-to-end:

```python
from playwright.sync_api import Page, expect


def test_playwright_homepage_has_correct_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")


def test_get_started_link_navigates_to_installation_page(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
```

## Step 6 — First test run (verification)

```bash
.venv/Scripts/python.exe -m pytest
```

Output:
```
tests/test_example.py::test_playwright_homepage_has_correct_title[chromium] PASSED
tests/test_example.py::test_get_started_link_navigates_to_installation_page[chromium] PASSED

============================== 2 passed in 6.44s ==============================
```

✅ Both tests passed — setup confirmed working.

## How to repeat this on a new machine

Once you've cloned the repo (see [01-github-connection-setup.md](01-github-connection-setup.md)):

```bash
# 1. Make sure Python 3.10+ is installed
python --version

# 2. Create venv and activate
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

# 3. Install Python deps
pip install -r requirements.txt

# 4. Install browsers (~400 MB download, one-time)
playwright install

# 5. Run tests to confirm
pytest
```

That's it — your machine matches the original setup.
