import json
from pathlib import Path

from currency_converter import CurrencyConverter
c = CurrencyConverter()

def generator():
    with open(str(Path(__file__).with_name('scaleway.json'))) as f:
        plans = json.load(f)['plans']
    for plan in plans:
        plan = {
            'provider': 'DigitalOcean',
            'url': '#',
            'id': 'do-' + '0',
            'name': '[unknown]',
            'cost': plan['price USD/mo'],
            'ram': plan['memory GB'],
            'storage': plan['storage GB'],
        }
        yield plan
