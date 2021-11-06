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
VACIO = '-'


def comenzar():
    return input('Ingrese "Y" para jugar 4 en linea\n\t=> ') in ['y', 'Y']

# comenzar = lambda: input('Ingrese "Y" para jugar 4 en linea\n\t=> ') in ['y', 'Y']

######################################## LOGICA DE JUEGO ########################################


def inicializarTablero():
    return [[VACIO] * 7 for i in range(6)]


def mostrar_tablero(tabla):
    for i in tabla:
        print()
        for j in i:
            print(' %s ' % j, end='')


def posicion_vacia(tablero, columna):
    """Consulta si la ultima posicion de la columna esta ocupada."""
    return tablero[0][columna] == VACIO if columna < 7 else False


def posicion_en_fila_ocupado(tablero, fila, columna):
    """Verifica si la [fila][columna] esta ocupada, 
        si no lo esta retorna fila,
        sino se repite funcion hasta la siguiente fila desocupada. 
        Se usa RECURSIVIDAD"""

    return fila if tablero[fila][columna] == VACIO else posicion_en_fila_ocupado(tablero, fila-1, columna)


def ficha_en_tablero(tablero, fila, columna, ficha):
    """Añade ficha en tablero."""
    tablero[fila][columna] = ficha


def hubo_ganador(tablero, j1, j2):
    """Verifica si el jugador junto las 4 fichas en diagonal, vertical o horizontal.
        Si las junto es GANADOR.
        Caso contrario, sigue jugando. """
    filas, columnas = len(tablero), len(tablero[0])
    hubo_ganador = False

    # Recorriendo el tablero
    for f in range(filas):
        for c in range(columnas):
            # Si la posicion del tablero es igual a la ficha de un jugador, tomaremos esa ficha y realizaremos las verificaciones
            if tablero[f][c] == j1[1] or tablero[f][c] == j2[1]:
                fichaX = tablero[f][c]

                if (
                    # Diagonales
                    fichaX == tablero[f-1][c-1] == tablero[f-2][c-2] == tablero[f-3][c-3] or
                    # Horizontales
                    fichaX == tablero[f][c-1] == tablero[f][c-2] == tablero[f][c-3] or
                    # Verticales
                    fichaX == tablero[f-1][c] == tablero[f-2][c] == tablero[f-3][c]
                ):
                    # Cualquiera de las igualdades verificara que hubo ganador y no sera necesario seguir recorriendo el tablero
                    hubo_ganador = True
                    break
    return hubo_ganador


def registrar_jugadores():
    print("Jugador 1\n")
    jugador1 = (input("Ingrese nombre:\n"),
                input("Con que caracter jugara?\n"))
    print("Jugador 2\n")
    jugador2 = (input("Ingrese nombre:\n"),
                input("Con que caracter jugara?\n"))
    while jugador1[0] == jugador2[0]:
        jugador2 = (input("Seleccione un nombre diferente al del jugador 1\n"), jugador2[0])
    while jugador1[1] == jugador2[1]:
        jugador2 = (jugador2[0], input("Seleccione un caracter diferente al del jugador 1\n"))

    print(
        f"{jugador1[0]} jugarás con {jugador1[1]}, {jugador2[0]} jugarás con {jugador2[1]}")
    return jugador1, jugador2


def siguiente_turno(turno_actual):
    """
    Alterna entre los turnos de los jugadores
    """
    return 0 if turno_actual else 1

def validar_columna_jugada(columna, maximo_columnas):
  """
    Validara si el usuario ingreso un valor del rango correcto, devuelve la posicion de la columna
  """
  while columna not in map(lambda n: str(n), range(maximo_columnas+1)):
    columna = input("Ingrese una opcion valida (1-7)\n\t=> ")
  else:
    columna = int(columna)
    columna -= 1
    return columna


def partida(tablero):
    print("\n\n========== EMPIEZA PARTIDA ==========")
    j1, j2 = registrar_jugadores()

    jugadores = {
      0: { 'nombre':j1[0], 'ficha': j1[1] },
      1: { 'nombre':j2[0], 'ficha': j2[1] }
    }

    cantidad_columnas = len(tablero[0])
    turno = 1

    while not hubo_ganador(tablero, j1, j2):
        turno = siguiente_turno(turno)
        fila = FILA-1
        columna = validar_columna_jugada(
            input(f"\nJUGADOR {jugadores.get(turno).get('nombre')}, ingrese su jugada (1-7): "),
            cantidad_columnas
        )

        if posicion_vacia(tablero, columna):
            fila = posicion_en_fila_ocupado(tablero, fila, columna)
            ficha_en_tablero(tablero, fila, columna, ficha=jugadores.get(turno).get('ficha'))
            mostrar_tablero(tablero)
        else:
            print("\nINGRESE VALOR VALIDO")
            # Al ingresar un valor invalido, no se jugo ficha, entonces forzamos el alternado de turno para que vuelva a jugar el mismo jugador, solo en este caso
            turno = siguiente_turno(turno)
    else:
      print("\n\n========== GAME OVER ==========\n")
      print(f"JUGADOR {turno+1} ES EL GANADOR DE LA PARTIDA: {jugadores.get(turno).get('nombre')}!")
      print("\n========== ========= ==========\n")

    # -----------SI LES PARECE , ACA PUEDE GUARDAR GANADOR EN ARCHIVOS-----------

    # Logica para volver a jugar
    return menu() if input('Ingrese Y para volver a jugar\n\t=>') in ['Y', 'y'] else print('Gracias por jugar!')

######################################## OPCIONES DE MENU ########################################


def jugar():
    tablero = inicializarTablero()

    mostrar_tablero(tablero)
    partida(tablero)


def instrucciones():
    try:
        with open("/home/marian/Documentos/WebCampus/Programacion1/Instrucciones.txt", "r") as arch:
            for l in arch:
                print("\n", l, end="   ")
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    opcion = input(
        '\nPresione una tecla para volver al menu o 0 para salir... ')
    if opcion == "0":
        despedir()
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


def despedir():
    print("GRACIAS POR ENTRAR A NUESTRO FABULOSO JUEGO")
    input("Presione una tecla para salir...")
    return False


######################################## FUNCION MANU ########################################

def menu():
    print("========== Menu ==========")
    print("1- JUGAR")
    print("2- INSTRUCCIONES")
    print("3- RANKING")
    print("4- SALIR")

    opcion = input("Ingrese opcion: ")
    while opcion not in map(lambda x: str(x), range(1, 5)):
        print('Opcion incorrecta.')
        opcion = input("Ingrese opcion válida:\n\t=> ")

    # acciones es un diccionario que guarda la referencia a funciones del programa
    acciones = {
        '1': jugar,
        '2': instrucciones,
        '3': ranking,
        '4': despedir
    }

    # Obtengo la funcion guardada en el diccionario y la asigno a una variable
    accion = acciones.get(opcion)

    # Ejecuto mi nueva variable que hace referencia a una funcion
    # Esto retornara falso solo al elegir "salir" (4)
    return accion()
 
    
    """
    # Alternativo
    # Ejecutar directamente accediendo mediante la KEY de opcion
    # Entiendo que accediendo al valor del diccionario recibire la referencia a la funcion, entonces podre ejecutarla

    return acciones[opcion]()
    """


    

######################################## PROGRAMA PRINCIPAL ########################################
print()
print('Bienvenido a nuestro juego!'.upper())
while comenzar():
    # Menu arrojara Falso solo al salir del juego
    if not menu():
        break
else:
    despedir()
