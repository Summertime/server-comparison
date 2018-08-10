import os

def generator():
    url = 'https://api.vultr.com/v1/plans/list'
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers).json()
    for item in response['sizes'].values():
        item = {
            'provider': 'Vultr',
            'url': 'https://www.vultr.com/?ref=7171892',
            'id': 'vultr-' + item['VPSPLANID'],
            'name': item['VPSPLANID'],
            'cost': item['price_per_month'], # USD/m
            'ram': float(item['ram'])/1024, # GB
            'storage': float(item['disk']), #GB
        }
        yield item
