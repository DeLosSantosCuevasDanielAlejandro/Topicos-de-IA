import random
import numpy as np

class Particula:
    def __init__(self, dimension, matriz_distancias, limites, funcion_objetivo):
        self.dimension = dimension
        self.matriz_distancias = matriz_distancias
        self.limites = limites
        self.funcion_objetivo = funcion_objetivo
        self.posicion = random.sample(range(dimension), dimension)
        self.velocidad = 0
        self.valor = self.evaluar()
        self.mejor_posicion = self.posicion[:]
        self.mejor_valor = self.valor

    def evaluar(self):
        self.valor = self.funcion_objetivo(self.posicion, self.matriz_distancias)
        return self.valor

    def mover(self, inercia, c1, c2, mejor_global):
        posicion_anterior = self.posicion[:]

        r1 = random.random()
        r2 = random.random()
        influencia_p = c1 * r1
        influencia_g = c2 * r2
        self.velocidad = inercia * self.velocidad + influencia_p + influencia_g

        # Movimiento mediante múltiples intercambios aleatorios de ciudades
        num_intercambios = max(1, int(self.velocidad))  # Asegura al menos un intercambio
        for _ in range(num_intercambios):
            i, j = random.sample(range(self.dimension), 2)
            self.posicion[i], self.posicion[j] = self.posicion[j], self.posicion[i]

        nuevo_valor = self.evaluar()
        if nuevo_valor < self.mejor_valor:
            self.mejor_valor = nuevo_valor
            self.mejor_posicion = self.posicion[:]
        else:
            if nuevo_valor > self.valor:
                self.posicion = posicion_anterior[:]
                self.valor = self.funcion_objetivo(self.posicion, self.matriz_distancias)

    def __str__(self):
        return (
            f"  Posición: {self.posicion}\n"
            f"  Velocidad: {round(self.velocidad, 2)}\n"
            f"  Valor: {self.valor}\n"
            f"  Mejor posición: {self.mejor_posicion}\n"
        )

class Enjambre:
    def __init__(self, n_particulas, dimension, matriz_distancias, limites, funcion_objetivo):
        self.particulas = [
            Particula(dimension, matriz_distancias, limites, funcion_objetivo)
            for _ in range(n_particulas)
        ]
        self.funcion_objetivo = funcion_objetivo
        self.mejor_particula = min(self.particulas, key=lambda p: p.valor)

        print("=== Enjambre inicial creado ===")
        for i, particula in enumerate(self.particulas):
            print(f"Partícula {i + 1}:\n{particula}")
        print("================================")

    def mover_enjambre(self, inercia, c1, c2):
        print("Moviendo enjambre...")
        for idx, particula in enumerate(self.particulas):
            print(f"\nPartícula {idx + 1} antes del movimiento:")
            print(particula)

            if particula != self.mejor_particula:
                particula.mover(inercia, c1, c2, self.mejor_particula.mejor_posicion)
                print(f"Partícula {idx + 1} después del movimiento:")
                print(particula)
                if particula.valor < self.mejor_particula.valor:
                    self.mejor_particula = particula
            else:
                print(f"Partícula {idx + 1} es la mejor del enjambre y no se moverá.")

    def evaluar_enjambre(self):
        print("Evaluando enjambre...")
        for idx, particula in enumerate(self.particulas):
            valor = particula.evaluar()
            print(f"Partícula {idx + 1} valor evaluado: {valor}")
        self.mejor_particula = min(self.particulas, key=lambda p: p.valor)


def funcion_objetivo_tsp(ruta, matriz_distancias):
    distancia = 0
    for i in range(len(ruta)):
        ciudad_origen = ruta[i]
        ciudad_destino = ruta[(i + 1) % len(ruta)]
        distancia += matriz_distancias[ciudad_origen][ciudad_destino]
    return distancia

def generar_matriz_distancias(n):
    matriz = np.random.randint(10, 100, size=(n, n))
    matriz = (matriz + matriz.T) // 2
    np.fill_diagonal(matriz, 0)
    return matriz

def optimizar_enjambre(funcion_objetivo, n_ciudades, n_particulas=30, n_iteraciones=100):
    matriz_distancias = generar_matriz_distancias(n_ciudades)
    limites = (0, n_ciudades - 1)
    enjambre = Enjambre(n_particulas, n_ciudades, matriz_distancias, limites, funcion_objetivo)

    inercia = 0.7
    c1 = 1.4
    c2 = 1.4

    for i in range(n_iteraciones):
        print(f"\n===== Iteración {i + 1} =====")
        enjambre.mover_enjambre(inercia, c1, c2)
        print(">> Mejor valor hasta ahora:", enjambre.mejor_particula.valor)

    return {
        "mejor_valor": enjambre.mejor_particula.valor,
        "mejor_posicion": enjambre.mejor_particula.posicion,
        "matriz_distancias": matriz_distancias
    }

# Ejecución del código
if __name__ == "__main__":
    n_ciudades = 6
    resultados = optimizar_enjambre(funcion_objetivo_tsp, n_ciudades, n_particulas=5, n_iteraciones=10)

    print("\n=== Resultados Finales ===")
    print("Mejor ruta encontrada:", resultados["mejor_posicion"])
    print("Distancia total:", resultados["mejor_valor"])
    print("Matriz de distancias:\n", resultados["matriz_distancias"])
