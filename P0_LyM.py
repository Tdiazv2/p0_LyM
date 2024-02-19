defvarComandos = { "move":None, "skip":None, "turn":None, "face":None, "put":None, 
                      "pick":None, "rotate":None}
variables ={}
dimx = 0
dimy=0
myXpos = 1
myYpos = 1
myChips = 0
myBalloons = 0
funciona = True
Spaces = 0
vista = "E"

def lectura():

    
    codigo = open("archivo", "r")
    linea = codigo.readline()
    
    ballonsHere = 0
    ChipsHere = 0
    while(linea!="" and funciona == True):
        linea = codigo.readline()
        linea.lower().replace("(", "").replace(")","")
        lista = linea.split(" ")
        
        command(lista)
    
    codigo.close()
    if funciona:
        print("yes")
    else:
        print("no")

def command(lista):

    if lista[0].lower() == "defvar":
        if (lista[2].lower() == "dim" or lista[2].lower() == "myxpos" or lista[2].lower() == "myypos" or lista[2].lower() == "mychips" or lista[2].lower() == "myballoons" or lista[2].lower() == "balloonshere" or lista[2].lower() == "chipshere" or lista[2].lower() == "spaces" or int(lista[2]) == int):
            
            variables[lista[1]] = lista[2]
        else:
            funciona = False
        
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
           return dentro()

        elif lista[1].lower().replace(":","")== "right":
            if vista == "W":
                myYpos -= int(casillas)

                
            elif vista == "N":
                myXpos += int(casillas)
            elif vista == "S":
                myXpos -= int(casillas)
                        
            elif vista == "E":
                myYpos += int(casillas)

        elif lista[1].lower().replace(":","") == "back":
            if vista == "W":
                myXpos += int(casillas)

                

            
            elif vista == "N":
                myYpos += int(casillas)
            elif vista == "S":
                 myYpos -= int(casillas)
                
                        
            elif vista == "E":
                myXpos -= int(casillas)
           
        elif lista[1].lower().replace(":","") =="left":
            if vista == "W":
                myYpos += int(casillas)

                
            
            elif vista == "N":
                myXpos -= int(casillas)

                
            elif vista == "S":
                myXpos += int(casillas)
    
            elif vista == "E":
                myYpos -= int(casillas)
    if lista[0].lower() == "run-dirs":
        vistaAntes = vista
        for i in lista[1:len(lista) - 1]:
            vista = i
            movimiento(1)
        vista = vistaAntes 
    if lista[0].lower() == "move-face":
        vista = lista[2]
        if(int(lista[1]) is int):
            movimiento(int(lista[1]))
        elif(variables[lista[1]] is int):
            movimiento(variables[lista[1]])
    if lista[0].lower() == "if":
        if not (lista[1].lower() == "facing?" or lista[1].lower() == "blocked?" or lista[1].lower() == "can-put?" or lista[1].lower() == "can-pick?" or lista[1].lower() == "can-move?" or lista[1].lower() == "iszero()" or lista[1].lower() == "not"):
            funciona = False
            if not (lista[2].lower() == "facing?" or lista[2].lower() == "blocked?" or lista[2].lower() == "can-put?" or lista[2].lower() == "can-pick?" or lista[2].lower() == "can-move?" or lista[2].lower() == "iszero()" or lista[2].lower() == "not"):
                funciona = False
                
    if lista[0].lower() == "loop":
        if not (lista[1].lower() == "facing?" or lista[1].lower() == "blocked?" or lista[1].lower() == "can-put?" or lista[1].lower() == "can-pick?" or lista[1].lower() == "can-move?" or lista[1].lower() == "iszero()" or lista[1].lower() == "not"):
            funciona = False
        
    if lista[0].lower() == "repeat":
        if not (lista[1].lower() == "facing?" or lista[1].lower() == "blocked?" or lista[1].lower() == "can-put?" or lista[1].lower() == "can-pick?" or lista[1].lower() == "can-move?" or lista[1].lower() == "iszero()" or lista[1].lower() == "not"):
            funciona = False
                    
    if lista[0].lower() == "defun":
        variables[lista[2]] == "0"
        
def movimiento(casillas):
    if vista == "W":
            myXpos -= int(casillas)
    elif vista == "N":
            myYpos -= int(casillas)
    elif vista == "S":
                myYpos += int(casillas)
    elif vista == "E":
                myXpos += int(casillas)


def dentro():

    
    if (myXpos > 0) and (myXpos <= dimx) and (myYpos >0)and (myYpos <= dimy):
            return True
    else:
            return False


