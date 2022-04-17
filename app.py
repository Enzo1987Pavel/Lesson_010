from flask import Flask

import funcs

app = Flask(__name__)

cand = funcs.candidates_preformat()


@app.route("/")
def main_page():
    return f"<pre>{cand}</pre>"


app.run()
