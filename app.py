from flask import Flask, jsonify, request
from genProducts import genProducts
from src.config import serverConfig
from flask_mysqldb import MySQL
from src.blobToBase64 import blobToBase64

app = Flask(__name__)

dbConnection = MySQL(app)


@app.route("/catalog")
def getCatalog():
    # Conseguir datos de productos
    # Consulta SQL
    query = "select * from product;"
    # Crea un cursor
    dbCursor = dbConnection.connection.cursor()
    # Ejecuta la consulta
    dbCursor.execute(query)
    # Guardamos los datos obtenidos en una variable
    data = dbCursor.fetchall()

    # Darle formato a los datos
    # Creamos una nueva lista
    catalog = []
    # Accedemos a cada producto de los datos obtenidos
    for productData in data:
        # Formateamos los datos de cada producto
        newProduct = {
            "id": productData[0],
            "name": productData[1],
            "price": productData[2],
            "images": []
        }
        getImagesQuery = f"select image from product_image where id_product = {productData[0]};"
        dbCursor.execute(getImagesQuery)
        receivedImages = dbCursor.fetchall()
        for receivedImage in receivedImages:
            newProduct["images"].append(blobToBase64(receivedImage[0]))
        # Insertamos en la lista los datos ya formateados
        catalog.append(newProduct)

    # Le devolvemos al cliente la lista de datos formateados
    return jsonify(catalog)


@app.route("/catalog/<times>")
def getCatalogByTimes(times):
    return jsonify(genProducts(app.root_path))


@app.route("/product/<id>")
def getSingleProduct(id):
    # dbCursor = dbConnection.connection.cursor()
    # dbCursor.execute("select * from product where id_product = " + str(id))
    # returnedData = dbCursor.fetchall()
    # firstProduct = returnedData[0]
    # newProduct = {
    #     "id": firstProduct[0],
    #     "name": firstProduct[1],
    #     "price": firstProduct[2],
    #     "images": []
    # }
    # dbCursor.execute(
    #     "select image from product_image where id_product = " + str(id))
    # images = dbCursor.fetchall()
    # for image in images:
    #     convertedImage = blobToBase64(image[0])
    #     newProduct["images"].append(convertedImage)
    return jsonify(genProducts(40)[int(id) - 1])


@app.route("/product", methods=["POST"])
def createProduct():
    name = request.json["name"]
    price = request.json["price"]
    query = f"insert into product (name, price) values ('{name}' , {price});"
    dbCursor = dbConnection.connection.cursor()
    dbCursor.execute(query)
    dbConnection.connection.commit()
    print(query)
    return "Product created"


if __name__ == '__main__':
    # Configuración de servidor y conexión a BD
    app.config.from_object(serverConfig["development"])
    app.run(port=5000)
