# IA Route Planner

Sistema inteligente basado en conocimiento para calcular la mejor ruta en un sistema de transporte masivo local. Implementa reglas lógicas, estrategias de búsqueda (Dijkstra, A*, BFS) y un frontend responsive.

## Estructura del Proyecto

```
IA_Route_Planner/
├── backend/          # API Flask
├── frontend/         # React + Vite + Tailwind
├── main.py           # CLI
├── docs/             # Documentación
├── README.md
├── tests.md
├── .gitignore
```

## Instalación y Ejecución

### Backend

1. Navega al directorio backend:
   ```
   cd backend
   ```
2. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Ejecuta el backend:
   ```
   python app.py
   ```
   O usa el script:
   ```
   ./run.sh
   ```

### Frontend

1. Navega al directorio frontend:
   ```
   cd frontend
   ```
2. Instala dependencias:
   ```
   npm install
   ```
3. Ejecuta el frontend:
   ```
   npm run dev
   ```

## Uso

### CLI

Ejemplo:
```
python main.py --start EstacionA --goal EstacionF --algorithm dijkstra --closed EstacionC
```

Salida:
```
Path: ['EstacionA', 'EstacionG', 'EstacionH', 'EstacionF']
Cost: 18.0
Expanded nodes: [...]
Time: 0.12 ms
```

### API

POST a `http://localhost:5000/api/route` con JSON:
```json
{
  "start": "EstacionA",
  "goal": "EstacionF",
  "algorithm": "dijkstra",
  "closed": ["EstacionC"]
}
```

Respuesta:
```json
{
  "path": ["EstacionA", "EstacionG", "EstacionH", "EstacionF"],
  "cost": 18.0,
  "expanded": [...],
  "status": "ok"
}
```

### Frontend

Abre `http://localhost:5173` en el navegador. Ingresa los datos y calcula la ruta gráficamente.

## Knowledge Base

El archivo `backend/knowledge_base.txt` contiene hechos en formato Prolog:
- `edge(StationA, StationB, Cost).`
- `closed(Station).`

## Algoritmos

Utiliza NetworkX para implementaciones eficientes.

- **Dijkstra**: Camino más corto por costo.
- **A***: Dijkstra con heurística (actualmente 0, extensible a Manhattan).
- **BFS**: Búsqueda por anchura (costo = número de aristas).

## Requisitos

- Python 3.10+
- Node.js 16+

## Documentación

- `tests.md`: Casos de prueba.
- `docs/deliverable.md`: Resumen para entrega.
- `docs/video_script.md`: Guion de video.