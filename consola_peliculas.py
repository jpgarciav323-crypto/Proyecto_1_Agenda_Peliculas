"""
Agenda de peliculas.
Modulo de interacci0n por consola.
"""
import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora%100)
    else:
        min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    print(mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5))

def ejecutar_encontrar_pelicula(pelicula, p1, p2, p3, p4, p5):
    print(mod.encontrar_pelicula(pelicula, p1, p2, p3, p4, p5))

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    print(mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5))  

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio) -> None:
    print(mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio))

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    print(mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5))
    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    print("Reagendar una pelicula de la agenda")

    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)
    
    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        nuevo_dia = input("Ingrese el nuevo dia (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo): ")
        nueva_hora = int(input("Ingrese la nueva hora en formato 24h (ej. 1430): "))
        control = input("¿Desea activar el control horario? (si/no): ").strip().lower()
        
        if control == "si":
            control_horario = True
        else:
            control_horario = False
            
        se_pudo = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)
        
        if se_pudo == True:
            print("La pelicula fue reagendada exitosamente.")
        else:
            print("No se pudo reagendar la pelicula por conflictos de horario o restricciones.")

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    print("Decidir si se puede invitar a alguien a ver una pelicula")

    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        edad = int(input("Ingrese la edad del invitado: "))
        aut = input("¿Tiene autorizacion de sus padres? (si/no): ").strip().lower()
        
        if aut == "si":
            autorizacion = True
        else:
            autorizacion = False
            
        puede = mod.decidir_invitar(pelicula, edad, autorizacion)
        
        if puede == True:
            print("Si se puede invitar a la persona a ver", nom_peli)
        else:
            print("No se puede invitar a la persona a ver", nom_peli)
  
def iniciar_aplicacion():
    pelicula1 = mod.crear_pelicula("Shrek", "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out", "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
    pelicula3 = mod.crear_pelicula("Icarus", "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception", "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back", "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de peliculas para la semana de receso" + "\n" + ("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")
    print(" 7 - Encontrar Pelicula")    
    print(" 8 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        anio = int(input('Ingrese el Año: '))
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5)
    elif opcion_elegida == '7':
        pelicula = input('Ingrese la pelicula a buscar: ')
        ejecutar_encontrar_pelicula(pelicula, p1, p2, p3, p4, p5)
    elif opcion_elegida == "8":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando

iniciar_aplicacion()
