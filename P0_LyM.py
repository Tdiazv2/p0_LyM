
def lectura():

    comandos = {"defvar": None, "move":None, "skip":None, "turn":None, "face":None, "put":None, "pick":None}

    Dim = 0
    myXpos = 0
    myYpos = 0
    myChips = 0
    myBalloons = 0
    ballonsHere = 0
    ChipsHere = 0
    Spaces = 0

    codigo = open("archivo", "r")
    linea = codigo.readline()
    funciona = True
    while(linea!="" and funciona == True):
        linea = codigo.readline()
    
    codigo.close()

def defvar(comando):
    comando.lower().replace("(", "").replace(")","")
    