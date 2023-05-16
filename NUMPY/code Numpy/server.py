import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("upload.html")


@app.route("/uploader", methods=["POST"])
def uploader():
    uploaded = flask.request.files[
        "file"
    ]  # files si riferisce all'HTML input type=file name=file
    uploaded.save(f"uploads/{uploaded.filename}")
    return "Caricamento avvenuto con successo!"


app.run("0.0.0.0", 5000)
