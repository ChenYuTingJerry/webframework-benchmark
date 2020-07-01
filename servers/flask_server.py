from flask import Flask, request

app = Flask(__name__)


@app.route("/<int:number>")
def index(number=1):
    return "{}-fib({})={}".format(__file__, number, _fib(int(number)))


@app.route("/", methods=["POST"])
def post():
    number = request.form["fib"]
    return "{}-fib({})={}".format(__file__, number, _fib(int(number)))


def _fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib(n - 1) + _fib(n - 2)


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
