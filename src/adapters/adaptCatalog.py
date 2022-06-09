from utils.bytesToBase64 import bytesToBase64


def adaptImageBlob(imageBlob):
    return bytesToBase64(imageBlob)


def adaptCatalog(data):
    catalog = []
    for row in data:
        product = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "images": list(
                map(adaptImageBlob, row[3].split(b';'))
            )
        }
        catalog.append(product)
    return catalog
