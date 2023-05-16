import socket

UDP_IP_ADDRESS = "213.209.210.193"  # IP al livello due. INDIRIZZO DEL TUO PC
UDP_PORT_NO = 12000  # numero di porta che si rappresenta su due byte (16bit)

server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
)  # creazione socket, libreria socket, oggetto socket. AF_INET e SOCK_DGRAM sono due variabili. Il primo è una famiglia di indirizzi che utilizzano l'IP V4, il secondo è datagram
server_socket.bind(
    (UDP_IP_ADDRESS, UDP_PORT_NO)
)  # UDP e TCP sono migliori poichè non hanno bisogno di creare altre unità di trasporto, il bind dice a cosa attaccarsi

print("UDP server up and listening")

# preparazione applicazione
contatore = 0


def app(msg):
    global contatore
    try:   
    numero = int(msg)
except:
return "Accetto solo numeri!!"
    contatore += numero
    return f"Siamo al numero: {contatore}"


while True:
    data, addr = server_socket.recvfrom(
        1024
    )  # data sono i dati che arrivano, addr è il numero di porta che invia il messaggio. receive from (dimensione massima, anche se si può arrivare fino a 15000)
    print("Received message:", addr, data.decode())  # decodifica i dati

    # sviluppo applicazione
    msg = data.decode()

    resp = app(msg)

    # resp = f"{data} {addr[0]} {addr[1]}"

    server_socket.sendto(resp.encode(), addr)
    if (
        addr[0] == UDP_IP_ADDRESS and data.decode() == "quit"
    ):  # questo serve, quando si scrive quit di chiudere
        break
