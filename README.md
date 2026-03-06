# Elgato Prompter Text Recoverer – Fix Missing Scripts in Camera Hub

> **Note:** This script and documentation were created with the help of [Claude](https://claude.ai) (Anthropic AI).

A simple Python script that recovers missing teleprompter scripts in **Elgato Camera Hub** on Windows.

> **Keywords:** elgato prompter scripts missing, camera hub texts disappeared, teleprompter scripts gone, prompter library empty, scripts not showing, camera hub lost scripts, elgato scripts reset, prompter texts missing after update, camera hub scripts vanished, elgato teleprompter recovery

---

## The Problem

If you have used Camera Hub's teleprompter text mode for a while, you may open the app one day to find that all — or most — of your scripts have disappeared from the list, even though the actual `.json` files still exist on disk.

**Why does this happen?**

Camera Hub stores your scripts as individual `.json` files in:
```
%APPDATA%\Elgato\CameraHub\Texts\
```

However, the app also maintains a separate list of which scripts to display, stored in `AppSettings.json` under the key `applogic.prompter.libraryList`. If the app crashes, is force-closed, or otherwise fails to save properly on exit, this list does not get updated — even though your script files are perfectly intact on disk.

## What This Script Does

- Scans all `.json` files in your `Texts` folder
- Adds any missing script GUIDs to `applogic.prompter.libraryList` in `AppSettings.json`
- Fixes duplicate `index` values across script files to prevent ordering conflicts
- Creates an automatic backup of `AppSettings.json` before making any changes

## Requirements

- Windows
- Python 3.x — download from [python.org](https://www.python.org/downloads/) if not already installed
  - During installation, make sure to check **"Add Python to PATH"**

## Usage

1. **Close Camera Hub completely** — right-click the tray icon and select *Quit Camera Hub*
2. Download and run `recover_missing_scripts.py`
3. **Restart Camera Hub** — your scripts should now appear in the list

## Notes

- A backup of your original `AppSettings.json` is automatically saved as `AppSettings.json.backup` in the same folder before any changes are made
- The script only adds missing entries — it does not remove or modify any existing scripts
- The script can be safely run multiple times

---

> **Note:** This script and documentation were created with the help of [Claude](https://claude.ai) (Anthropic AI).
