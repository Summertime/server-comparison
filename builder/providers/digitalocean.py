import json
from pathlib import Path

def generator():
    with open(str(Path(__file__).with_name('digitalocean.json'))) as f:
        plans = json.load(f)['plans']
    for plan in plans:
        plan = {
            'provider': 'DigitalOcean',
            'provider_slug': 'digitalocean',
            'url': 'https://m.do.co/c/7b3c321c35ef',
            'id': 'do-' + plan['name'],
            'name': plan['name'],
            'cost': plan['price USD/mo'],
            'ram': plan['memory GB'],
            'storage': plan['storage GB'],
        }
        yield plan
