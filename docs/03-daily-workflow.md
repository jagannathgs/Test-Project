# 03 — Daily workflow

The cycle you'll repeat every day. Bookmark this file.

## Mental model: 3 places your work lives

```
1. Your folder           →  what you see and edit
2. Your local git        →  saved snapshots on your laptop
3. GitHub                →  the cloud copy (everyone can see)
```

Saving a file in your editor only updates **#1**. Git commands move work between #1 → #2 → #3.

## Starting a work session

```bash
# Open your terminal in the project folder, then:
.venv\Scripts\activate          # Windows — turn on the venv
git pull                        # grab any changes from GitHub first
```

You'll see `(.venv)` at the start of your prompt when the venv is active.

## Writing a new test

1. Create a file in `tests/` named `test_<thing>.py` (it MUST start with `test_` so pytest finds it).
2. Each test function inside also MUST start with `test_`.
3. Use the `page: Page` parameter — pytest-playwright provides it for free.

Minimal template:

```python
from playwright.sync_api import Page, expect


def test_something(page: Page):
    page.goto("https://your-app.com")
    expect(page.get_by_role("button", name="Login")).to_be_visible()
```

## Running tests

| Command | What it does |
|---|---|
| `pytest` | Run all tests in `tests/`, headless (no browser window). |
| `pytest --headed` | Run with visible browser — great for debugging. |
| `pytest --headed --slowmo=500` | Same, but pause 500ms between actions so you can see what's happening. |
| `pytest tests/test_login.py` | Run only one file. |
| `pytest tests/test_login.py::test_valid_user` | Run only one test function. |
| `pytest -k login` | Run all tests with "login" in the name. |
| `pytest --browser firefox` | Run on Firefox instead of Chromium. |
| `pytest --browser chromium --browser firefox` | Run on multiple browsers. |

## Saving work — the 3-step git cycle

After you finish writing/editing tests, save them to GitHub:

```bash
# Step 1: Stage the files (tell git "these are the ones I want to save")
git add tests/test_login.py
# Or stage everything that changed:
git add .

# Step 2: Commit (take a snapshot, lives on your laptop only)
git commit -m "add login test for valid user"

# Step 3: Push (upload snapshot to GitHub)
git push
```

### Writing good commit messages

- Start with a verb: `add`, `fix`, `update`, `remove`.
- Be specific: ❌ `"changes"` → ✅ `"add login test for invalid password"`.
- Keep the first line under ~70 characters.

## Checking what state you're in

```bash
git status
```

This is your most-used command. It tells you:
- What files you've changed
- What's staged for commit
- Whether you're behind/ahead of GitHub

```bash
git log --oneline -10
```

Shows the last 10 commits.

## Quick "save everything" cheat sheet

When you've made changes and want to save them all:

```bash
git status                              # see what changed
git add .                               # stage everything
git commit -m "describe what you did"   # snapshot
git push                                # upload to GitHub
```

Or just say **"commit and push"** to me and I'll do it.

## Ending a session

Nothing special needed. You can:
- Leave the terminal open
- Or close it — your venv deactivates automatically when you close the shell

Just make sure you've **pushed** before stepping away for the day, so your work is safe on GitHub even if your laptop dies.

## Common "uh-oh" moments

| Situation | What to do |
|---|---|
| `pytest: command not found` | Forgot to activate venv. Run `.venv\Scripts\activate`. |
| `git push` rejected, says "behind" | Run `git pull` first, then `git push`. |
| You committed something wrong | Don't panic — ask for help. There are safe ways to undo. |
| Tests fail with "browser not found" | Run `playwright install` again. |

More in [04-troubleshooting.md](04-troubleshooting.md).
