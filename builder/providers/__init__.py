from .vultr import generator as vultr

__all__ = ['generators']

plans = [
    *vultr,
]
