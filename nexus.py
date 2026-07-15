"""Unreserved — Local development server.

Serves index.html on http://127.0.0.1:9376 and opens it in the default browser.
"""

import http.server
import webbrowser
import time
import os

PORT = 9376
HOST = "127.0.0.1"
DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    """Serve files from the project directory with clean logging."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, format, *args):
        if self.path != "/favicon.ico":
            print(f"  {self.command} {self.path} — {args[0] if args else ''}")


def main():
    server = http.server.HTTPServer((HOST, PORT), Handler)
    url = f"http://localhost:{PORT}/"

    print()
    print("=" * 50)
    print("  UNRESERVED — Study App")
    print(f"  Serving on {url}")
    print("  Press Ctrl+C to stop.")
    print("=" * 50)
    print()

    webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopping server...")
        server.shutdown()
        print("  Server stopped.")


if __name__ == "__main__":
    main()
