from .providers import plans

from pathlib import Path

build_dir = Path('./build/')
build_dir.mkdir()
with open(str(build_dir/'index.html'),'w') as f:
    f.write('<!doctype html>')
    f.write('<title>Server Plans</title>')
    for plan in plans:
        f.write('<p>')
        f.write(plan['name'])
