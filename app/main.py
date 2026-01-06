from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/calc')
def calculator(a: float = Query(...), b:float=Query(...), op: str=Query('add')):
  if op == 'add':
    result = a+b
  elif op == 'sub':
    result = a-b
  elif op == 'mul':
    result = a*b
  elif op == 'div':
    result = a/b
  else:
    result = 'Invalid opreations'
  
  return {'a':a,'b':b,'opreations':op,'result': result}

 