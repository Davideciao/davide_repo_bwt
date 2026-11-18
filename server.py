import socket
from main import trasformata_bwt

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

conn, addr = server.accept()

parola = conn.recv(1024).decode()
risultato = trasformata_bwt(parola)
conn.send(risultato.encode())

conn.close()
server.close()