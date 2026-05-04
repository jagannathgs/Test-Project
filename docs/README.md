# Project Documentation

This folder contains complete records of how this project was set up and how to work with it day-to-day.

## Contents

| File | What's in it |
|---|---|
| [01-github-connection-setup.md](01-github-connection-setup.md) | How this local folder was connected to the GitHub repo (cloning, authentication, identity). |
| [02-python-playwright-setup.md](02-python-playwright-setup.md) | How Python, Playwright, and pytest were installed and configured. |
| [03-daily-workflow.md](03-daily-workflow.md) | The everyday cycle: write tests → commit → push. Cheat sheet for daily use. |
| [04-troubleshooting.md](04-troubleshooting.md) | Known issues we hit during setup and how they were solved. |

## Quick reference

- **GitHub repo:** https://github.com/jagannathgs/Test-Project
- **Local folder:** `C:\ProgramData\Claude\Test Project`
- **Stack:** Python 3.14 + Playwright + pytest
- **Branch:** `main`
- **Auth method:** Git Credential Manager (GCM) — browser-based GitHub sign-in

## When you forget how to do something

1. First, check [03-daily-workflow.md](03-daily-workflow.md) — covers 90% of daily tasks.
2. If something broke, check [04-troubleshooting.md](04-troubleshooting.md).
3. If a brand new machine — follow [01](01-github-connection-setup.md) then [02](02-python-playwright-setup.md) in order.
