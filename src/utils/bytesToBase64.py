from base64 import b64encode


def bytesToBase64(bytes):
    return str(b64encode(bytes))
