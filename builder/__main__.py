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
    f.write('<th scope=col>Cost/mo')
    f.write('<th scope=col>RAM')
    f.write('<th scope=col>Storage')
    f.write('<tbody>')
    for plan in plans:
        f.write(f'<tr data-provider="{plan["provider"].lower()}" data-planid="{plan["id"]}">')
        f.write(f'<td data-col=provider data-type=string>{plan["provider"]}')
        f.write(f'<td data-col=name data-type=string><a href="{plan["url"]}">{plan["name"]}</a>')
        f.write(f'<td data-col=cost data-type=float>{plan["cost"]:.2f} <span class=unit>USD</span>')
        f.write(f'<td data-col=ram data-type=float>{plan["ram"]:.0f} <span class=unit>MB</span>')
        f.write(f'<td data-col=storage data-type=float>{plan["storage"]:.0f} <span class=unit>GB</span>')
    f.write('</table>')
