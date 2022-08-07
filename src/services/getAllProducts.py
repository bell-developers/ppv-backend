sqlQuery = """
    select p.id_product, p.name, p.price
    from product p;
"""


def getAllProducts(dbConnection):
    cursor = dbConnection.connection.cursor()
    cursor.execute(sqlQuery)
    return cursor.fetchall()
