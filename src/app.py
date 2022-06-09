from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL
from falseData import falseData

app = Flask(__name__)

dbConnection = MySQL(app)


@app.route('/catalog')
def getProducts():
    return jsonify(falseData)
    # return jsonify(adaptCatalog(getCatalog(dbConnection)))


if __name__ == '__main__':
    app.config.from_object(config["development"])
    app.run()
