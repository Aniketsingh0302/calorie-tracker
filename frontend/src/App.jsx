import { useState } from 'react'
import OptionGroup from './OptionGroup'

const SEX_OPTIONS = [
  { value: 'MALE', label: 'Male' },
  { value: 'FEMALE', label: 'Female' },
]

const GOAL_OPTIONS = [
  { value: 'CUT', label: 'Lose weight' },
  { value: 'MAINTAIN', label: 'Maintain' },
  { value: 'BULK', label: 'Gain muscle' },
]

const ACTIVITY_OPTIONS = [
  { value: 'No Activity', label: 'No activity', hint: 'Desk job, little movement' },
  { value: 'Light Activity', label: 'Light activity', hint: 'Walks, light workouts' },
  { value: '2-3 days workout', label: 'Moderate', hint: '2-3 workouts a week' },
  { value: 'Proper Workout(4-6 days)', label: 'Very active', hint: '4-6 workouts a week' },
]

function App() {
  const [weight, setWeight] = useState('')
  const [height, setHeight] = useState('')
  const [age, setAge] = useState('')
  const [sex, setSex] = useState('MALE')
  const [goal, setGoal] = useState('MAINTAIN')
  const [activity, setActivity] = useState('No Activity')
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')
    setResult(null)

    const payload = {
      weight: Number(weight),
      height: Number(height) / 100,
      age: Number(age),
      sex,
      goal,
      activity,
    }

    try {
      const response = await fetch('http://127.0.0.1:8000/calculate_calories', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })

      if (!response.ok) {
        setError('Please check your inputs and try again.')
        return
      }

      setResult(await response.json())
    } catch (err) {
      setError('Could not reach the server. Is the backend running?')
    }
  }

  return (
    <div className="app">
      <main className="card">
        <h1>Calorie Calculator</h1>
        <p className="subtitle">Get your BMI and daily calorie target.</p>

        <form onSubmit={handleSubmit}>
          <div className="row">
            <label>
              <span>Weight (kg)</span>
              <input type="number" inputMode="decimal" step="any" required value={weight}
                onChange={(e) => setWeight(e.target.value)} />
            </label>
            <label>
              <span>Height (cm)</span>
              <input type="number" inputMode="decimal" step="any" required value={height}
                onChange={(e) => setHeight(e.target.value)} />
            </label>
          </div>

          <label>
            <span>Age</span>
            <input type="number" inputMode="numeric" required value={age}
              onChange={(e) => setAge(e.target.value)} />
          </label>

          <OptionGroup label="Sex" options={SEX_OPTIONS} value={sex} onChange={setSex} />
          <OptionGroup label="Goal" options={GOAL_OPTIONS} value={goal} onChange={setGoal} />
          <OptionGroup label="Activity level" options={ACTIVITY_OPTIONS}
            value={activity} onChange={setActivity} layout="stack" />

          <button type="submit">Calculate</button>
        </form>

        {error && <p className="error">{error}</p>}

        {result && (
          <section className="results">
            <div className="stat highlight">
              <span className="stat-label">Daily calories</span>
              <span className="stat-value">{result.calories}</span>
              <span className="stat-note">kcal per day</span>
            </div>

<div className={`stat bmi-card ${String(result.category).toLowerCase()}`}>
  <span className="stat-label">BMI</span>
  <span className="stat-value">{result.bmi}</span>
  <span className="badge">
    <span className="dot" />
    {result.category}
  </span>
</div>

            <div className="stat">
              <span className="stat-label">BMR</span>
              <span className="stat-value">{result.bmr}</span>
              <span className="stat-note">kcal at rest</span>
            </div>
          </section>
        )}
      </main>
    </div>
  )
}

export default App