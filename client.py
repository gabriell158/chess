import socket

HOST = '127.0.0.1'
PORT = 12345
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = (HOST, PORT)
clientSocket.connect(serverAddress)
print('Digite o seu nome')
message = input('--> ').encode()
clientSocket.send(message)
while message != b'sair':
    serverResponse = clientSocket.recv(10000)
    print(serverResponse.decode())
    message = input('--> ').encode()
    clientSocket.send(message)
clientSocket.close()
print('Adeus...')