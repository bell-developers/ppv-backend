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
    print(data)
    return "Consulta a la BD hecha!"


@app.route("/product/<id>")
def getSingleProduct(id):
    return jsonify(falseProducts[0])


if __name__ == '__main__':
    # Configuración de servidor y conexión a BD
    app.config.from_object(serverConfig["development"])
    app.run(port=5000)
