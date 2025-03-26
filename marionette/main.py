import ast, argparse
from threading import Timer
from backend.helper import *
from backend.exceptions import *
from webbrowser import open as webbrowser_open
from flask import (
    Flask,
    render_template
)


print("[  OK  ] Starting app...")
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.errorhandler(404)
def not_found_404(e):
    return render_template("404.html"), 404

@app.errorhandler(405)
def not_found_405(e):
    return render_template("405.html"), 405


if __name__ == "__main__":
    try:
        k = "[" + foreplay(parseArgs()) + "]"
        if k not in ["[I-11]", "[I-22]", "[I-12]", "[I-21]"]:
            raise InitializationErr(f"App unable to initialize, failed with error code: {k}")
        else:
            print(f"[  OK  ] App initialized successfully; code: {k}")

        app.run(host="0.0.0.0", port=8080, debug=True)
        # Timer(1, lambda: webbrowser_open("http://0.0.0.0:8080")).start()
    except InitializationErr as e:
        print(f"[ FAIL ] Initialization error: {e}")
    except Exception as e:
        print(f"[ FAIL ] Error: {e}")
