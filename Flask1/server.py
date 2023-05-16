import flask
import json

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    risposta = ""
    for i in range(10):
        risposta += f"<h{i}>{i}</h{i}>"
    return risposta

@app.route("/pagina1")
def pagina1():
    content = ""
    with open("code/pagina1.html") as file:
        content = file.read()
    return content

@app.route("/pagina2")
def pagina2():
    return flask.render_template("pagina2.html")

@app.route("/calcolatrice")
def calcolatrice():
    return flask.render_template("calcolatrice.html")


@app.route("/calcolatriceAPI", methods=["GET", "POST"])
def calcolatriceAPI():

    if flask.request.method == "GET":
        return "Daniele, non puoi accedere in GET!"
    
    GET = flask.request.args # per leggere i parametri GET
    POST = flask.request.get_json() # per leggere i parametri POST
    
    numero1 = int(POST["numero1"])
    numero2 = int(POST["numero2"])
    operazione = POST["operazione"]

    if operazione == "+":
        risultato = numero1 + numero2
    if operazione == "-":
        risultato = numero1 - numero2
    if operazione == "*":
        risultato = numero1 * numero2
    if operazione == "/":
        risultato = numero1 / numero2
    if operazione == "power":
        risultato = numero1 ** numero2
    if operazione == "root":
        risultato = numero1 ** (1/numero2)
    
    return json.dumps(risultato)



@app.route('/static/<path:path>')
def send_static(path):
    return flask.send_from_directory('static', path)


app.run("0.0.0.0", 8080, True)