import sys
from threading import Timer
from backend.helper import *
from backend.exceptions import *
from webbrowser import open as webbrowser_open
from flask import (
    Flask,
    render_template
)

log("Starting app...")


k = foreplay(loadOptions())
try:
    if "0" in k:
        raise InitializationErr(f"App unable to initialize, failed with error code: [{k}]")
    else:
        log(f"App initialized successfully; code: {k}")
except InitializationErr as e:
    log(f"Initialization error: {e}", 3)
    sys.exit(1)


app = Flask(__name__)


@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.errorhandler(404)
def not_found_404(e):
    return render_template("404.html"), 404

@app.errorhandler(405)
def not_found_405(e):
    return render_template("405.html"), 405


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8080, debug=False)
        # Timer(1, lambda: webbrowser_open("http://0.0.0.0:8080")).start()
    except KeyboardInterrupt:
        log(r"^C pressed, shutting down marionette", 1)
        log(r"Shutdown marionette successfully")
        sys.exit(0)
    except Exception as e:
        log(f"Error: {e}", 3)
        raise
