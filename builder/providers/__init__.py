from .digitalocean import generator as digitalocean
from .scaleway import generator as scaleway
from .vultr import generator as vultr

__all__ = ['generators']

plans = [
    *digitalocean(),
    *scaleway(),
    *vultr(),
]
plans.sort(key=lambda item:item['cost'])
