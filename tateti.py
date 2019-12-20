import random
from random import randrange

def comenzar_partida():
    try:
        print("Comenzar a jugar \n")
        primera_vez = True
        pers = quien_comienza()
        mostrar_tablero(primera_vez, pers, tablero = " "*10)
    except Exception as e:
        print(e)

def quien_comienza():
    try:
        
        if random.randint(0, 1) == 0:
            pers = False
        else:
            pers = True
        
        return pers
    except Exception as e:
        print(e)

def mostrar_tablero(primera_vez, pers, tablero):
    try:
        linea_vertical = "                      |                            |"
        linea_punteada = '---------------------------------------------------------------------'

        print(linea_vertical)
        print(linea_vertical)
        print('7-        ' + tablero[6] + '           | 8-           ' + tablero[7] + '             | 9-           ' + tablero[8])
        print(linea_punteada)
        print(linea_vertical)
        print('4-        ' + tablero[3] + '           | 5-           ' + tablero[4] + '             | 6-           ' + tablero[5])
        print(linea_vertical)
        print(linea_punteada)
        print('1-        ' + tablero[0] + '           | 2-           ' + tablero[1] + '             | 3-           ' + tablero[2])
        print(linea_vertical)
        print(linea_vertical)

        elegir_opcion(tablero, pers, primera_vez)
        
    except Exception as e:
        print(e)

def elegir_opcion(tablero, pers, primera_vez):
    try:
        if pers:    
            response = print("turno de persona")
            jugada = turno_jugador(tablero)
            response = jugada
        else:
            response = turno_maquina(tablero)

        nueva_jugada(response, tablero, pers, primera_vez)

        return response
    except Exception as e:
        print(e)

def turno_jugador(tablero):
    jugada = input('Elegir numero (1 a 9): ')
            
    invalido = posicion_invalida(jugada)
    if not invalido:
        jugada = input('Elegir un numero entre 1 y 9: ')

    while not jugada or tablero[int(jugada)-1] != " ":
        jugada = input('Debe elegir un numero sin ocupar(1 a 9): ')

    return jugada

def turno_maquina(tablero):
    response = randrange(10)
    while tablero[int(response)-1] != " ":
        response = randrange(10)
    
    return response

def nueva_jugada(jugada, tablero, pers, primera_vez):
    try:
        if primera_vez:
            tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            primera_vez = False
        
        if pers:
            jugador = "X"
        else:
            jugador = "O"

        tablero[int(jugada)-1] = jugador
        
        if not primera_vez:
            if pers:
                pers = False
            else: 
                pers = True

    except Exception as e:
        print(e)

def posicion_invalida(jugada):
    try:
        posiciones = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if jugada not in posiciones:
            response = False
        else:
            response = True
        return response 
    except Exception as e:
        print(e)

if __name__ == "__main__":
    comenzar_partida()


