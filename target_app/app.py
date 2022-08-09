from flask import Flask, Response
import os

app = Flask(__name__)


@app.route('/')
def default():
    return Response(f'Instance address - {os.environ["ENDPOINT"]}.', status=200)


@app.route('/healthcheck')
def healthcheck():
    return Response('Ok', status=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ['PORT']), debug=True)
