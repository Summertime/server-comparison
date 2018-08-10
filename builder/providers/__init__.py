from .vultr import generator as vultr
from .scaleway import generator as scaleway

__all__ = ['generators']

plans = [
    *vultr(),
    *scaleway(),
]
