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
    """Elije a un jugador aleatoriamente (persona o computadora) para que
    comience a jugar y le asigna True.

    Devuelve:
    pers(bool): true(comienza la persona) - false(comienza la computadora)
    """
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
        """Selecciona al jugador segun su turno.

        Parametros:
        tablero(list): posicion del tablero.
        pers(bool): true(juega la persona) - false(juega la maquina)
        primera_vez(bool): true(tablero vacio)

        Devuelve:
        response(int): nro de jugada
        """
        if pers:    
            print("turno de persona")

            jugada = turno_jugador(tablero)
            response = jugada
        
        else:
            print("turno de maquina")

            response = turno_maquina(tablero)

        nueva_jugada(response, tablero, pers, primera_vez)
    except Exception as e:
        print(e)

def turno_jugador(tablero):
    """ El jugador elije un numero del 1 al 10
    
    Parametro: 
    tablero(list): posicion del tablero.

    Devuelve: nro(1 al 10)
    """
    jugada = input('Elegir numero (1 a 9): ')
            
    invalido = posicion_invalida(jugada)
    if not invalido:
        jugada = input('Elegir un numero entre 1 y 9: ')

    while not jugada or tablero[int(jugada)-1] != " ":
        jugada = input('Debe elegir un numero sin ocupar(1 a 9): ')

    return jugada

def turno_maquina(tablero):
    """ La computadora elije un numero random
    
    Parametro: 
    tablero(list): posicion del tablero.

    Devuelve: nro(1 al 10)
    """
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

        response = verificar_ganador(tablero, jugador)
        response_lleno = tablero_lleno(tablero)
        if response or not response_lleno:
            jugar = input("Juego terminado. \nContinuar? (s): ")
            if jugar == "s":
                comenzar_partida()
        
        if not primera_vez:
            if pers:
                pers = False
            else: 
                pers = True

        mostrar_tablero(primera_vez, pers, tablero)
    except Exception as e:
        print(e)

def posicion_invalida(jugada):
    """ Verifica que los numeros ingresados sean solo del 1 al 9
    
    Parametro: 
    jugada(int): numero ingresado.

    Devuelve: response(bool): true(nro del 1-9) - false(nro invalido) 
    """
    try:
        posiciones = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if jugada not in posiciones:
            response = False
        else:
            response = True
        return response 
    except Exception as e:
        print(e)
    
def tablero_lleno(tablero):
    """Valida que el tablero no se haya quedado sin movimientos.

    Parametros: 
    tablero(list): posicion del tablero.

    Devuelve:
    response(bool): true(tablero vacio) - false(tablero disponible)
    """
    for i in tablero:
        if i == "":
            response = False
        else: response = True
    return response

    
def verificar_ganador(t, j):
    """Verifica todas las opciones que hagan ganar a un jugador

    Parametros:
    t(list): posicion del tablero
    j(str): jugador "O"(persona) - "X"(computadora)

    Devuelve:
    response(bool): true(linea ganadora) - false(ninguna linea)
    """
    try:
        if t[6] == j and t[7] == j and t[8] == j or\
        t[3] == j and t[4] == j and t[5] == j or\
        t[0] == j and t[1] == j and t[2] == j or\
        t[6] == j and t[3] == j and t[0] == j or\
        t[7] == j and t[4] == j and t[1] == j or\
        t[8] == j and t[5] == j and t[2] == j or\
        t[6] == j and t[4] == j and t[2] == j or\
        t[8] == j and t[4] == j and t[0] == j:
            print("{} ha ganado".format(j))
            response = True
        else:
            response = False
        return response
    except Exception as e:
        print(e)


if __name__ == "__main__":
    comenzar_partida()


