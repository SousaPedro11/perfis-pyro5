from unicodedata import normalize
from uuid import uuid4


def __generate_id__():
    codigo = uuid4()
    return str(codigo)


def __equals(obj, other):
    hobj = hash(frozenset(vars(obj).items()))
    hother = hash(frozenset(vars(other).items()))
    print(obj, hobj)
    print(other, hother)
    return hobj == hother


def __remove_acento(text):
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
