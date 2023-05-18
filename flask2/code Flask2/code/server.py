import flask
import json

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/paga", methods=["POST"])
def paga():
    carrello = flask.request.get_json()
    for item in carrello:
        print(item)
    return json.dumps({"success": True})
    
@app.route("/static/<path:path>")
def static_files(path):
    flask.send_from_directory("static", path)

app.run("0.0.0.0", 8080, True)