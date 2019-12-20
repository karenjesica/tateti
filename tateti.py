import random

def comenzar_partida():
    try:
        print("Comenzar a jugar \n")
        primera_vez = True
        quien_comienza(primera_vez)
    except Exception as e:
        print(e)

def quien_comienza(primera_vez):
    try:
        tablero = " "*10
        if random.randint(0, 1) == 0:
            pers = False
        else:
            pers = True

    except Exception as e:
        print(e)
  
  if __name__ == "__main__":
    comenzar_partida()


