export function createCalculatorUI(root, api) {
  const inputA = root.querySelector('#input-a')
  const inputB = root.querySelector('#input-b')
  const operations = root.querySelector('#operations')
  const calculateButton = root.querySelector('#calculate')
  const resultBox = root.querySelector('#result')
  const errorBox = root.querySelector('#error')

  let selectedOperation = 'add'


  function readOperand(input) {
    const raw = input.value.trim()
    return raw === '' ? Number.NaN : Number(raw)
  }

  function selectOperation(operation) {
    selectedOperation = operation
    operations.querySelectorAll('.op').forEach((button) => {
      button.classList.toggle(
        'op--active',
        button.dataset.operation === operation
      )
    })
  }

  function showResult(value) {
    resultBox.textContent = String(value)
    resultBox.hidden = false
    errorBox.hidden = true
  }

  function showError(message) {
    errorBox.textContent = message
    errorBox.hidden = false
  }

  async function runCalculation() {
    const a = readOperand(inputA)
    const b = readOperand(inputB)

    if (!Number.isFinite(a) || !Number.isFinite(b)) {
      showError('Bitte zwei gültige Zahlen eingeben.')
      return
    }

    calculateButton.disabled = true
    try {
      const response = await api.calculate(selectedOperation, a, b)
      showResult(response.result)
    } catch (error) {
      showError(error.message)
    } finally {
      calculateButton.disabled = false
    }
  }

  operations.addEventListener('click', (event) => {
    const button = event.target.closest('.op')
    if (button) selectOperation(button.dataset.operation)
  })

  calculateButton.addEventListener('click', runCalculation)

  return { runCalculation, selectOperation, get operation() { return selectedOperation } }
}
