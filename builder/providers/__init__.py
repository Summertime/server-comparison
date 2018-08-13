from .vultr import generator as vultr
from .scaleway import generator as scaleway
from .digitalocean import generator as digitalocean

__all__ = ['generators']

plans = [
    *vultr(),
    *scaleway(),
    *digitalocean(),
]
plans.sort(key=lambda item:item['cost'])
