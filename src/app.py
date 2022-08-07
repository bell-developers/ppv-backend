from flask import Flask, jsonify
from adapters.adaptCatalog import adaptCatalog
from adapters.adaptImages import adaptImages
from config import config
from flask_mysqldb import MySQL
from services.getAllImages import getAllImages
from services.getAllProducts import getAllProducts

app = Flask(__name__)

dbConnection = MySQL(app)


@app.route('/catalog')
def getProducts():
    allProductsData = getAllProducts(dbConnection)
    adaptedImages = adaptImages(getAllImages(dbConnection))
    adaptedData = adaptCatalog(allProductsData, adaptedImages)
    response = jsonify(adaptedData)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.config.from_object(config["development"])
    app.run()
