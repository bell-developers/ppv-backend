from ..models.ProductRepository import ProductRepository


class MySQLProductRepository(ProductRepository):
    def loadCatalog(self, dbConnection):
        query = "select * from product;"
        dbCursor = dbConnection.connection.cursor()
        dbCursor.execute(query)
        data = dbCursor.fetchall()
        return data
