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

######################################## LOGICA DE JUEGO ########################################


def inicializarTablero():
    return [[VACIO] * 7 for i in range(6)]


def mostrar_tablero(tabla):
    for i in tabla:
        print()
        for j in i:
            print(' %s ' % j, end='')
    print()


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


def conteo_vacios(tabla):
    espacios_vacios = 0
    for i in tabla:
        for j in i:
            if j == VACIO:
                espacios_vacios = espacios_vacios + 1

    return espacios_vacios


def verificar_espacios_tablero(tabla):
    """
        Devuelve si True o False en base a si el tablero proporcionado esta completo.
    """
    esta_completo = True

    for i in tabla:
        for j in i:
            if j == VACIO:
                esta_completo = False
                break

    return esta_completo


def hubo_ganador(tablero, j1, j2):
    """
        Verifica si el jugador junto las 4 fichas en diagonal, vertical o horizontal.
        Si las junto es GANADOR.
        Caso contrario, sigue jugando.
    """
    filas, columnas = len(tablero), len(tablero[0])
    hubo_ganador = False

    # Recorriendo el tablero
    for f in range(filas):
        for c in range(columnas):
            # Si la posicion del tablero es igual a la ficha de un jugador, tomaremos esa ficha y realizaremos las verificaciones
            if tablero[f][c] != VACIO:
                # fichaX es la jugada de algun jugador, tomaremos su posicion para pivotear con el.
                fichaX = tablero[f][c]

                # Cualquiera de las igualdades verificara que hubo ganador y no sera necesario seguir recorriendo el tablero
                # Ademas verificamos que no estamos comparando indices opuestos (ej: ganador con columnas  -1, 0, 1, 2)
                # La verificacion de igualdad la hacemos sustrayendo unidades al indice, por lo que la fila o columna debe ser siempre mayor a 3 para tener indices como minmo "3, 2, 1, 0"
                if (
                    # Verificacion de Diagonales
                    ((f> 2 and c > 2) and fichaX == tablero[f-1][c-1] == tablero[f-2][c-2] == tablero[f-3][c-3] ) or
                    # ... Horizontales
                    (c > 2 and fichaX == tablero[f][c-1] == tablero[f][c-2] == tablero[f][c-3]) or
                    # ... Verticales
                    (f > 2 and fichaX == tablero[f-1][c] == tablero[f-2][c] == tablero[f-3][c])
                ):
                    hubo_ganador = True
                    break
    return hubo_ganador

def verificar_validez_segun_lista(string_a_validar: str, lista_invalidos=[]):
    """
        Retorna el string en caso de ser validado contra la lista proporcionada
    """
    if string_a_validar.strip() in lista_invalidos:
        return verificar_validez_segun_lista(input('Valor invalido o tomado, seleccione otro valor\n=> '), lista_invalidos)
    else:
        lista_invalidos.append(string_a_validar.strip())
        return string_a_validar


def registrar_jugadores():
    nombres_invalidos = ['']
    caracteres_invalidos = ['', VACIO]

    jugador1 = (
        verificar_validez_segun_lista( input("Ingrese NOMBRE para jugador 1:\n"), nombres_invalidos ),
        verificar_validez_segun_lista( input("Ingrese UN CARACTER para jugador 1:\n")[0], caracteres_invalidos)
    )

    jugador2 = (
        verificar_validez_segun_lista( input("Ingrese NOMBRE para jugador 2:\n"), nombres_invalidos ),
        verificar_validez_segun_lista( input("Ingrese UN CARACTER para jugador 2:\n")[0], caracteres_invalidos )
    )

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
  while columna not in map(lambda n: str(n), range(1, maximo_columnas+1)):
    columna = input("Ingrese una opcion valida (1-7)\n\t=> ")
  else:
    columna = int(columna)
    columna -= 1
    return columna


def mostrar_cartel(titulo:str, mensaje:str):
    titulo_espaciado = ' ' + titulo + ' '
    largo_msj = mensaje

    largo_cartel = len(titulo_espaciado)+4 if len(titulo_espaciado) > len(largo_msj) else len(largo_msj)+4

    print(
        '',
        f"╔{titulo_espaciado.center(largo_cartel, '═')}╗",
        f"║{''.center(largo_cartel, ' ')}║",
        f"║{mensaje.center(largo_cartel, ' ')}║",
        f"║{''.center(largo_cartel, ' ')}║",
        f"╚{''.center(largo_cartel, '═')}╝",
        sep="\n"
    )


def mostrar_ganador(nombre_ganador=None):
    """
        Mostrara por consola el mensaje de ganador, en tanto se proporcione.
    """
    mensaje:str = 'HUBO UN EMPATE!'
    if nombre_ganador:
        mensaje = f"JUGADOR {nombre_ganador} ES EL GANADOR DE LA PARTIDA!"

    mostrar_cartel("FIN DEL JUEGO", mensaje)



def partida(tablero):
    j1, j2 = registrar_jugadores()
    print("\n\n========== EMPIEZA PARTIDA ==========")

    # Jugadores guarda los valores de nombre y turno que se hayan seleccionado para los jugadores, la key corresponde a su turno (j1 = turno 0, j2 = turno 1)
    jugadores = {
      0: {
            'nombre':j1[0],
            'ficha': j1[1]
        },
      1: {
            'nombre':j2[0],
            'ficha': j2[1]
        }
    }

    cantidad_columnas = len(tablero[0])
    turno = 0

    while not verificar_espacios_tablero(tablero):
        # Correccion de fila
        fila = FILA-1
        columna = validar_columna_jugada(
            input( f"\nJUGADOR {jugadores.get(turno).get('nombre')}, ingrese su jugada (1-7): "),
            cantidad_columnas
        )

        if posicion_vacia(tablero, columna):
            fila = posicion_en_fila_ocupado(tablero, fila, columna)
            ficha_en_tablero(tablero, fila, columna, ficha=jugadores.get(turno).get('ficha'))
            mostrar_tablero(tablero)

            if hubo_ganador(tablero, j1, j2):
                mostrar_ganador(jugadores.get(turno).get('nombre'))
                break
            else:
                turno = siguiente_turno(turno)
        else:
            print("\nINGRESE VALOR VALIDO")
            # Al ingresar un valor invalido, no se jugo ficha, entonces forzamos el alternado de turno para que vuelva a jugar el mismo jugador, solo en este caso
    else:
        mostrar_ganador()

    # -----------SI LES PARECE , ACA PUEDE GUARDAR GANADOR EN ARCHIVOS-----------

    # Logica para volver a jugar
    return menu() if input('Ingrese Y para al menu\n\t=>') in ['Y', 'y'] else print('Gracias por jugar!')

######################################## OPCIONES DE MENU ########################################


def jugar():
    tablero = inicializarTablero()

    mostrar_tablero(tablero)
    partida(tablero)


def instrucciones():
    try:
        with open("./Instrucciones.txt", "r", encoding="utf8") as arch:
            for l in arch:
                print(l)
    except FileNotFoundError as mensaje:
        print("Archivo no encontrado:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass 
    if input('\nPresione una tecla para volver al menu o 0 para salir...\n\t=> ') == "0":
        despedir()
    else:
        menu()


def ranking():
    print("\n\n========== RANKING ==========")
    d = {}
    with open("./ganadores_historico.txt", "r", encoding="utf8") as f:
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
    mostrar_cartel('Adios!', "GRACIAS POR ENTRAR A NUESTRO FABULOSO JUEGO")
    input("Presione una tecla para salir...")
    return False


######################################## FUNCION MENU ########################################

def menu():
    print("========== Menu ==========")
    print("1- JUGAR")
    print("2- INSTRUCCIONES")
    print("3- RANKING")
    print("4- SALIR")
    print("==========================")


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
mostrar_cartel('4 EN RAYA','Bienvenido a nuestro juego!'.upper())
while comenzar():
    # Menu arrojara False al salir del juego desde alguna de las opciones "in game"
    if not menu():
        break
else:
    despedir()
