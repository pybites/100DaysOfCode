from collections import defaultdict, Counter
import glob
import os
import re

from stdlib import is_std_lib

index = defaultdict(set)

import_regex = re.compile('^(?:from|import)\s(?P<module>\w+).*')

path = os.path.dirname(os.path.abspath(__file__))
dirname = os.path.dirname(path)


def get_dirs():
    for path in glob.glob('{}/[0-9]*'.format(dirname)):
        yield path


def get_files(path):
    for fi in os.listdir(path):
        if fi.endswith('.py'):
            yield os.path.join(path, fi)


def get_lines(script):
    with open(script) as f:
        for line in f:
            yield line


def _is_package(dirname, day, mod):
    mod_dir = os.path.join(dirname, day, mod)
    return os.path.isdir(mod_dir)


if __name__ == '__main__':
    for path in get_dirs():
        day = os.path.basename(path)
        for script in get_files(path):
            for line in get_lines(script):
                m = import_regex.match(line)
                if m:
                    mod = m.groupdict()['module']
                    index[mod].add(day)

    cnt = Counter()

    min_scripts = 1  # set to higher to limit output to most used modules

    for mod, scripts in sorted(index.items()):
        if len(scripts) < min_scripts:
            continue

        if mod == 'common' or \
            any(_is_package(dirname, day, mod) or
                glob.glob(os.path.join(dirname, day, mod + '.py'))
                for day in scripts):
            source = 'own'
        else:
            source = 'stdlib' if is_std_lib(mod) else 'pypi'
        cnt[source] += 1
        appeared_in = ', '.join(sorted(scripts))
        print(f'{mod:<18} | {source:<6} | {appeared_in}')

    total = sum(cnt.values())
    print()
    for source, count in cnt.most_common():
        print(f'{source:<10}: {count:>3} ({count/total*100:.1f}%)')
    print('-' * 30)
    print(f'Total: {total}')
