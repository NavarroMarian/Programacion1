""" Cuatro en Linea

Archivos y Excepciones: Historial de Ganadores
Archivo : Ranking de Jugadores
Listas (Matriz) : Tablero 7x6
Diccionario: Datos de jugador (nombre y caracter para ficha).
Recursividad: En Ranking

Temas : Listas , Cadenas , Excepciones , Recursividad y Tuplas ,Conjuntos o Diccionarios.

VISUALIZACION DE TABLERO 
[[' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

"""

from typing import Collection


FILA = 6
COLUMNA = 7

######################################## LOGICA DE JUEGO ########################################

def inicializarTablero () :
    return [[0] * 7 for i in range(6)]
    
def mostrar_tablero(tabla):
    for i in tabla:
        print()
        for j in i:
            print(' %s '% j, end='')

def posicion_vacia(tablero,columna):
    """Consulta si la ultima posicion de la columna esta ocupada."""
    return tablero[0][columna] == 0 if columna < 7 else False


def posicion_en_fila_ocupado(tablero,fila,columna):
    """Verifica si la [fila][columna] esta ocupada, 
        si no lo esta retorna fila,
        sino se repite funcion hasta la siguiente fila desocupada. 
        Se usa RECURSIVIDAD"""

    return fila if tablero[fila][columna] is 0 else posicion_en_fila_ocupado(tablero,fila-1,columna)

def ficha_en_tablero(tablero,fila, columna, ficha):
    """Añade ficha en tablero."""
    tablero[fila][columna] = ficha


def sera_o_no_sera_ganador(tablero,j1,j2):
    """Verifica si el jugador junto las 4 fichas en diagonal, vertical o horizontal.
        Si las junto es GANADOR.
        Caso contrario, sigue jugando. """
    filas = len(tablero)
    columnas = len(tablero[0])
    for f in range(filas):
        for c in range(columnas):
            if tablero[f][c] == j1[1] or tablero[f][c] == j2[1]:
                fichaX = tablero[f][c]
                if fichaX == tablero[f-1][c-1] and fichaX == tablero[f-2][c-2] and fichaX == tablero[f-3][c-3]:#SE REVISA DIAGONALES
                    print("GANADOR DEL NADA PERO GANADOR AL FIN")
                    return True
                elif fichaX == tablero[f][c-1] and fichaX == tablero[f][c-2] and fichaX == tablero[f][c-3]:#SE REVISA HORIZONTALES
                    print("GANADOR DE NADA PERO GANADOR AL FIN")
                    return True
                elif fichaX == tablero[f-1][c] and fichaX == tablero[f-2][c] and fichaX == tablero[f-3][c]:#SE REVISA VERTICALES
                    print("GANADOR DE NADA PERO GANADOR AL FIN")
                    return True
            
    return False

def registrar_jugadores():
    print("Jugador 1\n")
    jugador1 = (input("Ingrese nombre:\n"),input("Con que caracter jugara?\n"))
    print("Jugador 2\n")
    jugador2 = (input("Ingrese nombre:\n"),input("Con que caracter jugara?\n"))
    while jugador2[1] == jugador1[1]:
        jugador2 = (jugador2[0],input("Seleccione un caracter diferente\n"))

    print(f"{jugador1[0]} jugarás con {jugador1[1]}, {jugador2[0]} jugarás con {jugador2[1]}")
    return jugador1,jugador2
   
    
def partida(tablero):
    print("\n\n========== EMPIEZA PARTIDA ==========")
    j1,j2 = registrar_jugadores()
    partida_finalizada , turno= False ,0

    while not partida_finalizada:
        fila=FILA-1

        if turno == 0:
            columna = int(input("\nJUGADOR 1, ingrese su jugada (1-7): "))
            columna-=1
            if posicion_vacia(tablero,columna): 
                """Si posicion_vacia(tablero,columna) es True pide ingreso de ficha y la ubica donde esta desocupado,
                en caso de partida_finalizada = sera_o_nosera_ganador(tablero,j1,j2) ser True GANADOR y termina partida."""

                fila = posicion_en_fila_ocupado(tablero,fila,columna) 
                ficha_en_tablero(tablero,fila, columna, ficha=j1[1])
                mostrar_tablero(tablero)
                partida_finalizada = sera_o_no_sera_ganador(tablero,j1,j2) 
                turno=1 
            else:
                """Si posicion_vacia(tablero,columna) es False viene aca y se vuelve a solicitar que ingrese columna nuevamente"""
                turno = 0
                print("\nNO EXISTE LA COLUMNA ", columna, ". INGRESE UN VALOR CORRECTO") 
                
        else:
            columna = int(input("\nJUGADOR 2, ingrese su jugada (1-7): "))
            columna-=1
            if posicion_vacia(tablero,columna): 
                fila = posicion_en_fila_ocupado(tablero,fila,columna)
                ficha_en_tablero(tablero,fila, columna, ficha=j2[1])
                mostrar_tablero(tablero)
                partida_finalizada = sera_o_no_sera_ganador(tablero,j1,j2)
                turno = 0
            else:
                turno = 1
                print("\nNO EXISTE LA COLUMNA ", columna, ".INGRESE UN VALOR CORRECTO.")

        print("\n\n========== GAME OVER ==========")
        print("\n\n GANADOR DE PARTIDA:", j2[0] if turno == 0 else j1[0])
        #-----------SI LES PARECE , ACA PUEDE GUARDAR GANADOR EN ARCHIVOS-----------
    return menu()


######################################## OPCIONES DE MENU ########################################

def jugar(tablero):
    mostrar_tablero(tablero)
    partida(tablero)

def instrucciones():
    try:
        with open("/home/marian/Documentos/WebCampus/Programacion1/Instrucciones.txt","r") as arch:
            for l in arch:
                print("\n",l,end="   ")
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close( )
        except NameError:
            pass
    opcion = input('\nPresione una tecla para volver al menu o 0 para salir... ')
    if opcion == "0":
        salir()
    else:
        menu()

def ranking():
    print("\n\n==========RANKING==========") 
    d = {}
    with open("/home/marian/Documentos/WebCampus/Programacion1/ganadores_historico.txt", "r") as f:
        for linea in f:
            (key, val) = linea.split()
            d[int(key)] = val
    print(d)

    # with open("/Users/cmaio/Desktop/ganadores.txt","r") as archivo:
    #     for linea in archivo:
    #         print("\n",linea,end="   ")

    # if ganador:
    #     with open('/home/marian/Documentos/WebCampus/Programacion1/ganadores_historico.txt', 'a') as f:
    #         f.write(jugador_ganador)
    #         f.write("\n")
    #         f.close()
    #     with open('/home/marian/Documentos/WebCampus/Programacion1/ganadores_historico.txt', 'r') as f:
    #         for players in f:
    #             print("\n",players,end="   ")

def mostrarArchivo(archivo):
    pass


def salir():
    print("GRACIAS POR ENTRAR A NUESTRO FABULOSO JUEGO")
    input("Presione una tecla para salir...")
    

######################################## FUNCION MANU ########################################
    
def menu():    
    print("========== Menu ==========") 
    print("1- JUGAR")
    print("2- INSTRUCCIONES")
    print("3- RANKING")
    print("4- SALIR")

    opcion = input("Ingrese opcion: ")
    while opcion.isnumeric() == False or opcion > "4" or opcion < "0": 
        opcion = (input("Ingrese opcion válida: "))    
        
    if opcion == '1':
        jugar(tablero)
    elif opcion == '2':
        instrucciones()
    elif opcion == '3':
        ranking()
    elif opcion == '4':
        salir()

######################################## PROGRAMA PRINCIPAL ########################################
tablero = inicializarTablero()
menu()



# Hola! Probando 1, 2, 3, 1, 2, 3