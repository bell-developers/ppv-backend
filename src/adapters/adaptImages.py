from utils.bytesToBase64 import bytesToBase64


def adaptImageBlob(imageBlob):
    return bytesToBase64(imageBlob)


def adaptImages(images):
    imagesById = {}
    for image in images:
        id = image[0]
        imageBlob = image[1]
        if id in imagesById:
            imagesById[id].append(adaptImageBlob(imageBlob))
        else:
            imagesById[id] = [adaptImageBlob(imageBlob)]
    return imagesById
