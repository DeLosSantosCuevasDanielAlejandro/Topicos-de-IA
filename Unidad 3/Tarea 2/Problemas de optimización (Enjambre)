import random

class Particula:
    def __init__(self, limites_x, limites_y):
        """
        Inicializa una partícula con posición aleatoria dentro de los límites dados
        y velocidad inicial en cero.
        """
        min_x, max_x = limites_x
        min_y, max_y = limites_y

        if min_x >= max_x or min_y >= max_y:
            raise ValueError("El mínimo debe ser menor que el máximo en cada eje.")
        
        self.posicion = [
            random.randint(min_x, max_x),
            random.randint(min_y, max_y)
        ]
        self.velocidad = [0.0, 0.0]
        self.valor = None
        self.memoria = None

    def __str__(self):
        return (f"Posición: X = {self.posicion[0]}, Y = {self.posicion[1]}, "
                f"Velocidad: {self.velocidad}, Valor: {self.valor}, Memoria: {self.memoria}")


class Enjambre:
    def __init__(self):
        """
        Inicializa un enjambre vacío.
        """
        self.particulas = []

    @classmethod
    def crear(cls, n_particulas, limites_x, limites_y, verbose=False):
        """
        Crea un enjambre con múltiples partículas generadas aleatoriamente.
        """
        print(f"\nLímites establecidos:")
        print(f"  - Eje X: {limites_x}")
        print(f"  - Eje Y: {limites_y}\n")

        enjambre = cls()
        for i in range(n_particulas):
            if verbose:
                print(f"Creando partícula {i + 1}/{n_particulas}...")
            particula = Particula(limites_x, limites_y)
            if verbose:
                print(particula)
            enjambre.agregar_particula(particula)
        return enjambre

    def agregar_particula(self, particula):
        """
        Agrega una partícula existente al enjambre.
        """
        self.particulas.append(particula)

    def mostrar_enjambre(self):
        """
        Muestra todas las partículas del enjambre.
        """
        print("\nEnjambre de partículas:")
        for i, particula in enumerate(self.particulas, 1):
            print(f"Partícula {i}: {particula}")


# === EJEMPLO DE USO ===

limites_x = (-10, 10)
limites_y = (-10, 10)

# 1. Crear un enjambre completo de n partículas
enjambre = Enjambre.crear(n_particulas=5, limites_x=limites_x, limites_y=limites_y, verbose=True)

# 2. Crear una partícula individual
particula_extra = Particula(limites_x, limites_y)
print("\nPartícula individual creada:")
print(particula_extra)

# 3. Agregar la partícula individual al enjambre
enjambre.agregar_particula(particula_extra)

# 4. Mostrar el enjambre actualizado
enjambre.mostrar_enjambre()
