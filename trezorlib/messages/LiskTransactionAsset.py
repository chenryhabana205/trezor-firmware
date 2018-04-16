# Automatically generated by pb2py
from .. import protobuf as p
from .LiskDelegateType import LiskDelegateType
from .LiskMultisignatureType import LiskMultisignatureType
from .LiskSignatureType import LiskSignatureType


class LiskTransactionAsset(p.MessageType):
    FIELDS = {
        1: ('signature', LiskSignatureType, 0),
        2: ('delegate', LiskDelegateType, 0),
        3: ('votes', p.UnicodeType, p.FLAG_REPEATED),
        4: ('multisignature', LiskMultisignatureType, 0),
        5: ('data', p.UnicodeType, 0),
    }
