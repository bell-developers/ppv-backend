from flask import Flask, jsonify
from falseData import falseProducts

app = Flask(__name__)


@app.route("/catalog")
def getCatalog():
    return jsonify(falseProducts)


@app.route("/product/<id>")
def getSingleProduct(id):
    return jsonify(falseProducts[0])


if __name__ == '__main__':
    app.run(debug=True, port=4000)
