from base64 import b64encode


def getImageAsBase64(path):
    with open(path, 'rb') as file:
        binaryData = file.read()
    return str(b64encode(binaryData))
