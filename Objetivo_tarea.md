Proyecto: image.pngRescate Inteligente
Objetivo:
     Implementar y comparar 3 algoritmos de búsqueda para planear rutas de rescate desde un hospital hacia zonas de emergencia representadas en un mapa como un grafo.

     Este proyecto tiene como finalidad comprender el funcionamiento de algoritmos de búsqueda informada y no informada asi como el manejo interno de las busqueda mediantes estructuras como pilas y colas.

Actividades:
1. Comprensión del código base:

Revisa main.py para entender cómo se orquestan las búsquedas.

Observa cómo se carga el grafo desde ciudad_ejemplo.json

 

2. Completar estructuras de frontera (Están implementadas parcialmente, pero es importante comprenderlas y completarlas):

Cada estudiante/equipo debe entregar implementaciones EXPLICITAS y funcionales de:

BFS en bfs.py

Debe usar cola FIFO implementada manualmente.

UCS (Disjkstra) en ucs.py

Debe usar cola de prioridad implementada manualmente, ordenando por costo acumulado.

A* en astar.py

Debe usar cola de prioridad implementada manualmente, ordenando por f(n) = g(n) + h(n).

La heurística a implementar será distancia euclidiana entre nodos (posiciones en el JSON).

NO ESTA PERMITIDO EL USO DE LIBRERIAS Y/O funciones como "deque" ó nx.shortest_path() entre otras.
3. Modificar y experimentar con:

Se deberá modificar y crear grafos en el archivo ciudad_ejemplo.json (o en archivos adicionales) con los siguientes escenarios:

Mapa base (dado en el Starter Kit)

Analizar rutas desde el hospital (nodo A) hacia cada emergencia definida.

Mapa con costos modificados

Aumentar los pesos de ciertas calles para simular tráfico pesado.

Pregunta guía: ¿qué cambia entre BFS, UCS y A*?

Mapa con varias emergencias

Definir al menos tres zonas de emergencia.

Pregunta guía: ¿qué algoritmo es más eficiente al resolver múltiples destinos?

Mapa extendido

Agregar al menos tres nodos nuevos (nuevos barrios o calles).

Pregunta guía: ¿A* sigue siendo más eficiente que UCS en todos los casos?

     Además de los experimentos con grafos descritos (mapa base, costos modificados, múltiples emergencias, mapa extendido), los alumnos deberán experimentar con al menos una nueva heurística en A*.

a) Heurísticas a usar
Distancia euclidiana (ya implementada en el código base).

Nueva heurística (1 a elegir y justificar):

Distancia Manhattan: h(n) = |x2 - x1| + |y2 - y1|

Heurística constante: h(n) = 1 (equivale a UCS en comportamiento).

Otra propuesta por ti, siempre que se justifique su lógica.

4. Formato de los resultados esperados

a) Deberás presentar los resultados en un reporte en tabla, con el siguiente formato:

        * Se debe registrar cómo cambia el rendimiento al usar heurísticas diferentes.

Ejemplo:

Grafo usado	Heurística	Camino encontrado	Costo total	Nodos visitados	Tiempo de ejecución (segundos)
Base	Euclidiana	A → C → F	5	3	0.001
Base	Manhattan	A → C → F	7	4	0.002
Base	Constante	A → C → F	3	6	0.004
b) Reflexión breve
¿La nueva heurística que elegiste ó propusiste sigue siendo admisible (es decir nunca sobreestima el costo real)?

¿Mejoró o empeoró la eficiencia comparada con la heurística euclidiana?

¿Cómo cambia el número de nodos visitados según la heurística?

 

4. Formato de entrega
Debe incluir:

Caratula con datos de la materia / tu nombre / nombre del trabajo entregado
**Explicación breve de cada algoritmo.**

Tablas de resultados para todos los experimentos (grafos + heurísticas).

Reflexiones por escenario.

Conclusión general sobre el impacto de la heurística en A*.

Evaluación
Criterio	Puntaje
BFS implementado correctamente (cola manual)	15%
UCS implementado correctamente (cola de prioridad manual)	20%
A* implementado correctamente (cola de prioridad + heurística euclidiana)	20%
Experimentación con al menos una nueva heurística en A*	10%
Experimentos: creación de grafos (mínimo 3 escenarios)	15%
Tablas de resultados completas y claras	10%
Reflexiones y conclusión	10%
Total	100%
 

Haz clic en el siguiente enlace para descargar el archivo con información estructurada que facilitara la implementación de tu proyecto:

 

📦 Starter KitDownload 📦 Starter Kit
rescate_inteligente/
├── main.py
├── grafos/
│ └── ciudad_ejemplo.json
├── algoritmos/
│  ├── bfs.py
│  ├── ucs.py
│  ├── astar.py
│    └── greedy.py (opcional)
├── utils/
│  ├── grafo_utils.py
│  └── visualizacion.py
├── requirements.txt
└── README.md
Requisitos
Python 3.9+

Instala dependencias necesarias:

pip install -r requirements.txt
Ejecución
python main.py
     Este archivo ejecuta los algoritmos y muestra las rutas desde el hospital a cada zona de emergencia. También visualizará el camino hallado con A* (puedes modificarlo para ver otros).