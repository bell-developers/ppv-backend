from base64 import b64encode


def blobToBase64(blobImage):
    base64Image = b64encode(blobImage)
    return str(base64Image)
