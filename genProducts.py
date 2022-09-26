from openImage import openImage


def genFalseData(id: int):
    return {
        "id": id,
        "name": "Remera Naranja",
        "price": 550,
        "sizes": ['S', 'M'],
        "images": [openImage(r'C:\Programming\Projects\Bell\ppv\ppv-backend\images\1.jpg')]
    }


def genProducts(times: int):
    # products = []
    # for i in range(1, times):
    #     products.append(genFalseData(i))
    # return products
    return [
        {
            "id": 1,
            "name": "Aros argolla Bali",
            "price": 550,
            "images": [openImage(r'C:\Programming\Projects\Bell\ppv\ppv-backend\images\1.jpg')]
        },
        {
            "id": 2,
            "name": "Anillo doble",
            "price": 450,
            "images": [openImage(r'C:\Programming\Projects\Bell\ppv\ppv-backend\images\2.jpg')]
        },
        {
            "id": 3,
            "name": "Aritos Estrella",
            "price": 700,
            "images": [openImage(r'C:\Programming\Projects\Bell\ppv\ppv-backend\images\3.jpg')]
        },
        {
            "id": 4,
            "name": "Aritos Flecha",
            "price": 700,
            "images": [openImage(r'C:\Programming\Projects\Bell\ppv\ppv-backend\images\4.jpg')]
        },
        {
            "id": 5,
            "name": "Aritos Ángel",
            "price": 700,
            "images": [openImage(r'C:\Programming\Projects\Bell\ppv\ppv-backend\images\5.jpg')]
        },
    ]
