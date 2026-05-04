# 04 — Troubleshooting & known issues

Issues we hit during the initial setup, and how they were solved.

## Issue: `git push` hung waiting for credentials

**What happened:** When `git push` was run from a non-interactive shell (like Claude Code's automated bash tool), Git Credential Manager's browser popup did not appear, so the push hung indefinitely waiting for sign-in.

**Solution:** Run `git push` (or any first-time auth command) from your **own interactive terminal**. In Claude Code, prefix the command with `!` to make it run in your interactive shell:

```
! git push origin main
```

This lets GCM pop up the browser window properly so you can sign in.

**After signing in once:** GCM stores credentials in Windows Credential Manager, so subsequent pushes won't prompt again.

---

## Issue: `pytest` says "no tests found"

**Cause:** pytest only runs files that match the pattern `test_*.py` and functions named `test_*`.

**Fix:**
- Filename must start with `test_` → `test_login.py` ✅, `login_test.py` ❌
- Function name must start with `test_` → `def test_login():` ✅, `def login_works():` ❌

---

## Issue: `pytest` says `command not found`

**Cause:** Virtual environment not activated. `pytest` lives inside `.venv/`, not on your system PATH.

**Fix:**
```bash
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux / Mac / Git Bash
```

You should see `(.venv)` at the start of your prompt.

---

## Issue: "browser not found" or `Executable doesn't exist` from Playwright

**Cause:** Browser binaries weren't downloaded, or got cleaned up.

**Fix:**
```bash
playwright install
```

(Re-downloads Chromium + Firefox + WebKit. ~400 MB.)

---

## Issue: Line ending warnings on Windows

**Symptom:**
```
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
```

**Cause:** Windows uses CRLF line endings; the repo files were written with LF. Git auto-converts on Windows.

**Fix:** Ignore — these are warnings, not errors. The conversion is intentional and correct.

To silence them:
```bash
git config core.autocrlf true
```

---

## Issue: `git push` rejected — "Updates were rejected because the remote contains work that you do not have locally"

**Cause:** Someone (or you, on another machine) pushed changes to GitHub that you don't have yet.

**Fix:**
```bash
git pull              # download and merge the remote changes
git push              # try push again
```

If `git pull` reports merge conflicts → ask for help, don't blindly resolve them.

---

## Issue: "fatal: refusing to merge unrelated histories"

**Cause:** Your local repo and remote repo started independently and have no shared commits.

**Fix:** Don't blindly run with `--allow-unrelated-histories` flag — it can create a mess. Better to investigate first. In our setup we avoided this by cloning fresh (option B) instead of trying to merge.

---

## Issue: Tests pass locally but you want to see them run visibly

**Fix:** add the `--headed` flag:
```bash
pytest --headed
```

Or pause between actions to watch slowly:
```bash
pytest --headed --slowmo=1000     # 1000 ms = 1 second between actions
```

---

## Issue: Want to record what your test does and replay it

Playwright has a "codegen" feature that records your manual clicks into Python code:

```bash
playwright codegen https://your-app.com
```

A browser window opens. Click around, fill forms — Playwright writes the code in real-time in a side panel. Copy/paste into a test file.

Excellent for learning the API.

---

## When in doubt

1. `git status` — what's the current state?
2. Read the error message carefully — Playwright errors are usually descriptive.
3. Ask for help — paste the full error message and what you ran.
