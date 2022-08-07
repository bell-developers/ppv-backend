def adaptCatalog(data, images):
    catalog = []
    for row in data:
        product = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "images": images[row[0]]
        }
        catalog.append(product)
    return catalog
