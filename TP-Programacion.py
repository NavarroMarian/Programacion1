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

def inicializarTablero () :
    return [['?'] * 7 for i in range(6)]
    
def mostrar_tablero(tabla):
    for i in tabla:
        print()
        for j in i:
            estado = 'vacio'
            print(' %s '% estado, end='')
    print()

def registrar_jugadores():
    print("Jugador 1\n")
    jugador1 = (input("Ingrese nombre:\n"),input("Con que caracter jugara?\n"))
    print("Jugador 2\n")
    jugador2 = (input("Ingrese nombre:\n"),input("Con que caracter jugara?\n"))
    while jugador2[1] == jugador1[1]:
        jugador2 = (jugador2[0],input("Seleccione un caracter diferente\n"))

    print(jugador1,jugador2)
    return jugador1,jugador2
    
def jugar():
    tablero = inicializarTablero()
    mostrar_tablero(tablero)
    j1,j2 = registrar_jugadores()    
    partida()
    
def partida():
    pass

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
    
def menu():    
    print("========== Menu ==========") 
    print("1- JUGAR")
    print("2- INSTRUCCIONES")
    print("3- RANKING")
    print("4- SALIR")

    opcion = input("Ingrese opcion:")
    while opcion.isnumeric() == False or opcion > "4" or opcion < "0": 
        opcion = (input("Ingrese opcion válida:"))    
        
    if opcion == '1':
        jugar()
    elif opcion == '2':
        instrucciones()
    elif opcion == '3':
        ranking()
    elif opcion == '4':
        salir()
    else:
        print('Ingrese una opcion correcta.')

def pedir_jugada(jugador_actual, tabla):
    """ 
    Sarasa
    """

    # jugador_actual determinaria el caracter a posicionar en la tabla (?)
    # tabla recibe el estado actual del tablero de juego

    """ 
    jugada = -1
    while jugada not in range(len(tabla[0])):
        print(f'Jugador  {jugador_actual}')
        jugada = input('Ingrese una columna para jugar')    
    
    invocar_jugada(jugada, tabla)
    """
    pass
    

#programa principal
# menu()
ranking()