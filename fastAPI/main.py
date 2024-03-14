# from fastapi import FastAPI

# app = FastAPI()
# print(app, type(app))

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get('/fib')
# async def fibo():
#     fib_series = [0, 1]
#     for i in range(2, 10):
#         next_term = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_term)
#     newJson= dict()
#     for key, value in enumerate(fib_series,0):
#         newJson[key]= value
#     return newJson
# @app.get('/fib/{n}')
# async def fibos(n):
#     fib_series = [0, 1]
#     for i in range(2, n):
#         next_term = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_term)
#     newJson= dict()
#     for key, value in enumerate(fib_series,0):
#         newJson[key]= value
#     return newJson

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/fib')
async def fibo():
    fib_series = [0, 1]
    for i in range(2, 10):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return {str(key): value for key, value in enumerate(fib_series)}

@app.get('/fib/{n}')
async def fibo(n: int):
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return {str(key): value for key, value in enumerate(fib_series)}

@app.get('/apigenerator/fibonacci/{n}')
async def fibo(n: int):
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return {str(key): value for key, value in enumerate(fib_series)}

@app.get('/apigenerator/reverse_a_string/{n}')
async def reverse_string(n: str):
    return n[::-1]

@app.post('/apigenerator/palindrome/{n}')
async def is_palindrome(n: str):
    return {"is_palindrome": n == n[::-1]}




