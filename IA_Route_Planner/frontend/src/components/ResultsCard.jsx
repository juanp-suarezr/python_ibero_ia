const ResultsCard = ({ results }) => {
  if (!results) {
    return (
      <div className="bg-gray-50 p-4 rounded-lg">
        <h2 className="text-xl font-semibold mb-4">Resultados</h2>
        <p className="text-gray-500">Ingrese los datos y calcule la ruta para ver los resultados.</p>
      </div>
    )
  }

  if (results.status === 'error') {
    return (
      <div className="bg-red-50 p-4 rounded-lg border border-red-200">
        <h2 className="text-xl font-semibold mb-4 text-red-800">Error</h2>
        <p className="text-red-700">{results.message}</p>
      </div>
    )
  }

  return (
    <div className="bg-green-50 p-4 rounded-lg border border-green-200">
      <h2 className="text-xl font-semibold mb-4 text-green-800">Resultados</h2>
      <div className="space-y-2">
        <p><strong>Ruta:</strong> {results.path.join(' → ')}</p>
        <p><strong>Costo Total:</strong> {results.cost}</p>
        <p><strong>Nodos Expandidos:</strong> {results.expanded.join(', ')}</p>
      </div>
    </div>
  )
}

export default ResultsCard