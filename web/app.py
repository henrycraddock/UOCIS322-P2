"""
Henry Craddock's Flask API.
"""

from flask import Flask, abort, send_from_directory
import os
import config


app = Flask(__name__)

@app.route("/<file_name>")
def hello(file_name):
     options = config.configuration()
     docroot = options.DOCROOT
     pages = os.listdir(docroot)
     if "//" in file_name or "~" in file_name or ".." in file_name:
         abort(403)
     elif file_name in pages:
         return send_from_directory(docroot, file_name)
     else:
         abort(404)


@app.errorhandler(404)
def not_found(e):
    return send_from_directory('templates', '404.html'), 404


@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('templates', '403.html'), 403


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
