from flask import Flask, jsonify
from falseData import falseProducts
from flask_cors import CORS

from genProducts import genProducts

app = Flask(__name__)
CORS(app)


@app.route('/catalog/')
def getProducts():
    return jsonify(falseProducts)


@app.route('/catalog/<times>')
def getProductsMock(times):
    numberOfProducts = int(times)
    return jsonify(genProducts(numberOfProducts))


@app.route('/product/<id>')
def getSingularProduct(id):
    return jsonify(falseProducts[0])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
