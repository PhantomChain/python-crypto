class PhantomCryptoException(Exception):
    pass


class PhantomSerializerException(PhantomCryptoException):
    """Raised when there's a serializer related issue"""


class PhantomInvalidTransaction(PhantomCryptoException):
    """Raised when transaction is not valid"""
