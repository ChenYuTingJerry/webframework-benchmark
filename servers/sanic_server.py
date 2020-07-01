from sanic import response, Sanic

app = Sanic()


@app.route("/<number:int>")
async def index(request, number=1):
    return response.html("{}-fib({})={}".format(__file__, number, _fib(int(number))))


@app.route("/", methods=["POST"])
async def post(request):
    data = request.form
    number = data["fib"][0]
    return response.html("{}-fib({})={}".format(__file__, number, _fib(int(number))))


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
