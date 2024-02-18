defvarComandos = { "move":None, "skip":None, "turn":None, "face":None, "put":None, 
                      "pick":None, "rotate":None}
variables ={}
dimx = 0
dimy=0
myXpos = 1
myYpos = 1
myChips = 0
myBalloons = 0

Spaces = 0
vista = "E"

def lectura():

    
    codigo = open("archivo", "r")
    linea = codigo.readline()
    funciona = True
    ballonsHere = 0
    ChipsHere = 0
    while(linea!="" and funciona == True):
        linea = codigo.readline()
        linea.lower().replace("(", "").replace(")","")
        lista = linea.split(" ")
        if (lista[0] == "defvar"):
            defvar()
    
    codigo.close()

def defvar(lista):


    if (lista[1] == "move"):
        return dentro(lista[2])
    elif (lista[0]== "="):
        variables[lista[1]]= lista[2]

    elif (lista[1]== "skip"):
        esta =dentro(lista[2])
    
    elif (lista[1]== "turn"):
          
          
              
    
def dentro(casillas):

    if vista == "W":
            myXpos -= int(casillas)
    elif vista == "N":
            myYpos -= int(casillas)
    elif vista == "S":
            myYpos += int(casillas)
    elif vista == "E":
            myYpos += int(casillas)
    if (myXpos > 0) and (myXpos <= dimx) and (myYpos >0)and (myYpos <= dimy):
            return True
    else:
            return False


