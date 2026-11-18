import socket

HOST = "127.0.0.1"
PORT = 12345

parola = input("Inserisci la parola: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(parola.encode())

risultato = client.recv(1024).decode()
print(risultato)

client.close()