from flask import Flask, send_from_directory

app = Flask("example-2")

@app.route("/")
def serve_html():
    return send_from_directory("html", filename = "index.html")

app.run()
