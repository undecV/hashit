import os.path

py = os.path.abspath(os.path.join(os.path.dirname(__file__), 'hashit.py'))
bat = os.path.abspath(os.path.join(os.path.dirname(__file__), 'hashit.bat'))
s = '@echo off\npython {} %*\npause'.format(py)

with open(bat, 'w', encoding='utf-8') as f:
    f.write(s)

print('Done.')
