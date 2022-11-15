from ..models.ProductRepository import ProductRepository


class ListCatalog:
    def __init__(self, repository: ProductRepository, adapter) -> None:
        self.repository = repository
        self.adapter = adapter

    def run(self):
        data = self.repository.loadCatalog()
        return self.adapter.adapt(data)
