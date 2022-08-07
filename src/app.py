from flask import Flask, jsonify
from falseData import falseProducts
from config import serverConfig
from flask_mysqldb import MySQL

app = Flask(__name__)

dbConnection = MySQL(app)


@app.route("/catalog")
def getCatalog():
    return jsonify(falseProducts)


@app.route("/product/<id>")
def getSingleProduct(id):
    return jsonify(falseProducts[0])


if __name__ == '__main__':
    app.config.from_object(serverConfig["development"])
    app.run(port=5000)
