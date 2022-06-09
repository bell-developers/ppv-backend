sqlQuery = """
        select p.id_product, p.name, p.price, i.image
        from product p 
        left join product_image i on i.id_product = p.id_product
        group by p.id_product;
    """


def getCatalog(dbConnection):
    cursor = dbConnection.connection.cursor()
    cursor.execute(sqlQuery)
    return cursor.fetchall()
