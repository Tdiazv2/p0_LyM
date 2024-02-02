comandos = {"defvar": None, "move":None, "skip":None, "turn":None, "face":None, "put":None, "pick":None}

codigo = open("archivo", "r")
linea = codigo.readline()
while(linea!=""):
    linea = codigo.readline()
    
codigo.close()