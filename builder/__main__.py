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
    f.write('<th scope=col>Cost<br>USD/month')
    f.write('<th scope=col>RAM<br>GB')
    f.write('<th scope=col>Storage<br>GB')
    f.write('<tbody>')
    for plan in plans:
        f.write('<tr>')
        f.write(f'<td>{plan["provider"]}')
        f.write(f'<td>{plan["name"]}')
        f.write(f'<td>{plan["cost"]}')
        f.write(f'<td>{plan["ram"]}')
        f.write(f'<td>{plan["storage"]}')
    f.write('</table>')
