import json
from pathlib import Path

from currency_converter import CurrencyConverter
c = CurrencyConverter()

def generator():
    with open(str(Path(__file__).with_name('scaleway.json'))) as f:
        plans = json.load(f)['plans']
    for plan in plans:
        plan = {
            'provider': 'Scaleway<sup>†</sup>',
            'provider_slug': 'scaleway',
            'url': 'https://www.scaleway.com/',
            'id': 'scaleway-' + plan['name'],
            'name': plan['name'],
            'cost': c.convert(plan['price_eur_mo'], 'EUR', 'USD'),
            'ram': plan['memory_gb'],
            'storage': plan['storage_gb'],
        }
        yield plan
