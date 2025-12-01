# Pruebas IA Route Planner

## Casos de Prueba

### Caso 1: Ruta básica con Dijkstra
- **Comando CLI**: `python main.py --start EstacionA --goal EstacionF --algorithm dijkstra`
- **Salida esperada**:
  ```
  Path: ['EstacionA', 'EstacionG', 'EstacionH', 'EstacionF']
  Cost: 18.0
  Expanded nodes: [...]
  Time: X.XX ms
  ```

### Caso 2: Ruta con estación cerrada
- **Comando CLI**: `python main.py --start EstacionA --goal EstacionF --algorithm dijkstra --closed EstacionC`
- **Salida esperada**:
  ```
  Path: ['EstacionA', 'EstacionB', 'EstacionD', 'EstacionE', 'EstacionF']
  Cost: 22.0
  Expanded nodes: ['EstacionA', 'EstacionB', 'EstacionD', 'EstacionE', 'EstacionF']
  Time: X.XX ms
  ```

### Caso 3: Ruta con A*
- **Comando CLI**: `python main.py --start EstacionA --goal EstacionF --algorithm astar`
- **Salida esperada**: Igual que Caso 1 (ya que heurística = 0)

### Caso 4: Ruta con BFS
- **Comando CLI**: `python main.py --start EstacionA --goal EstacionF --algorithm bfs`
- **Salida esperada**:
  ```
  Path: ['EstacionA', 'EstacionB', 'EstacionC', 'EstacionD', 'EstacionE', 'EstacionF']
  Cost: 5.0  # Número de aristas
  Expanded nodes: ['EstacionA', 'EstacionB', 'EstacionC', 'EstacionD', 'EstacionE', 'EstacionF']
  Time: X.XX ms
  ```

## Casos Excepcionales

### Caso E1: Estación no existe
- **Comando CLI**: `python main.py --start EstacionX --goal EstacionF --algorithm dijkstra`
- **Salida esperada**:
  ```
  Error: Start or goal not in knowledge base
  ```

### Caso E2: No hay ruta
- **Comando CLI**: `python main.py --start EstacionA --goal EstacionF --algorithm dijkstra --closed EstacionB,EstacionE`
- **Salida esperada**:
  ```
  No path found
  ```

### Caso E3: Archivo KB no encontrado
- Modificar `--kb` a archivo inexistente
- **Salida esperada**: Errores de parsing

## Pruebas API

Usar curl o Postman para POST a `/api/route`.

Ejemplo:
```bash
curl -X POST http://localhost:5000/api/route \
  -H "Content-Type: application/json" \
  -d '{"start": "EstacionA", "goal": "EstacionF", "algorithm": "dijkstra"}'
```

Respuesta esperada: JSON como en README.

## Pruebas Frontend

1. Abrir frontend en navegador.
2. Ingresar datos y verificar resultados.
3. Probar con estaciones cerradas.
4. Verificar responsive en móvil.