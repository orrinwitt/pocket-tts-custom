#!/usr/bin/env python3
"""
Pocket TTS — Windows Executable Launcher
Calls the serve() command to properly load the model before starting uvicorn.
"""

import os
import sys
import time
import webbrowser
import threading


def open_browser_when_ready():
    """Wait for server to be ready, then open browser."""
    import urllib.request
    url = "http://localhost:8000"
    for _ in range(60):
        try:
            urllib.request.urlopen(url, timeout=1)
            webbrowser.open(url)
            return
        except Exception:
            time.sleep(1)
    print("Server did not start in time. Open http://localhost:8000 manually.")


def main():
    # Start browser opener in background
    browser_thread = threading.Thread(target=open_browser_when_ready, daemon=True)
    browser_thread.start()

    # Import and call serve() which loads the model THEN starts uvicorn
    from pocket_tts.main import serve
    serve(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
