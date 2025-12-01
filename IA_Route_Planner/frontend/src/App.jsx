import { useState } from 'react'
import RouteForm from './components/RouteForm'
import ResultsCard from './components/ResultsCard'

function App() {
  const [results, setResults] = useState(null)

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="max-w-4xl w-full bg-white rounded-lg shadow-lg p-6">
        <h1 className="text-3xl font-bold text-center mb-6 text-gray-800">IA Route Planner</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <RouteForm onResults={setResults} />
          <ResultsCard results={results} />
        </div>
      </div>
    </div>
  )
}

export default App