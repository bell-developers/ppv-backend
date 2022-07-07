from flask import Flask, jsonify
from falseData import falseProducts

app = Flask(__name__)


@app.route('/catalog')
def getProducts():
    return jsonify(falseProducts)


@app.route('/product/<id>')
def getSingularProduct(id):
    return "El id de su producto es: " + id


if __name__ == '__main__':
    app.run(debug=True, port=4000)
