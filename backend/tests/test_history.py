from ..app.calculator import add
from ..app.service import CalculatorService

def test_append_history():
  service = CalculatorService()

  listbefore = List(service.history)
  result = str(add(10, 20))
  service.append_history(("add",10,20,result))

  listafter = List(service.history)

  assert len(listafter) == len(listbefore) + 1
  
  
