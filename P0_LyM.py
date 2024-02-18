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


    if (lista[0] == "move"):
        casillas = lista[1]
        movimiento(casillas)
        return dentro()
    if (lista[0]== "="):
        variables[lista[1]]= lista[2]

    if (lista[1]== "skip"):
        movimiento(lista[1])
        esta =dentro()
    
    if (lista[0]== "turn"):
        if lista[1].lower() == "left":
                if vista == "N":
                      vista = "W"
                elif vista == "W":
                      vista = "S"  
                elif vista == "S":
                      vista = "E" 
                elif vista == "E":
                      vista = "N" 
        elif lista[1].lower() == "right":
           
                if vista == "N":
                      vista = "E"
                elif vista == "E":
                      vista = "S"  
                elif vista == "S":
                      vista = "W" 
                elif vista =="W":
                      vista = "N"
        elif lista[1].lower() == "around":
           
                if vista == "N":
                      vista = "S"
                elif vista == "E":
                      vista = "W"  
                elif vista == "S":
                      vista = "N" 
                elif vista =="W":
                      vista = "E"
    if lista[0]== "face":
        if lista[1] == "north":
                      vista = "N"
        elif lista[1] == "east":
                      vista = "E"  
        elif lista[1] == "west":
                     vista = "W" 
        elif lista[1] =="south":
                      vista = "S"
    if lista[0].lower() == "put":
            soltar = lista[1].lower().replace(":","")
            if soltar == "ballons":
                try:
                       myBalloons -= variables[lista[2]]
                except:
                       myBalloons -= lista[2]
            elif soltar =="chips":
                try:
                       myChips -= variables[lista[2]]
                except:
                       myChips -= lista[2]
                   
    if lista[0].lower() == "pick":
            soltar = lista[1].lower().replace(":","")
            if soltar == "ballons":
                try:
                       myBalloons += variables[lista[2]]
                except:
                       myBalloons += lista[2]
            elif soltar =="chips":
                try:
                       myChips += variables[lista[2]]
                except:
                       myChips += lista[2] 
    if lista[0].lower() == "move-dir":
        try:
            numero = variables[lista[2]]
        except:
            numero = lista[2]

        if lista[1].lower().replace(":","") == "front":
           movimiento(numero)

        elif lista[1].lower().replace(":","")== "right":
            vista = "left"  

        elif lista[1].lower().replace(":","") == "back ":
             myXpos -= int(numero)
        elif lista[1].lower().replace(":","") =="left":
                      vista = "S"
                    
def movimiento(casillas):
    if vista == "W":
            myXpos -= int(casillas)
    elif vista == "N":
            myYpos -= int(casillas)
    elif vista == "S":
                myYpos += int(casillas)
    elif vista == "E":
                myYpos += int(casillas)


def dentro():

    
    if (myXpos > 0) and (myXpos <= dimx) and (myYpos >0)and (myYpos <= dimy):
            return True
    else:
            return False


