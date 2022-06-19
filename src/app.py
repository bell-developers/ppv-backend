from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL
from falseData import falseData

app = Flask(__name__)

dbConnection = MySQL(app)


@app.route('/catalog')
def getProducts():
    response = jsonify(falseData)
    response.headers.add("Access-Control-Allow-Origin",
                         "*")
    return response


if __name__ == '__main__':
    app.config.from_object(config["development"])
    app.run()
