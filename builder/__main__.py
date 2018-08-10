from .providers import plans

from pathlib import Path

build_dir = Path('./build/')
build_dir.mkdir()
with open(str(build_dir/'index.html'),'w') as f:
    f.write('<!doctype html>')
    f.write('<title>Server Plans</title>')
    f.write('<table>')
    f.write('<col class=provider>')
    f.write('<col class=name>')
    f.write('<col class=cost>')
    f.write('<col class=ram>')
    f.write('<col class=storage>')
    f.write('<thead>')
    f.write('<tr>')
    f.write('<th scope=col>Provider')
    f.write('<th scope=col>Name')
    f.write('<th scope=col>Cost<br><span class=unit>USD/month</span>')
    f.write('<th scope=col>RAM<br><span class=unit>GB</span>')
    f.write('<th scope=col>Storage<br><span class=unit>GB</span>')
    f.write('<tbody>')
    for plan in plans:
        f.write(f'<tr data-planid="{plan["id"]}">')
        f.write(f'<td>{plan["provider"]}')
        f.write(f'<td><a href="{plan["url"]}">{plan["name"]}</a>')
        f.write(f'<td>{plan["cost"]:.2f}')
        f.write(f'<td>{plan["ram"]:.2f}')
        f.write(f'<td>{plan["storage"]:.2f}')
    f.write('</table>')
