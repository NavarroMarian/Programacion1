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

FILA = 6
COLUMNA = 7
VACIO = '-'

######################################## VISUALES ########################################

def mostrar_cartel(titulo: str, mensaje: str):
    """
        Muestra un cartel con titulo y unico mensaje (string)
    """
    titulo_espaciado = ' ' + titulo + ' '
    largo_msj = mensaje

    largo_cartel = len(titulo_espaciado) + \
        4 if len(titulo_espaciado) > len(largo_msj) else len(largo_msj)+4

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
    mensaje: str = 'HUBO UN EMPATE!'
    if nombre_ganador:
        mensaje = f"JUGADOR {nombre_ganador[0:16]} ES EL GANADOR DE LA PARTIDA!"

    mostrar_cartel("FIN DEL JUEGO", mensaje)


def despedir():
    """
        Envia mensaje de despedida por consola
    """
    mostrar_cartel('Adios!', "GRACIAS POR ENTRAR A NUESTRO FABULOSO JUEGO")


def mostrar_separador_seccion(nombre_seccion=None, interlineado=1):
    nombre_seccion = ' ' + nombre_seccion[0:16] + ' ' if nombre_seccion != None else '═'

    if interlineado:
        print("\n"*interlineado)
    print(nombre_seccion.center(35, '═'))




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



def verificar_espacios_tablero(tabla):
    """
        Devuelve True o False en base a si el tablero proporcionado esta completo.
    """
    esta_completo = True

    for i in tabla:
        for j in i:
            if j == VACIO:
                esta_completo = False
                break

    return esta_completo


def hubo_ganador(tablero):
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
                    # ... Horizontales
                    (c > 2 and fichaX == tablero[f][c-1] == tablero[f][c-2] == tablero[f][c-3]) or
                    # ... Verticales
                    (f > 2 and fichaX == tablero[f-1][c] == tablero[f-2][c] == tablero[f-3][c]) or
                    # Verificacion de Diagonales
                    # Diagonal primaria
                    ((f > 2 and columnas > c+3) and (fichaX == tablero[f-1][c+1] == tablero[f-2][c+2] == tablero[f-3][c+3])) or
                    # Diagonal secundaria
                    ((f > 2 and c > 2) and (fichaX == tablero[f-1][c-1] == tablero[f-2][c-2] == tablero[f-3][c-3]))
                ):
                    hubo_ganador = True
                    break
    return hubo_ganador


def verificar_validez_segun_lista(string_a_validar, lista_prohibidos=[], maximo_largo_cadena=10):
    """
        Retorna un string de input en caso de ser validado contra la lista de prohibidos proporcionada o maximo de caracteres.
    """
    if string_a_validar.strip() in lista_prohibidos or string_a_validar.find(',') != -1:
        return verificar_validez_segun_lista(input(f'No se permiten los valores {str(lista_prohibidos)}, seleccione otro valor\n\t» '), lista_prohibidos, maximo_largo_cadena)
    elif len(string_a_validar)>maximo_largo_cadena:
        return verificar_validez_segun_lista(input(f'El largo no puede superar {maximo_largo_cadena} caracteres, seleccione otro valor\n\t» '), lista_prohibidos, maximo_largo_cadena)
    else:
        lista_prohibidos.append(string_a_validar.strip())
        return string_a_validar


def registrar_jugadores():
    """
        Se encarga de gestionar los nombres y caracteres de los usuarios. Devuelve tupla.
    """
    nombres_invalidos = ['', ',']
    caracteres_invalidos = ['', VACIO]

    mostrar_separador_seccion("Registro Jugadores")


    jugador1 = (
        verificar_validez_segun_lista( input("Ingrese NOMBRE para jugador 1:\n\t» "), nombres_invalidos ),
        verificar_validez_segun_lista( input("Ingrese UN CARACTER para jugador 1:\n\t» ")[0:1], caracteres_invalidos, 1)
    )
    mostrar_separador_seccion()

    jugador2 = (
        verificar_validez_segun_lista( input("Ingrese NOMBRE para jugador 2:\n\t» "), nombres_invalidos ),
        verificar_validez_segun_lista( input("Ingrese UN CARACTER para jugador 2:\n\t» ")[0:1], caracteres_invalidos,1 )
    )

    print(f"{jugador1[0]} jugarás con {jugador1[1]}\n{jugador2[0]} jugarás con {jugador2[1]}")
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
    columna = input("Ingrese una opcion valida (1-7)\n\t» ")
  else:
    columna = int(columna)
    columna -= 1
    return columna

def partida():
    """
        Funcion principal del juego
    """

    # Inicializa los jugadores, con sus nombres y caracteres elegidos
    j1, j2 = registrar_jugadores()
    # Tablero inicializado (matriz)
    tablero = inicializarTablero()

    mostrar_separador_seccion("EMPIEZA LA PARTIDA!")


    mostrar_tablero(tablero)
    
    # Jugadores guarda los valores de nombre y turno que se hayan seleccionado para los jugadores, la key corresponde a su turno
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

    # Variable de turno (j1 = turno 0, j2 = turno 1)
    turno = 0

    # En cada ciclo verificara que el tablero tenga al menos una posicion para ser jugada.
    while not verificar_espacios_tablero(tablero):
        # Correccion de fila
        fila = FILA-1

        # Obtengo el nombre del jugador del turno correspondiente
        nombre_jugador_actual = jugadores.get(turno).get('nombre')

        mostrar_separador_seccion(f"Turno de {nombre_jugador_actual}")

        # Recibe y valida el input de la columna elegida por el jugador.
        columna = validar_columna_jugada(
            input( f"\nJUGADOR {nombre_jugador_actual}, ingrese su jugada (1-7)\n\t» "),
            cantidad_columnas
        )

        # Validada la columna, se verifica que haya espacio para la jugada.
        if posicion_vacia(tablero, columna):
            # Obtendra la posicion de la fila
            fila = posicion_en_fila_ocupado(tablero, fila, columna)

            # La matriz de tablero se modifica con la ficha del jugador.
            ficha_en_tablero(tablero, fila, columna, ficha=jugadores.get(turno).get('ficha'))

            # Tras cada jugada, se verificara si hubo un ganador con el tablero actual.
            if hubo_ganador(tablero):
                # Al haber ganador, obtenemos el nombre del jugador que coincida con el turno
                mostrar_ganador(nombre_jugador_actual)

                # El jugador sumara un punto en su ranking, o sera incluido en el si no se encuentra.
                sumarPunto(nombre_jugador_actual)
                break
            else:
                # Si no hubo ganador, alternamos por el siguiente turno
                turno = siguiente_turno(turno)
        else:
            # Al no haber espacio para la jugada, no se jugo ficha y vuelve a intentar el mismo jugador
            print(f"\nColumna Completa! {nombre_jugador_actual}, ingrese nuevo valor")
        # Sin importar si se jugo, se mostrara siempre la tabla al final de cada turno
        mostrar_tablero(tablero)
    else:
        # Si no hay espacios en el tablero (y no hubo break intermedio por haber ganador), entonces es un empate, lo mostramos por pantalla.
        mostrar_ganador(ganador=None)
        # No es necesario dar parametro ya que utiliza valores por defecto
        #mostrar_ganador()
    mostrar_separador_seccion('Tablero final')
    mostrar_tablero(tablero)
    mostrar_separador_seccion(interlineado=0)



def instrucciones():
    mostrar_separador_seccion("INSTRUCCIONES")
    try:
        with open("./Instrucciones.txt", "r", encoding="utf8") as arch:
            for l in arch:
                print(l)
    except FileNotFoundError as mensaje:
        print("Archivo no encontrado:\n", mensaje)
    except OSError as mensaje:
        print("Error en sistema al intentar leer el archivo:\n", mensaje)
    except Exception as e:
        print('Se produjo un error no especificado:\n', e)
    finally:
        try:
            arch.close()
        except NameError:
            pass 
    mostrar_separador_seccion(interlineado=1)



#===============================================RANKING=============================================

def leerArchivo():
    diccionario = {}
    # Lee el archivo de ganadores, y lo crea si no existe.
    try:
        archivo = open("ganadores.txt")
    except FileNotFoundError:
        archivo = open("ganadores.txt","w+")

    for linea in archivo:
        # Se lee la Key y el Value separados con un espacio
        #print(linea.split(","))
        key, value = linea.split(",")
        
        # Se asigna el par Key\Value a el diccionario "diccionario"
        diccionario[key] = int(value)
    return diccionario

def escribirArchivo(dict):
    f = open("ganadores.txt","w+")
    for key,value in dict.items():
        f.write(f"{key},{value}\n")

    f.close()

def sumarPunto(playerName):
    """

    """
    ganadores = leerArchivo()
    # Si la key "playerName" existe en el archivo, le suma uno al Value. Caso contrario, lo escribe con un nuevo "playerName" y le asigna el Value = 1.
    if playerName in ganadores.keys():
        ganadores[playerName] += 1
    else:
        ganadores[playerName] = 1
    escribirArchivo(ganadores)
    
def imprimirScoreboard():
    """
        Mostrara la lista de ganadores con su conteo de partidas ganadas
    """
    mostrar_separador_seccion("Ranking")
    print()

    # Creamos una lista desde el archivo utilizando la funcion leerArchivo()
    dicGanadores = leerArchivo()
    listaGanadores = [[key,value] for key,value in dicGanadores.items()]
        # Guardamos la lista en una lista secundaria en la que esta ordenada por Puntaje, es decir por "Value".
    listaGanadores_sorted = sorted(listaGanadores, key=lambda x: -x[1])
    """titulo = ["Jugador","Puntaje"]
    print(tabulate(listaGanadores_sorted,titulo, tablefmt="psql"))"""
    print("╔════════════════╦════════════════╗")
    print("║     Jugador    ║     Puntaje    ║")
    print("╠════════════════╬════════════════╣")
    # Imprime cada linea del archivo alineando  los valores del Key y Value.
    for key,value in listaGanadores_sorted:
        print(f"║{key[0:16].center(16,' ')}║{str(value)[0:16].center(16,' ')}║")
    print("╚════════════════╩════════════════╝")
    mostrar_separador_seccion(interlineado=0)


#===================================================================================================


######################################## FUNCION MENU ########################################

def menu():
    """
        Muestra por pantalla el menu principal, recibiendo parametros para siguiente instruccion.
    """
    titulo = '╔═════════════ Menu ══════════════╗'
    # Para el formateo, el largo del titulo -4 lugares para espaciado.
    largo_titulo = len(titulo)-4

    print('\n\n'+titulo)
    print("║ "+ "1- JUGAR".ljust(largo_titulo)  , '║')
    print("║ "+ "2- INSTRUCCIONES".ljust(largo_titulo)  , '║')
    print("║ "+ "3- RANKING".ljust(largo_titulo)  , '║')
    print("║ "+ "4- SALIR".ljust(largo_titulo)  , '║')
    print("╚" + ''.center(largo_titulo+2, "═") + "╝")


    opcion = input("Ingrese opcion\n\t» ")
    # En lugar de usar numeros para el menu, usaremos su equivalente en tipo string
    while opcion not in map(lambda x: str(x), range(1, 5)):
        print('Opcion incorrecta.')
        opcion = input("Ingrese opcion válida (1-5):\n\t» ")

    # acciones es un diccionario que guarda la referencia a funciones del programa
    acciones = {
        '1': partida,
        '2': instrucciones,
        '3': imprimirScoreboard,
        '4': despedir
    }

    # Obtengo la funcion guardada en el diccionario y la asigno a una variable
    accion = acciones.get(opcion)

    # Ejecuto mi nueva variable que hace referencia a una funcion
    # Esto retornara falso solo al elegir "salir" (4)
    accion()

    # Salvo que se solicite salir, tras cada accion se consultara si el usuario desea volver al menu principal.
    if opcion != '4':
        return menu() if input('Ingrese "Y" para volver al menu o cualquier otra tecla para salir\n\t» ') in ['Y', 'y'] else despedir()

    
    """
    # Alternativo
    # Ejecutar directamente accediendo mediante la KEY de opcion
    # Entiendo que accediendo al valor del diccionario recibire la referencia a la funcion, entonces podre ejecutarla

    return acciones[opcion]()
    """


    

######################################## PROGRAMA PRINCIPAL ########################################
print()
mostrar_separador_seccion('4 EN RAYA')
mostrar_cartel('INTEGRANTES GRUPO 11', "Ivan Samokec, Carolina Maio, Mariana Navarro, Ramon Irala")
if input('Ingrese "Y" para ir al menu principal\n\t» ') in ['y', 'Y']:
    menu()
