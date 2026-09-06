export const BASE_URL =
  globalThis.CALC_API_BASE_URL || 'http://localhost:5000/api'

export class ApiError extends Error {}

async function request(path, options = {}) {
  let response
  try {
    response = await fetch(`${BASE_URL}${path}`, {
      headers: { 'Content-Type': 'application/json' },
      ...options,
    })
  } catch {
    throw new ApiError('Backend nicht erreichbar.')
  }

  let body
  try {
    body = await response.json()
  } catch {
    throw new ApiError('Antwort des Servers war kein gültiges JSON')
  }

  if (!response.ok) {
    throw new ApiError(body.error || `Server antwortete mit Status ${response.status}`)
  }
  return body
}

export function calculate(operation, a, b) {
  return request('/calculate', {
    method: 'POST',
    body: JSON.stringify({ operation, a, b }),
  })
}

export function fetchOperations() {
  return request('/operations')
}
