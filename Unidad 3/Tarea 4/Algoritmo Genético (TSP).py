import random
import numpy as np

# Parámetros iniciales
N = 100
pc = 0.9
pm = 0.1
generaciones = 150

# Ciudades
ciudades = [
    "Bilbao", "Celta", "Vigo", "Valladolid", "Jaen", "Sevilla", "Granada", "Murcia",
    "Valencia", "Barcelona", "Gerona", "Zaragoza", "Madrid", "Albacete"
]
indices = {ciudad: i for i, ciudad in enumerate(ciudades)}

# Inicializamos la matriz de distancias
distancias = np.inf * np.ones((len(ciudades), len(ciudades)))

# Conexiones válidas extraídas del grafo
conexiones = [
    ("Bilbao", "Celta", 378), ("Bilbao", "Zaragoza", 324), ("Celta", "Vigo", 171), ("Celta", "Valladolid", 235),
    ("Vigo", "Valladolid", 356), ("Vigo", "Sevilla", 245), ("Valladolid", "Madrid", 193),
    ("Valladolid", "Zaragoza", 390), ("Valladolid", "Jaen", 411),
    ("Jaen", "Sevilla", 125), ("Jaen", "Granada", 207), ("Sevilla", "Granada", 211),
    ("Granada", "Murcia", 257), ("Murcia", "Albacete", 150), ("Murcia", "Valencia", 241),
    ("Valencia", "Albacete", 191), ("Valencia", "Barcelona", 349), ("Barcelona", "Zaragoza", 296),
    ("Barcelona", "Gerona", 100), ("Zaragoza", "Gerona", 289), ("Zaragoza", "Madrid", 190),
    ("Zaragoza", "Albacete", 215), ("Madrid", "Albacete", 251), ("Albacete", "Granada", 244)
]

# Crear matriz y lista de adyacencia
grafo = {i: [] for i in range(len(ciudades))}

for origen, destino, dist in conexiones:
    i, j = indices[origen], indices[destino]
    distancias[i][j] = distancias[j][i] = dist
    grafo[i].append(j)
    grafo[j].append(i)

# Función de aptitud
def calcular_distancia_total(ruta):
    distancia = 0
    for i in range(len(ruta)):
        origen = ruta[i]
        destino = ruta[(i + 1) % len(ruta)]
        if destino not in grafo[origen]:
            return np.inf  # Ruta inválida
        distancia += distancias[origen][destino]
    return distancia

# Generar población inicial con rutas válidas
def ruta_valida():
    while True:
        ruta = [random.choice(list(grafo.keys()))]
        visitadas = set(ruta)
        while len(ruta) < len(ciudades):
            vecinos = [n for n in grafo[ruta[-1]] if n not in visitadas]
            if not vecinos:
                break  # atascado
            siguiente = random.choice(vecinos)
            ruta.append(siguiente)
            visitadas.add(siguiente)
        if len(ruta) == len(ciudades) and ruta[0] in grafo[ruta[-1]]:
            return ruta

def generar_poblacion(n):
    return [ruta_valida() for _ in range(n)]

# Calcular la aptitud
def evaluar_poblacion(poblacion):
    return [1 / calcular_distancia_total(ind) for ind in poblacion]

# Torneo
def seleccion_torneo(poblacion, aptitudes, k=3):
    seleccionados = random.sample(list(zip(poblacion, aptitudes)), k)
    seleccionados.sort(key=lambda x: x[1], reverse=True)
    return seleccionados[0][0]

# Cruce respetando adyacencia
def cruce(p1, p2):
    if random.random() > pc:
        return p1[:], p2[:]

    a, b = sorted(random.sample(range(len(p1)), 2))
    hijo = [-1]*len(p1)
    hijo[a:b] = p1[a:b]

    fill = [ciudad for ciudad in p2 if ciudad not in hijo]
    fill_iter = iter(fill)
    for i in range(len(hijo)):
        if hijo[i] == -1:
            hijo[i] = next(fill_iter)

    if es_valida(hijo):
        return hijo, cruce(p2, p1)[0]
    else:
        return p1[:], p2[:]  # fallback

# Mutación por intercambio (si mantiene adyacencia)
def mutacion(cromosoma):
    if random.random() < pm:
        a, b = random.sample(range(len(cromosoma)), 2)
        nuevo = cromosoma[:]
        nuevo[a], nuevo[b] = nuevo[b], nuevo[a]
        if es_valida(nuevo):
            return nuevo
    return cromosoma

def es_valida(ruta):
    for i in range(len(ruta)):
        if ruta[(i + 1) % len(ruta)] not in grafo[ruta[i]]:
            return False
    return True

# Bucle principal con impresión por generación
poblacion = generar_poblacion(N)
for gen in range(generaciones):
    aptitudes = evaluar_poblacion(poblacion)
    mejor_gen = min(poblacion, key=lambda r: calcular_distancia_total(r))
    mejor_dist_gen = calcular_distancia_total(mejor_gen)
    ruta_gen = [ciudades[i] for i in mejor_gen]
    print(f"Generación {gen+1}: Distancia = {mejor_dist_gen} | Ruta: {' -> '.join(ruta_gen)}")

    nueva_poblacion = []
    while len(nueva_poblacion) < N:
        p1 = seleccion_torneo(poblacion, aptitudes)
        p2 = seleccion_torneo(poblacion, aptitudes)
        h1, h2 = cruce(p1, p2)
        nueva_poblacion.append(mutacion(h1))
        if len(nueva_poblacion) < N:
            nueva_poblacion.append(mutacion(h2))
    poblacion = nueva_poblacion

# Resultado final
mejor = min(poblacion, key=lambda r: calcular_distancia_total(r))
mejor_distancia = calcular_distancia_total(mejor)
ruta_ciudades = [ciudades[i] for i in mejor]

print("\nRuta válida óptima encontrada:")
print(" -> ".join(ruta_ciudades))
print(f"Distancia total: {mejor_distancia}")
