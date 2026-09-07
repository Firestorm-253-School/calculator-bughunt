from ..app.calculator import add
from ..app.service import CalculatorService

def test_append_history(): # TF-01
  service = CalculatorService()

  listbefore = list(service.history)

  result = str(add(10, 20))
  entry = ("add", 10, 20, result)
  service.append_history(entry)

  listafter = list(service.history)

  assert len(listafter) == len(listbefore) + 1
  assert listafter[-1] == entry
  
  
