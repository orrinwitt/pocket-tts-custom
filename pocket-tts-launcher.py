#!/usr/bin/env python3
"""
Pocket TTS — Windows Executable Launcher
Bundles the FastAPI server and auto-opens the browser.
"""

import os
import sys
import time
import webbrowser
import threading
import uvicorn


def get_static_dir():
    """Find the static directory whether running from source or PyInstaller bundle."""
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running from source
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "pocket_tts", "static")


def open_browser_when_ready():
    """Wait for server to be ready, then open browser."""
    import urllib.request
    url = "http://localhost:8000"
    for _ in range(30):
        try:
            urllib.request.urlopen(url, timeout=1)
            webbrowser.open(url)
            return
        except Exception:
            time.sleep(1)
    print("Server did not start in time. Open http://localhost:8000 manually.")


def main():
    # Ensure static dir exists (PyInstaller compatibility)
    static_dir = get_static_dir()
    os.environ.setdefault("POCKET_TTS_STATIC_DIR", static_dir)

    # Start browser opener in background
    browser_thread = threading.Thread(target=open_browser_when_ready, daemon=True)
    browser_thread.start()

    # Start the FastAPI server
    print("Starting Pocket TTS server on http://localhost:8000")
    print("Press Ctrl+C to stop.\n")

    uvicorn.run(
        "pocket_tts.main:web_app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )


if __name__ == "__main__":
    main()
