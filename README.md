# Este repositorio pertenece a: Daniel Alejandro De Los Santos Cuevas
## 📁 Unidad 1
- **Tarea 1**  
📝 La inteligencia artificial (IA) ha revolucionado múltiples sectores al mejorar la eficiencia y optimizar procesos. Ejemplos incluyen **Deep Blue** en ajedrez, **ALVINN** en conducción autónoma, diagnóstico médico avanzado, optimización logística con **DART**, robots quirúrgicos como **HipNav**, detección de fraudes en finanzas, seguridad con análisis de video, agricultura de precisión con **See & Spray**, manufactura automatizada en **Tesla**, recomendaciones en **Netflix**, predicción climática con **GraphCast**, y educación personalizada con **Khanmigo**. Estos avances muestran su impacto creciente en la sociedad.
------------
-  **Tarea 2**  
📝 La **lógica difusa** es una rama de la inteligencia artificial que permite analizar información en una escala entre lo falso y lo verdadero, facilitando el manejo de conceptos vagos. En un aire acondicionado, esta tecnología ajusta gradualmente la potencia del compresor y la velocidad del ventilador en lugar de simplemente encenderlos o apagarlos, mejorando la eficiencia y el confort.
El código presentado implementa un control difuso en un aire acondicionado con un sensor **DHT11** y un sistema de reglas basadas en la diferencia entre la temperatura actual y la deseada. Se definen conjuntos borrosos para clasificar la temperatura (muy fría, fría, ideal, caliente, muy caliente) y la velocidad del ventilador (bajo, medio, alto). Dependiendo de la diferencia de temperatura, el ventilador ajusta su velocidad suavemente, evitando cambios bruscos.
------------
-  **Tarea 3**  
📝 Dado a que esta fue una tarea hecha en equipo, fue subida en el repositorio de mi compañero José Miguel Ruíz Medrano
------------
## 📁 Unidad 2
- **Tarea 1**  
📝La siguiente tarea explica 4 problemas clásicos de optimización
**Problema de Programación de Trabajos (JSSP)**: Consiste en asignar tareas a máquinas asegurando que se cumplan las fechas límite, con restricciones de capacidad y simultaneidad. El objetivo es minimizar el tiempo total, los costos y los retrasos.
**Problema de las N Reinas (N-Queens)**: Se trata de colocar **n** reinas en un tablero de ajedrez sin que se ataquen entre sí. Las restricciones son no compartir filas, columnas ni diagonales.
**Árbol de Expansión Mínima (MST)**: Es un árbol que conecta todos los vértices de un grafo con el menor peso total. Se resuelve con algoritmos como **Kruskal**, que selecciona las aristas de menor peso sin crear ciclos.
**Problema del Agente Viajero (TSP)**: Un vendedor debe visitar varias ciudades, minimizando la distancia total, visitando cada ciudad una sola vez y evitando subciclos. Se puede resolver con técnicas como la **optimización por colonia de hormigas**.
------------
- **Tarea 2**  
📝 El **Problema de las 8 Reinas** es un caso específico del **Problema de las N Reinas**, donde se deben colocar 8 reinas en un tablero de 8x8, de manera que ninguna reina pueda atacar a otra. Las reinas no deben compartir la misma fila, columna ni diagonal.
El **Algoritmo de Búsqueda Tabú** es un enfoque heurístico que utiliza una memoria para almacenar los últimos movimientos realizados. Esto permite evitar soluciones ya exploradas y ayuda a minimizar los conflictos entre las reinas.
------------
- **Tarea 3**  
📝 Este código resuelve el problema de las 8 reinas usando recocido simulado. Coloca 8 reinas en un tablero de 8x8 sin que se ataquen entre sí.

Funciones principales:
- **calcularConflictos**: Cuenta los ataques entre reinas.
- **generarVecino**: Mueve una reina a una nueva posición para crear un tablero vecino.
- **probabilidadAceptacion**: Calcula la probabilidad de aceptar un peor movimiento, dependiendo de la temperatura.
- **mostrarTablero**: Muestra el tablero actual en la consola.
- **resolverOchoReinasRecocidoSimulado**: Ejecuta el recocido simulado para encontrar la solución, mejorando el tablero en cada iteración.
  Uso:
El usuario define la temperatura inicial, final y un estado inicial (o se genera uno aleatorio). El algoritmo ajusta el tablero para minimizar los conflictos y muestra la solución final.
------------
## 📁 Unidad 3
- **Tarea 1**  
📝 La **evolución diferencial** es un algoritmo heurístico de optimización utilizado para problemas no lineales y multimodales. Funciona mediante una población de soluciones que se actualizan a través de mutación, cruzamiento y selección.

Componentes:
- **Mutación**: Se crea un vector mutado combinando tres vectores aleatorios.
- **Cruzamiento**: El vector mutado se mezcla con el vector objetivo.
- **Selección**: El mejor vector reemplaza al actual si mejora el rendimiento.
- **Repetición**: El proceso se repite hasta alcanzar un criterio de parada.

Características:
- **Basado en población**, no requiere derivadas, y es simple de implementar.
- **Buena exploración** para evitar óptimos locales.
- **Versátil** para problemas continuos y discretos.

### Parámetros:
- **F**: Factor de escala.
- **CR**: Tasa de cruce.
- **NP**: Tamaño de población.
------------
- **Tarea 2**
📝 Este código simula un **enjambre de partículas** utilizado en algoritmos de optimización, donde cada partícula tiene una posición y velocidad en un espacio bidimensional.

Componentes:
- **Clase `Particula`**: Representa una partícula con una posición aleatoria dentro de los límites definidos, una velocidad inicial de cero, y un valor y memoria asociados a su mejor posición encontrada.
- **Clase `Enjambre`**: Contiene un conjunto de partículas. Permite crear un enjambre con partículas aleatorias, agregar partículas adicionales y mostrar el estado del enjambre.

Funciones principales:
1. **crear**: Crea un enjambre con n_particulas aleatorias dentro de los límites especificados.
2. **agregar_particula**: Añade una partícula al enjambre.
3. **mostrar_enjambre**: Muestra las partículas del enjambre.
------------
- **Tarea 3**
📝 Este código implementa un **algoritmo de optimización por enjambre de partículas (PSO)** para resolver el **Problema del Agente Viajero (TSP)**. Cada partícula en el enjambre representa una ruta entre ciudades y busca minimizar la distancia total de la ruta.

Componentes:
- **Clase Particula**: Representa una partícula con una posición (ruta de ciudades), velocidad, valor (distancia total de la ruta), y su mejor posición encontrada.
- **Clase Enjambre**: Contiene el conjunto de partículas y gestiona sus movimientos en busca de la mejor solución. Utiliza el algoritmo PSO para actualizar las posiciones de las partículas basadas en la mejor solución global.
- **Funciones**:
  - **funcion_objetivo_tsp**: Calcula la distancia total de una ruta (suma de distancias entre ciudades consecutivas).
  - **generar_matriz_distancias**: Genera una matriz de distancias aleatorias entre las ciudades.
  - **optimizar_enjambre**: Ejecuta el algoritmo PSO para encontrar la mejor ruta.

### Funcionamiento:
- **Inicialización**: Se crean partículas con rutas aleatorias y se evalúa su distancia.
- **Movimiento**: Cada partícula actualiza su ruta basada en la mejor ruta global y su propio historial.
- **Evaluación**: Se evalúan las rutas del enjambre y se actualiza la mejor solución encontrada.
