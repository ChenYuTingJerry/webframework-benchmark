from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    fib: int


@app.get("/{number}")
async def read_item(number: int):
    return "{}-fib({})={}".format(__file__, number, _fib(number))


@app.post("/")
async def read_item(fib: int = Form(...)):
    return "{}-fib({})={}".format(__file__, fib, _fib(fib))


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)
