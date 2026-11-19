"""
Agenda de peliculas.
Módulo de cálculos.
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    d = {}
    d['nombre'] = nombre
    d['genero'] = genero
    d['duracion'] = duracion
    d['hora'] = hora
    d['dia'] = dia
    d['anio'] = anio
    d['clasificacion'] = clasificacion
    return d

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    bd = [p1, p2, p3, p4, p5]
    for i in range(len(bd)):
        if bd[i]['nombre'] == nombre_pelicula:
            return bd[i]
    return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    bd = [p1, p2, p3, p4, p5]
    lt = []
    for i in range(len(bd)):
        lt.append(bd[i]['duracion'])
    
    return bd[lt.index(max(lt))]

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    bd = [p1, p2, p3, p4, p5]
    l_promedio = []
    for i in range(len(bd)):
        l_promedio.append(bd[i]['duracion'])

    promedio = sum(l_promedio) / len(l_promedio)
    h = int(promedio // 60)
    m = int(promedio % 60)
    
    if h < 10:
        h_str = "0" + str(h)
    else:
        h_str = str(h)
        
    if m < 10:
        m_str = "0" + str(m)
    else:
        m_str = str(m)
        
    return h_str + ":" + m_str

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    bd = [p1, p2, p3, p4, p5]
    l_estrenos = []
    for i in range(len(bd)):
        if bd[i]['anio'] > anio:
            l_estrenos.append(bd[i]['nombre'])
    
    if len(l_estrenos) == 0:
        return 'Ninguna'
    else:
        return ', '.join(l_estrenos)

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    bd = [p1, p2, p3, p4, p5]
    count = 0
    for i in range(len(bd)):
        if bd[i]['clasificacion'] == '18+':
            count += 1
    return count

def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool: 
    if control_horario == True:
        if "Documental" in peli['genero'] and nueva_hora >= 2200:
            return False
        
        if "Drama" in peli['genero'] and nuevo_dia == "Viernes":
            return False
        
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        if nuevo_dia in dias_semana:
            if nueva_hora >= 2300 or nueva_hora < 600:
                return False

    inicio_nueva = (nueva_hora // 100) * 60 + (nueva_hora % 100)
    fin_nueva = inicio_nueva + peli['duracion']

    bd = [p1, p2, p3, p4, p5]
    for i in range(len(bd)):
        otra = bd[i]
        if otra['nombre'] != peli['nombre'] and otra['dia'] == nuevo_dia:
            inicio_otra = (otra['hora'] // 100) * 60 + (otra['hora'] % 100)
            fin_otra = inicio_otra + otra['duracion']
            
            if inicio_nueva < fin_otra and fin_nueva > inicio_otra:
                return False

    peli['hora'] = nueva_hora
    peli['dia'] = nuevo_dia
    return True
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool) -> bool:
    if edad_invitado >= 18:
        return True

    if edad_invitado < 15 and "Terror" in peli['genero']:
        return False

    if edad_invitado <= 10 and "Familiar" not in peli['genero']:
        return False

    clasif = peli['clasificacion']
    edad_minima = 0
    if clasif == "7+":
        edad_minima = 7
    elif clasif == "13+":
        edad_minima = 13
    elif clasif == "16+":
        edad_minima = 16
    elif clasif == "18+":
        edad_minima = 18

    if edad_invitado < edad_minima:
        if "Documental" in peli['genero']:
            return True
        else:
            return autorizacion_padres

    return True
