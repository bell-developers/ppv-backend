def getCatalogFromMySQL(dbConnection):
    query = "select * from product;"
    dbCursor = dbConnection.connection.cursor()
    dbCursor.execute(query)
    data = dbCursor.fetchall()

    return data
