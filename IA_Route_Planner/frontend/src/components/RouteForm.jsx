import { useState } from 'react'

const RouteForm = ({ onResults }) => {
  const [formData, setFormData] = useState({
    start: '',
    goal: '',
    algorithm: 'dijkstra',
    closed: []
  })
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleClosedChange = (e) => {
    const value = e.target.value.split(',').map(s => s.trim()).filter(s => s)
    setFormData(prev => ({ ...prev, closed: value }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    try {
      const response = await fetch('http://localhost:5000/api/route', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      })
      const data = await response.json()
      onResults(data)
    } catch (error) {
      onResults({ status: 'error', message: 'Failed to connect to backend' })
    }
    setLoading(false)
  }

  return (
    <div className="bg-gray-50 p-4 rounded-lg">
      <h2 className="text-xl font-semibold mb-4">Planificar Ruta</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-1">Estación Inicio</label>
          <input
            type="text"
            name="start"
            value={formData.start}
            onChange={handleChange}
            className="w-full p-2 border rounded"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Estación Destino</label>
          <input
            type="text"
            name="goal"
            value={formData.goal}
            onChange={handleChange}
            className="w-full p-2 border rounded"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Algoritmo</label>
          <select
            name="algorithm"
            value={formData.algorithm}
            onChange={handleChange}
            className="w-full p-2 border rounded"
          >
            <option value="dijkstra">Dijkstra</option>
            <option value="astar">A*</option>
            <option value="bfs">BFS</option>
          </select>
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Estaciones Cerradas (separadas por coma)</label>
          <input
            type="text"
            value={formData.closed.join(', ')}
            onChange={handleClosedChange}
            className="w-full p-2 border rounded"
            placeholder="e.g. EstacionC, EstacionD"
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600 disabled:bg-gray-400"
        >
          {loading ? 'Calculando...' : 'Calcular Ruta'}
        </button>
      </form>
    </div>
  )
}

export default RouteForm