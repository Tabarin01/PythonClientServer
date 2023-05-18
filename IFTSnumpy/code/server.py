import flask
import os
import json

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("upload.html")


@app.route("/uploader/<path:path>", methods=["POST"])
def uploader(path):
    # print(flask.request.files)
    # uploaded = flask.request.files["file"]
    uploaded = flask.request.files.getlist("file")
    # print(uploaded)

    # uploaded.save(f"uploads/{path}{uploaded.filename}")
    for f in uploaded:
        f.save(f"uploads/{path}{f.filename}")
        print(f"uploads/{path}{f.filename}")
    return json.dumps(
        {"success": True, "message": "Caricamento avvenuto con successo!"}
    )


@app.route("/create_folder/<path:path>", methods=["GET", "POST"])
def create_folder(path):
    # print(path)
    if os.path.exists(f"uploads/{path}"):
        return json.dumps({"success": False, "error": "la cartella esiste"})
    else:
        os.mkdir(f"uploads/{path}")
    return json.dumps({"success": True, "folder": path})


@app.route("/folders")
def folders():
    return flask.render_template("folders.html")


"""
il parametro json folder vuole / alla fine se è una sottocartella
"""


@app.route("/read_folder", methods=["POST"])
def read_folder():
    folder = flask.request.get_json()["folder"]

    if os.path.exists(f"uploads/{folder}"):
        tutto = os.listdir(f"uploads/{folder}")
        dir = []
        fls = []
        for x in tutto:
            y = f"uploads/{folder}" + x
            x = f"{folder}" + x
            if os.path.isdir(y):
                dir += [x]
            if os.path.isfile(y):
                fls += [x]
        return json.dumps({"success": True, "folders": dir, "files": fls})
    else:
        return json.dumps({"success": False})


@app.route("/get_file/<path:path>")
def get_file(path):
    return flask.send_file(f"../uploads/{path}")


app.run("0.0.0.0", 5000, True)
