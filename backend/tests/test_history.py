from ..app.calculator import add
from ..app.service import CalculatorService

def test_append_history():
  service = CalculatorService()

  listbefore = list(service.history)
  result = str(add(10, 20))
  service.append_history(("add",10,20,result))

  listafter = list(service.history)

  assert len(listafter) == len(listbefore) + 1
  
  
