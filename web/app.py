"""
Henry Craddock's Flask API.
"""

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"


@app.errorhandler(404)
def not_found(e):
    return send_from_directory('templates', '404.html'), 404


@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('templates', '403.html'), 403


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
