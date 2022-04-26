##########################################
#                                        #
#  Programe sus funciones aquí           #
#                                        #
##########################################



from typing import ClassVar


def disparo(tablero, barcos, fila, columna):
    filan=int(fila)
    for i in barcos:
        Lbarco=i[0]
        Fbarco=i[2]
        Cbarco=i[3]
        if i[1]==2:
            if Fbarco == fila: 
                if columna in list(range(Cbarco,Cbarco+Lbarco)):
                    tablero[fila][columna]="O" 
                    return
                else:
                    tablero[fila][columna]=" "
            else:
                tablero[fila][columna]=" "
        elif i[1]==1:
            if Cbarco == columna: 
                if fila in list(range(Fbarco,Fbarco+Lbarco)):
                    tablero[fila][columna]="O" 
                    return
                else:
                    tablero[fila][columna]=" "
            else:
                tablero[fila][columna]=" "
    return

#BACK UP FUNCION DISPARO
'''
def disparo(tablero, barcos, fila, columna):
    filan=int(fila)
    for i in barcos:
        Lbarco=i[0]
        Fbarco=i[2]
        Cbarco=i[3]
        if Fbarco == fila and columna ==Cbarco: 
            tablero[fila][columna]="O" 
            return
        else:
            tablero[fila][columna]=" "

    return
'''


        
    # Desarrolle aquí su código para la función


def destruidos(tablero, barcos):
    n=0
    for barco in barcos:
        cuerpo=0
        cont=0
        pi=0
        muerto=False
        Bfila=barco[2]
        Bcolumna=barco[3]
        Blargo=range(barco[0])
        while cont<barco[0]:
            if barco[1]==1:
                if tablero[Bfila+cont][Bcolumna] == 'O':
                    cuerpo+=1
                    cont+=1
                elif tablero[Bfila+cont][Bcolumna]!= 'O':
                    cont+=1
                if cuerpo== barco[0]:
                    muerto=True
            elif barco[1] == 2:
                if tablero[Bfila][Bcolumna+cont] == 'O':
                    cuerpo+=1
                    cont+=1
                elif tablero[Bfila][Bcolumna+cont]!= 'O':
                    cont+=1
                if cuerpo== barco[0]:
                    muerto=True
        if muerto==True:
            if barco[1]==1:
                while pi<barco[0]:
                    tablero[Bfila+pi][Bcolumna] = "X"
                    pi+=1
            elif barco[1]==2:
                while pi<barco[0]:
                    tablero[Bfila][Bcolumna+pi] = "X"
                    pi+=1
        if "X" in tablero [Bfila][Bcolumna]:
            n+=1
    return n

#BACK UP FUNCION DESTRUIDOS
'''
def destruidos(tablero, barcos):
    n=0
    for barco in barcos:
        cuerpo=0
        cont=0
        pi=0
        muerto=False
        Bfila=barco[2]
        Bcolumna=barco[3]
        Blargo=range(barco[0])
        while cont<barco[0]:
            if tablero[Bfila+cont][Bcolumna] == 'O':
                cuerpo+=1
                cont+=1
            elif tablero[Bfila+cont][Bcolumna]!= 'O':
                cont+=1
            if cuerpo== barco[0]:
                muerto=True
        if muerto==True:
            while pi<barco[0]:
                tablero[Bfila+pi][Bcolumna] = "X"
                pi+=1
            n+=1
    return n

'''

    # Desarrolle aquí su código para la función








# OPCIONAL:
# Cambie el valor de esta variable a 1 si desea ver
# la ubicación de los barcos antes de comenzar.
# Esto puede ser útil para probar sus funciones.
mostrar_solucion = 1





##################################################
#                                                #
#  NO MODIFIQUE EL CÓDIGO A PARTIR DE ESTE PUNTO #
#                                                #
##################################################

import random as rd

# Función que muestra el tablero con el formato deseado para la pantalla
def show(tablero):
    print("\n  123456789")
    for i in range(9):
        fila_texto = " "
        for j in tablero[i]:
            fila_texto += str(j)
        print(chr(65+i)+fila_texto)

# Creación del tablero (inicialmente únicamente con "-" en todas las posiciones)
tablero = []
board = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append("-")
    tablero.append(fila)
    board.append(list(fila))

# Creación de los barcos con orientación y posición aleatorias
barcos = []
length = [2,3,3,4,5]
for i in range(5):
    l = length[i]
    orientation = rd.randint(1,2)
    if orientation == 1:
        flag = True
        while flag:
            row = rd.randint(0,9-l)
            column = rd.randint(0,8)
            empty = True
            for j in range(l):
                empty = empty and board[row+j][column] != "X"
            if empty:
                flag = False
        for j in range(l): board[row+j][column] = "X"
    else:
        flag = True
        while flag:
            row = rd.randint(0,8)
            column = rd.randint(0,9-l)
            if "X" not in board[row][column:column+l]:
                flag = False
        for j in range(l): board[row][column+j] = "X"
    barcos.append([l,orientation,row,column])
print(barcos)
# Se muestra la solución al inicio en caso de que se haya seleccionado esta opción
if mostrar_solucion == 1:
    print("Solución:")
    show(board)
    print("\n\n")

# Ciclo principal del programa donde se reciben los disparos, se validan y se llama a la función disparo()
print("¡Bienvenido a Solitary Battleship!")
destroyed = 0
while destroyed < 5:
    not_valid = True
    while not_valid:
        turn = input("\n¿Que casilla desea disparar? (Ejemplo: A1): ")
        not_valid = False
        if len(turn) != 2:
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("A" <= turn[0] and turn[0] <= "I"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("1" <= turn[1] and turn[1] <= "9"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        else:
            fila = "ABCDEFGHI".index(turn[0])
            columna = int(turn[1])-1
            if tablero[fila][columna] != "-":
                not_valid = True
                print("Ya ha disparado a esta casilla.")
    disparo(tablero, barcos, fila, columna)
    destroyed = destruidos(tablero, barcos)
    show(tablero)
    print("\n"+str(destroyed)+" barcos destruidos.")
    # Fin del juego
    if destroyed == 5:
        print("Felicidades, juego terminado.")
