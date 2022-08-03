from openImage import openImage


def genFalseData(id: int):
    return {
        "id": id,
        "name": "Remera Naranja",
        "price": 5000,
        "sizes": ['S', 'M'],
        "images": [openImage(r'C:\Programming\Projects\Bell\ppv\ppv-backend\images\remera-naranja.png')]
    }


def genProducts(times: int):
    products = []
    for i in range(times):
        products.append(genFalseData(i))
    return products
