from math import sqrt

# peças brancas
WHITE_QUEEN = 1
WHITE_BISHOP = 2
WHITE_KNIGHT = 3
WHITE_ROOK = 4
WHITE_PAWN = 5
WHITE_KING = 6

# peças pretas
BLACK_QUEEN = 7
BLACK_BISHOP = 8
BLACK_KNIGHT = 9
BLACK_ROOK = 10
BLACK_PAWN = 11
BLACK_KING = 12

def howToPlay():
  return "Para fazer uma jogada, digite a origem e o destina da peça que deseja mover separado por vírgula.\n(e.g. H1,H4)"

def welcome():
  return "Bem vindo ao joguinho de xadrez!\nVocê quer jogar comigo?\nDigite 'jogar' para começar ou 'sair' a qualquer momento para sair.\nJogar?"

def toPlayOrNotToPlay():
  return "Digite uma opção válida! \nDigite 'jogar' para começar ou 'sair' a qualquer momento para sair."

def weArePlaying():
  return "Oba! Vamos jogar!\nPara fazer uma jogada, digite a origem e o destina da peça que deseja mover separado por vírgula.\n(e.g. H1,H4)\nQual cor você quer?\nDigite 'preto' ou 'branco.'"

def chooseYourColor():
  return "Digite uma opção válida! \nDigite 'preto' ou 'branco'."

def blackOrWhite(message: str):
  if message == "preto":
    print('O cliente está jogando com as peças pretas')
    print('O servidor jogará com as peças brancas')
    return "Já começei!"
  if message == "branco":
    print('O cliente está jogando com as peças brancas')
    print('O servidor jogará com as peças pretas')
    return "Você começa!"
  return "Não entendi..."

def assignColors(color: str):
  if color == 'preto':
    return 'preto', 'branco'
  if color == 'branco':
    return 'branco', 'preto'
  return 'cinza', 'cinza'

def assignPieces(color: str):
  if (color == 'branco'):
    return [
      WHITE_ROOK,
      WHITE_KNIGHT,
      WHITE_BISHOP,
      WHITE_QUEEN,
      WHITE_KING,
      WHITE_BISHOP,
      WHITE_KNIGHT,
      WHITE_ROOK,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN
    ],[
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_ROOK,
      BLACK_KNIGHT,
      BLACK_BISHOP,
      BLACK_QUEEN,
      BLACK_KING,
      BLACK_BISHOP,
      BLACK_KNIGHT,
      BLACK_ROOK
    ]
  if (color == 'preto'):
    return [
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_PAWN,
      BLACK_ROOK,
      BLACK_KNIGHT,
      BLACK_BISHOP,
      BLACK_QUEEN,
      BLACK_KING,
      BLACK_BISHOP,
      BLACK_KNIGHT,
      BLACK_ROOK
    ],[
      WHITE_ROOK,
      WHITE_KNIGHT,
      WHITE_BISHOP,
      WHITE_QUEEN,
      WHITE_KING,
      WHITE_BISHOP,
      WHITE_KNIGHT,
      WHITE_ROOK,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN,
      WHITE_PAWN
    ]
  return [0], [0]

def createTable(color: str):
  if (color == 'preto'):
    board = [
      [
        WHITE_ROOK,
        WHITE_KNIGHT,
        WHITE_BISHOP,
        WHITE_QUEEN,
        WHITE_KING,
        WHITE_BISHOP,
        WHITE_KNIGHT,
        WHITE_ROOK
      ],
      [
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN
      ],
      [0,
       0,
       0,
       0,
       0,
       0,
       0,
       0],
      [0,
       0,
       0,
       0,
       0,
       0,
       0,
       0],
      [0,
       0,
       0,
       0,
       0,
       0,
       0,
       0],
      [0,
       0,
       0,
       0,
       0,
       0,
       0,
       0],
      [
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN
      ],
      [
        BLACK_ROOK,
        BLACK_KNIGHT,
        BLACK_BISHOP,
        BLACK_QUEEN,
        BLACK_KING,
        BLACK_BISHOP,
        BLACK_KNIGHT,
        BLACK_ROOK
      ],
    ]
  else:
    board = [
      [
        BLACK_ROOK,
        BLACK_KNIGHT,
        BLACK_BISHOP,
        BLACK_QUEEN,
        BLACK_KING,
        BLACK_BISHOP,
        BLACK_KNIGHT,
        BLACK_ROOK
      ],
      [
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN,
        BLACK_PAWN
      ],
      [0,
       0,
       0,
       0,
       0,
       0,
       0,
       0],
      [0,
       0,
       0,
       0,
       0,
       0,
       0,
       0],
      [0,
       0,
       0,
       0,
       0,
       0,
       0,
       0],
      [0,
       0,
       0,
       0,
       0,
       0,
       0,
       0],
      [
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN,
        WHITE_PAWN
      ],
      [
        WHITE_ROOK,
        WHITE_KNIGHT,
        WHITE_BISHOP,
        WHITE_QUEEN,
        WHITE_KING,
        WHITE_BISHOP,
        WHITE_KNIGHT,
        WHITE_ROOK
      ],
    ]
  return board

def renderTable(matrix: 'list[list[int]]', reverse: bool = False):
  table = '┌───┬───┬───┬───┬───┬───┬───┬───┐'
  for j in range(len(matrix), 0, -1):
    table += '\n' + str(j)
    for i in range(0, 8):
      table += ' ' + convertPiece(matrix[8 - j][i]) + ' │'
    if j == 1:
      break
    table += '\n├───┼───┼───┼───┼───┼───┼───┼───┤'
  table += '\n└─A─┴─B─┴─C─┴─D─┴─E─┴─F─┴─G─┴─H─┘'
  return renderReference() + '\n' + table

def renderReference():
  return "\u265A Rei \n\u265B Rainha \n\u265C Torre \n\u265D Bispo \n\u265E Cavalo \n\u265F Peão"

def convertPiece(code: int):
  if code == WHITE_KING:
    return '\u2654'
  if code == WHITE_QUEEN:
    return '\u2655'
  if code == WHITE_ROOK:
    return '\u2656'
  if code == WHITE_BISHOP:
    return '\u2657'
  if code == WHITE_KNIGHT:
    return '\u2658'
  if code == WHITE_PAWN:
    return '\u2659'
  if code == BLACK_KING:
    return '\u265A'
  if code == BLACK_QUEEN:
    return '\u265B'
  if code == BLACK_ROOK:
    return '\u265C'
  if code == BLACK_BISHOP:
    return '\u265D'
  if code == BLACK_KNIGHT:
    return '\u265E'
  if code == BLACK_PAWN:
    return '\u265F'
  return ' '

def getMove():
  while True:
    play = input("Sua jogada: ")
    try:
      play = play.replace(" ", "")
      source, destination = play.split(',')
      if len(source) == 2 and len(destination) == 2:
        if (
          int(source[1]) == 1 or int(source[1]) == 2 or int(source[1]) == 3
          or int(source[1]) == 4 or int(source[1]) == 5 or int(source[1]) == 6
          or int(source[1]) == 7 or int(source[1]) == 8
        ) and (
          int(destination[1]) == 1 or int(destination[1]) == 2
          or int(destination[1]) == 3 or int(destination[1]) == 4
          or int(destination[1]) == 5 or int(destination[1]) == 6
          or int(destination[1]) == 7 or int(destination[1]) == 8
        ) and (
          source[0].lower() == 'a' or source[0] == 'b'
          or source[0].lower() == 'c' or source[0].lower() == 'd'
          or source[0].lower() == 'e' or source[0].lower() == 'f'
          or source[0].lower() == 'g' or source[0].lower() == 'h'
        ) and (
          destination[0].lower() == 'a' or destination[0] == 'b'
          or destination[0].lower() == 'c' or destination[0].lower() == 'd'
          or destination[0].lower() == 'e' or destination[0].lower() == 'f'
          or destination[0].lower() == 'g' or destination[0].lower() == 'h'
        ):
          break
        else:
          print(howToPlay())
      else:
        print(howToPlay())
    except:
      print(howToPlay())
  return source, destination

def serverPlay(matrix: 'list[list[int]]', pieces: 'list[int]'):
  while True:
    source, destination = getMove()
    sourceRow, sourceCollumn = getCoordinates(source)
    piece = matrix[sourceRow][sourceCollumn]
    if piece != 0:
      destinationRow, destinationCollumn = getCoordinates(destination)
      if validateOwnership(piece, pieces):
        if validateMove(
          piece,
          [sourceRow,
           sourceCollumn],
          [destinationRow,
           destinationCollumn]
        ):
          if validatePath(
            matrix,
            [sourceRow,
             sourceCollumn],
            [destinationRow,
             destinationCollumn],
            pieces,
            piece
          ):
            matrix[sourceRow][sourceCollumn] = 0
            matrix[destinationRow][destinationCollumn] = piece
            break
        else:
          print("Você não pode mover essa peça ali!")
      else:
        print("Você não pode mover as peças do adversário! Escolha uma peça sua!")
    else:
      print("Não há nada nesse lugar! Escolha uma casa válida!")
  return matrix

def getCoordinates(position: str):
  if int(position[1]) == 1:
    row = 7
  elif int(position[1]) == 2:
    row = 6
  elif int(position[1]) == 3:
    row = 5
  elif int(position[1]) == 4:
    row = 4
  elif int(position[1]) == 5:
    row = 3
  elif int(position[1]) == 6:
    row = 2
  elif int(position[1]) == 7:
    row = 1
  elif int(position[1]) == 8:
    row = 0
  else:
    row = 0
  if position[0] == 'a':
    collumn = 0
  elif position[0] == 'b':
    collumn = 1
  elif position[0] == 'c':
    collumn = 2
  elif position[0] == 'd':
    collumn = 3
  elif position[0] == 'e':
    collumn = 4
  elif position[0] == 'f':
    collumn = 5
  elif position[0] == 'g':
    collumn = 6
  else:
    collumn = 7
  return row, collumn

def validateOwnership(piece: int, pieces: 'list[int]'):
  if piece in pieces:
    return True
  return False

def validateMove(piece: int, source: 'list[int]', destination: 'list[int]', client: bool = False):
  x = destination[1] - source[1]
  y = source[0] - destination[0]
  if piece == WHITE_KING or piece == BLACK_KING:
    move = round(sqrt(x * x + y * y), 2)
    if move == 1.00 or move == 1.41:
      return True
    return False
  elif piece == WHITE_QUEEN or piece == BLACK_QUEEN:
    move = round(sqrt(x * x + y * y), 2)
    if (move % 1.00 == 0) or (round(move % 1.41) == 0):
      return True
    return False
  elif piece == WHITE_BISHOP or piece == BLACK_BISHOP:
    move = round(sqrt(x * x + y * y), 2)
    if (round(move % 1.41) == 0):
      return True
    return False
  elif piece == WHITE_KNIGHT or piece == BLACK_KNIGHT:
    move = round(sqrt(x * x + y * y), 2)
    if (round(move % 2.24) == 0):
      return True
    return False
  elif piece == WHITE_ROOK or piece == BLACK_ROOK:
    move = round(sqrt(x * x + y * y), 2)
    if (move % 1.00 == 0):
      return True
    return False
  elif piece == WHITE_PAWN or piece == BLACK_PAWN:
    move = round(sqrt(x * x + y * y), 2)
    if move == 1.00 or move == 2.00 or move == 1.41:
      if client:
        if y > 0:
          return True
      else:
        if y < 0:
          return True
      return False
    return False
  else:
    return False

def validatePath(
  matrix: 'list[list[int]]',
  source: 'list[int]',
  destination: 'list[int]',
  pieces: 'list[int]',
  piece: int,
  client = False
):
  x = destination[1] - source[1]
  y = source[0] - destination[0]
  move = round(sqrt(x * x + y * y), 2)
  if piece == WHITE_KING or piece == BLACK_KING:
    if matrix[destination[0]][destination[1]] in pieces:
      print("Você não pode comer suas próprias peças!")
      return False
    return True
  if piece == WHITE_KNIGHT or piece == BLACK_KNIGHT:
    if matrix[destination[0]][destination[1]] in pieces:
      print("Você não pode comer suas próprias peças!")
      return False
    return True
  if piece == WHITE_ROOK or piece == BLACK_ROOK:
    distance = round(move / 1.00)
    if distance == 1:
      if matrix[destination[0]][destination[1]] in pieces:
        print("Você não pode comer suas próprias peças!")
        return False
      return True
    if x == 0:
      if y > 0:
        source[0] -= 1
        if matrix[source[0]][source[1]]:
          print("Tem uma peça bloquendo o caminho!")
          return False
        return validatePath(matrix, source, destination, pieces, piece)
      if y < 0:
        source[0] += 1
        if matrix[source[0]][source[1]]:
          print("Tem uma peça bloquendo o caminho!")
          return False
        return validatePath(matrix, source, destination, pieces, piece)
      return True
    if y == 0:
      if x > 0:
        source[1] += 1
        if matrix[source[0]][source[1]]:
          print("Tem uma peça bloquendo o caminho!")
          return False
        return validatePath(matrix, source, destination, pieces, piece)
      if x < 0:
        source[1] -= 1
        if matrix[source[0]][source[1]]:
          print("Tem uma peça bloquendo o caminho!")
          return False
        return validatePath(matrix, source, destination, pieces, piece)
      return True
    return True
  if piece == WHITE_BISHOP or piece == BLACK_BISHOP:
    distance = round(move / 1.41)
    if distance == 1:
      if matrix[destination[0]][destination[1]] in pieces:
        print("Você não pode comer suas próprias peças!")
        return False
      return True
    if x > 0 and y > 0:
      source[1] += 1
      source[0] -= 1
      if matrix[source[0]][source[1]]:
        print("Tem uma peça bloquendo o caminho!")
        return False
      return validatePath(matrix, source, destination, pieces, piece)
    if x < 0 and y > 0:
      source[1] -= 1
      source[0] -= 1
      if matrix[source[0]][source[1]]:
        print("Tem uma peça bloquendo o caminho!")
        return False
      return validatePath(matrix, source, destination, pieces, piece)
    if x < 0 and y < 0:
      source[1] -= 1
      source[0] += 1
      if matrix[source[0]][source[1]]:
        print("Tem uma peça bloquendo o caminho!")
        return False
      return validatePath(matrix, source, destination, pieces, piece)
    if x > 0 and y < 0:
      source[1] += 1
      source[0] += 1
      if matrix[source[0]][source[1]]:
        print("Tem uma peça bloquendo o caminho!")
        return False
      return validatePath(matrix, source, destination, pieces, piece)
    return True
  if piece == WHITE_QUEEN or piece == BLACK_QUEEN:
    if round(move % 1.00) == 0:
      distance = round(move / 1.00)
      if distance == 1:
        if matrix[destination[0]][destination[1]] in pieces:
          print("Você não pode comer suas próprias peças!")
          return False
        return True
      if x == 0:
        if y > 0:
          source[0] -= 1
          if matrix[source[0]][source[1]]:
            print("Tem uma peça bloquendo o caminho!")
            return False
          return validatePath(matrix, source, destination, pieces, piece)
        if y < 0:
          source[0] += 1
          if matrix[source[0]][source[1]]:
            print("Tem uma peça bloquendo o caminho!")
            return False
          return validatePath(matrix, source, destination, pieces, piece)
        return True
      if y == 0:
        if x > 0:
          source[1] += 1
          if matrix[source[0]][source[1]]:
            print("Tem uma peça bloquendo o caminho!")
            return False
          return validatePath(matrix, source, destination, pieces, piece)
        if x < 0:
          source[1] -= 1
          if matrix[source[0]][source[1]]:
            print("Tem uma peça bloquendo o caminho!")
            return False
          return validatePath(matrix, source, destination, pieces, piece)
        return True
    if round(move % 1.41) == 0:
      distance = round(move / 1.41)
      if distance == 1:
        if matrix[destination[0]][destination[1]] in pieces:
          print("Você não pode comer suas próprias peças!")
          return False
        return True
      if x > 0 and y > 0:
        source[1] += 1
        source[0] -= 1
        if matrix[source[0]][source[1]]:
          print("Tem uma peça bloquendo o caminho!")
          return False
        return validatePath(matrix, source, destination, pieces, piece)
      if x < 0 and y > 0:
        source[1] -= 1
        source[0] -= 1
        if matrix[source[0]][source[1]]:
          print("Tem uma peça bloquendo o caminho!")
          return False
        return validatePath(matrix, source, destination, pieces, piece)
      if x < 0 and y < 0:
        source[1] -= 1
        source[0] += 1
        if matrix[source[0]][source[1]]:
          print("Tem uma peça bloquendo o caminho!")
          return False
        return validatePath(matrix, source, destination, pieces, piece)
      if x > 0 and y < 0:
        source[1] += 1
        source[0] += 1
        if matrix[source[0]][source[1]]:
          print("Tem uma peça bloquendo o caminho!")
          return False
        return validatePath(matrix, source, destination, pieces, piece)
      return True
    return False
  if piece == WHITE_PAWN or piece == BLACK_PAWN:
    if x == 0:
      print(round(move / 1.00))
      if round(move / 1.00) == 1:
        if matrix[destination[0]][destination[1]] in pieces:
          print("Você não pode comer suas próprias peças!")
          return False
        return True
      elif round(move / 1.00) == 2:
        if client and source[0] == 7:
          source[0] -= 1
          return validatePath(matrix, source, destination, pieces, piece)
        elif (not client) and source[0] == 1:
          source[0] += 1
          return validatePath(matrix, source, destination, pieces, piece)
        print("Você só pode andar duas casas no primeiro movimento!")
        return False
      return False
    if matrix[destination[0]][destination[1]] in pieces:
      print("Você não pode comer suas próprias peças!")
      return False
    if matrix[destination[0]][destination[1]] == 0:
      print("Você só pode mover ali se tiver alguma peça do adversário!")
      return False
    return True
  return False