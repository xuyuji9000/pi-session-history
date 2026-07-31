---
name: pi-session-history
description: Lists the most recent pi agent sessions along with their ID, date, workspace directory, and a brief description. Use this when you need to find a previous session or its ID.
---

# Pi Session History Skill

This skill provides a script to list previous pi agent sessions.

## Usage

Run the Python script located in this skill's directory:

```bash
python3 pi-session-history.py [number_of_sessions]
```

- If `[number_of_sessions]` is omitted, it defaults to 10.
- Example: `python3 pi-session-history.py 5` lists the 5 most recent sessions.

The output includes:
- Date
- Session ID
- Workspace path
- Description (first user prompt)