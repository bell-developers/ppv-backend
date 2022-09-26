from base64 import b64encode


def openImage(path):
    with open(path, 'rb') as file:
        bytes = file.read()
    return str(b64encode(bytes))
