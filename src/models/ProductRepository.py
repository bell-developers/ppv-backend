class ProductRepository:
    def __init__(self, methods) -> None:
        self.methods = methods

    def loadCatalog(self):
        self.methods.loadCatalog()
