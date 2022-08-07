sqlQuery = """
    select i.id_product, i.image
    from product_image i;
"""


def getAllImages(dbConnection):
    cursor = dbConnection.connection.cursor()
    cursor.execute(sqlQuery)
    return cursor.fetchall()
