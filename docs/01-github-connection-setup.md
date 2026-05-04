# 01 — Connecting this folder to GitHub

This is the complete record of how `C:\ProgramData\Claude\Test Project` was linked to https://github.com/jagannathgs/Test-Project.

## Starting state

| Where | What was there |
|---|---|
| Local folder | Empty `.git` directory only — no files, no commits. |
| GitHub repo | Existed with `README.md` and `Test File`, on `main` branch. |
| `gh` CLI | Not installed (we did not need it). |
| Git Credential Manager (GCM) | Already installed globally — handles GitHub authentication via browser popup. |

## The decision: clone fresh

Three options were considered:
1. Add a remote and `git pull` into the existing folder.
2. Wipe `.git` and `git clone` fresh. ✅ **Chosen.**
3. Add a remote without pulling, push later.

**Why clone fresh?** Cleanest for a beginner — it's the standard workflow you see in every tutorial, and it sets up the remote + branch tracking correctly in one command.

## Authentication choice: HTTPS via Git Credential Manager

We did **not** use:
- ❌ A Personal Access Token (PAT) typed manually
- ❌ An SSH key

We used:
- ✅ **Git Credential Manager (GCM)** — pops up a browser window for GitHub sign-in. Easier and more secure than typing tokens.

Confirmed GCM was already configured globally:
```bash
git config --global --get credential.helper
# output: manager
```

## The exact commands run

### Step 1 — Wipe the empty `.git` and clone

```bash
rm -rf .git
git clone https://github.com/jagannathgs/Test-Project.git .
```

The trailing `.` means "clone into the current folder" instead of creating a sub-folder.

After this:
```bash
git log --oneline -5
# 9c842f9 Create Test File
# bd1e31b Initial commit
```

### Step 2 — Configure git identity (so commits are attributed to you)

```bash
git config user.name "jagannathgs"
git config user.email "jagannathgs@users.noreply.github.com"
```

These commands set the identity **only for this repo** (no `--global` flag). To set globally for all your repos:
```bash
git config --global user.name "jagannathgs"
git config --global user.email "<your email>"
```

#### Why noreply email?
GitHub's `users.noreply.github.com` address keeps your real email private but still attributes commits to your GitHub profile. To get your **personalized** noreply email (with your numeric GitHub ID), visit https://github.com/settings/emails — recommended for better profile linking.

To update later:
```bash
git config user.email "<new-email>"
```

### Step 3 — First push (GCM browser sign-in)

The first `git push` triggered GCM, which opened a browser window for GitHub sign-in. After approving, the credentials were saved by Windows Credential Manager so you won't be prompted again.

```bash
git push origin main
# To https://github.com/jagannathgs/Test-Project.git
#    9c842f9..006b2f0  main -> main
```

## How to verify the connection

```bash
git remote -v
# origin  https://github.com/jagannathgs/Test-Project.git (fetch)
# origin  https://github.com/jagannathgs/Test-Project.git (push)

git status
# On branch main
# Your branch is up to date with 'origin/main'.
# nothing to commit, working tree clean

git config --get user.name
# jagannathgs

git config --get user.email
# jagannathgs@users.noreply.github.com
```

## How to do this on a new machine

If you ever need to set up this project on a different computer:

```bash
# 1. Pick or create a parent folder, then:
git clone https://github.com/jagannathgs/Test-Project.git
cd Test-Project

# 2. Set identity (one time per machine, can use --global)
git config --global user.name "jagannathgs"
git config --global user.email "jagannathgs@users.noreply.github.com"

# 3. First push will trigger GCM browser sign-in
```

Then follow [02-python-playwright-setup.md](02-python-playwright-setup.md) to install Python dependencies.
