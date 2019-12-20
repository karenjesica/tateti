import random

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

        elegir_opcion(pers)
        
    except Exception as e:
        print(e)

def elegir_opcion(pers):
    try:
        if pers:    
            response = print("turno de persona")
        else:
            response = print("turno de maquina")
        return response
    except Exception as e:
        print(e)


if __name__ == "__main__":
    comenzar_partida()


