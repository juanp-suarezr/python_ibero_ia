# Guion de Video IA Route Planner (5 minutos)

## Introducción (30s)
- Hola, soy [Nombre]. Hoy presento IA Route Planner, un sistema inteligente para rutas en transporte masivo.
- Implementa algoritmos de búsqueda y base de conocimiento Prolog.

## Base de Conocimiento (1 min)
- Mostrar knowledge_base.txt.
- Explicar hechos: edge(EstacionA, EstacionB, 5). para conexiones con costo.
- closed(EstacionC). para estaciones cerradas.
- Parser valida sintaxis y construye grafo.

## Algoritmos de Búsqueda (1 min)
- Dijkstra: camino más corto por costo, O((V+E) log V).
- A*: Dijkstra con heurística (actualmente 0, extensible a Manhattan).
- BFS: búsqueda por anchura, costo = aristas.
- Manejan estaciones cerradas.

## Demo CLI (1 min)
- Ejecutar: `python main.py --start EstacionA --goal EstacionF --algorithm dijkstra`
- Mostrar salida: ruta, costo, nodos expandidos, tiempo.
- Cambiar a A* y BFS.

## Demo Frontend (1 min)
- Abrir navegador en localhost:5173.
- Ingresar datos en formulario.
- Calcular ruta, mostrar resultados.
- Probar con estaciones cerradas.

## Conclusiones (30s)
- Proyecto cumple requisitos: reglas lógicas, algoritmos, frontend responsive.
- Aprendizajes: implementación de algoritmos, integración full-stack.
- Futuro: heurísticas mejores, más algoritmos, base de datos.
- Gracias por ver. Preguntas?