import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/static/<path:path>")
def static_file(path):
    flask.send_from_directory("static", path)


app.run("0.0.0.0", 8080, True)
