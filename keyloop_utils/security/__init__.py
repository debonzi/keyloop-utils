import hashlib
from base64 import b64encode, b64decode


class BadSignatureError(Exception):
    """ Raised when decoded string signature doesn't match. """


def encode_sign(string, secret):
    signature = hashlib.sha512("{}{}".format(string, secret).encode()).hexdigest()
    raw_string = (signature + string).encode()
    return b64encode(raw_string)


def decode_signed(encoded, secret):
    raw_string = b64decode(encoded)
    value = raw_string[128:]
    if encoded != encode_sign(value.decode(), secret):
        raise BadSignatureError(
            "Signature mismatch. Ether secret is wrong or string value has been tampered"
        )
    return value
