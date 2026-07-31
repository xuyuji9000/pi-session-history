#!/usr/bin/env python3
import json
import glob
import os
import sys

def main():
    num_sessions = 10
    if len(sys.argv) > 1:
        try:
            num_sessions = int(sys.argv[1])
        except ValueError:
            print(f"Usage: {os.path.basename(sys.argv[0])} [number_of_sessions]")
            sys.exit(1)

    sessions_dir = os.path.expanduser("~/.pi/agent/sessions")
    files = glob.glob(f"{sessions_dir}/*/*.jsonl")

    # Sort files by modification time descending
    files.sort(key=os.path.getmtime, reverse=True)

    print(f"{'Date':<20} | {'Session ID':<36} | {'Workspace':<35} | {'Description'}")
    print("-" * 150)

    for f in files[:num_sessions]:
        workspace = "Unknown"
        desc = "No description"
        timestamp = "Unknown"
        session_id = "Unknown"
        
        try:
            with open(f, 'r') as fp:
                for line in fp:
                    try:
                        data = json.loads(line)
                        if data.get("type") == "session":
                            timestamp = data.get("timestamp", timestamp)[:19].replace("T", " ")
                            workspace = data.get("cwd", workspace)
                            session_id = data.get("id", session_id)
                            home_dir = os.path.expanduser("~")
                            if workspace.startswith(home_dir):
                                workspace = "~" + workspace[len(home_dir):]
                        elif data.get("type") == "message" and data.get("message", {}).get("role") == "user":
                            content = data.get("message", {}).get("content", [])
                            for c in content:
                                if c.get("type") == "text":
                                    desc = c.get("text", "").strip().split('\n')[0]
                                    if len(desc) > 50:
                                        desc = desc[:47] + "..."
                                    break
                            break
                    except Exception:
                        pass
        except Exception:
            pass
            
        print(f"{timestamp:<20} | {session_id:<36} | {workspace[:33]:<35} | {desc}")

if __name__ == "__main__":
    main()
