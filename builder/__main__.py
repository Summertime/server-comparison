from .providers import plans

from pathlib import Path

build_dir = Path('./build/')
build_dir.mkdir()
with open(str(build_dir/'index.html'),'w') as f:
    f.write('<!doctype html>')
    f.write('<title>Server Plans</title>')
    f.write('<table>')
    f.write('<thead>')
    f.write('<tr>')
    f.write('<th scope=col>Provider')
    f.write('<th scope=col>Name')
    f.write('<th scope=col>Cost<br><span class=unit>USD/month</span>')
    f.write('<th scope=col>RAM<br><span class=unit>GB</span>')
    f.write('<th scope=col>Storage<br><span class=unit>GB</span>')
    f.write('<tbody>')
    for plan in plans:
        f.write(f'<tr data-provider="{plan["provider"].lower()}" data-planid="{plan["id"]}">')
        f.write(f'<td data-type=string>{plan["provider"]}')
        f.write(f'<td data-type=string><a href="{plan["url"]}">{plan["name"]}</a>')
        f.write(f'<td data-type=float>{plan["cost"]:.2f}')
        f.write(f'<td data-type=float>{plan["ram"]:.2f}')
        f.write(f'<td data-type=float>{plan["storage"]:.2f}')
    f.write('</table>')
