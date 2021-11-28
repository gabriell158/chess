import socket, sys
from chess import *

SIZE = 100000
HOST = '127.0.0.1'
PORT = 12345
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = (HOST, PORT)
serverSocket.bind(serverAddress)
serverSocket.listen(1)
while True:
    clientSocket, clientAddress = serverSocket.accept()
    serverSocket.close()
    print('Cliente conectado => ', clientAddress)
    message = welcome()
    clientSocket.send(message.encode())
    while True:
        clientResponse = clientSocket.recv(SIZE).decode()
        if not clientResponse: break
        while True:
            clientResponse = clientSocket.recv(SIZE).decode()
            if not clientResponse: break
            if clientResponse == 'jogar':
                break
            message = toPlayOrNotToPlay()
            clientSocket.send(message.encode())
        message = weArePlaying()
        clientSocket.send(message.encode())
        clientResponse = clientSocket.recv(SIZE).decode()
        if not clientResponse: break
        while True:
            if clientResponse == 'preto' or clientResponse == 'branco':
                break
            message = chooseYourColor()
            clientSocket.send(message.encode())
            clientResponse = clientSocket.recv(SIZE).decode()
            if not clientResponse: break
        message = blackOrWhite(clientResponse)
        clientColor, serverColor = assignColors(clientResponse)
        clientPieces, serverPieces = assignPieces(clientColor)
        matrix = createTable(clientColor)
        table = renderTable(matrix)
        if clientColor == "preto":
            print(table)
            matrix = serverPlay(matrix, serverPieces)
            table = renderTable(matrix)
        message = message + table
        clientSocket.send(message.encode())
        clientResponse = clientSocket.recv(SIZE).decode()
        if not clientResponse: break
        while True:
            if clientResponse == 'preto' or clientResponse == 'branco':
                break
            message = chooseYourColor()
            clientSocket.send(message.encode())
            clientResponse = clientSocket.recv(SIZE).decode()
            if not clientResponse: break
        clientSocket.send("legal fera".encode())
    print('Conexão finalizada com o cliente  ', clientAddress)
    clientSocket.close()
    sys.exit(0)