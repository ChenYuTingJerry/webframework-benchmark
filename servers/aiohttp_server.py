from aiohttp import web

app = web.Application()


async def index(request):
    number = request.match_info["number"]
    return web.Response(
        text="{}-fib({})={}".format(__file__, number, _fib(int(number)))
    )


async def post(request):
    data = await request.post()
    number = data["fib"]
    return web.Response(
        text="{}-fib({})={}".format(__file__, number, _fib(int(number)))
    )


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)


app.router.add_get("/{number:\d+}", index)
app.router.add_post("/", post)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=5000)
