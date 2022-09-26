from base64 import b64encode
import os


def openImage(path):
    with open(os.path.abspath(path), 'rb') as file:
        bytes = file.read()
    return str(b64encode(bytes))
