from flask import Flask, jsonify
from falseData import falseProducts
from config import serverConfig
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión a MySQL
dbConnection = MySQL(app)


@app.route("/catalog")
def getCatalog():
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
        }
        # Insertamos en la lista los datos ya formateados
        catalog.append(newProduct)
    # Le devolvemos al cliente la lista de datos formateados
    return jsonify(catalog)


@app.route("/product/<id>")
def getSingleProduct(id):
    dbCursor = dbConnection.connection.cursor()
    dbCursor.execute("select * from product where id_product = " + str(id))
    returnedData = dbCursor.fetchall()
    firstProduct = returnedData[0]
    newProduct = {
        "id": firstProduct[0],
        "name": firstProduct[1],
        "price": firstProduct[2]
    }
    return jsonify(newProduct)


if __name__ == '__main__':
    # Configuración de servidor y conexión a BD
    app.config.from_object(serverConfig["development"])
    app.run(port=5000)
