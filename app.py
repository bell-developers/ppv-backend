from flask import Flask, jsonify
from falseData import falseProducts

app = Flask(__name__)


@app.route('/catalogo')
def devolverProductos():
    return jsonify(falseProducts)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
