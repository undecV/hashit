# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import hashlib

import ascii_progress_bar
import crc32lib
from setting import *

BUFFER_SIZE = 2048


def main(argv):
    import os.path
    if len(argv) <= 1:
        raise ValueError('Too few arguments.')
    paths = argv[1:]
    files = []
    for path in paths:
        if os.path.isfile(path):
            files.append(path)
        else:
            print('WARNING - IS NOT A FILE: {}'.format(path))
    for i, file in enumerate(files):
        print('{:03d}: {}'.format(i, file))
        hashit(file)
        print()


def hashit(file):
    # Method filter
    methods = []
    if sw['sha1']:
        sha1 = hashlib.sha1()
        methods.append(('sha1', sha1))
    if sw['sha224']:
        sha224 = hashlib.sha224()
        methods.append(('sha224', sha224))
    if sw['sha256']:
        sha256 = hashlib.sha256()
        methods.append(('sha256', sha256))
    if sw['sha384']:
        sha384 = hashlib.sha384()
        methods.append(('sha384', sha384))
    if sw['sha512']:
        sha512 = hashlib.sha512()
        methods.append(('sha512', sha512))
    if sw['blake2b']:
        blake2b = hashlib.blake2b()
        methods.append(('blake2b', blake2b))
    if sw['blake2s']:
        blake2s = hashlib.blake2s()
        methods.append(('blake2s', blake2s))
    if sw['md5']:
        md5 = hashlib.md5()
        methods.append(('md5', md5))
    if sw['crc32']:
        crc32 = crc32lib.crc32()
        methods.append(('crc32', crc32))

    # Calc hash
    file_size = os.path.getsize(file)
    seek = 0
    apb = ascii_progress_bar.AsciiProgressBar(value=seek, maximum=file_size)
    print('{} {}/{}'.format(apb, seek, file_size), end='')
    with open(file, "rb") as f:
        while True:
            buff = f.read(BUFFER_SIZE)
            if not buff:
                break
            seek += len(buff)
            apb.value = seek
            for mathod, func in methods:
                func.update(buff)
            print('\r{} {:.2f}% {}/{}'.format(apb, apb.percentage*100, seek, file_size), end='')
    print()

    # Print
    for mathod, func in methods:
        digest = func.hexdigest()
        if op['uppercase']:
            digest = digest.upper()
        print('{:>7}: {}'.format(mathod, digest))

    # Log with YAML
    if op['yaml']:
        import yaml
        from yaml_setting import yaml_setting

        data = {'file': os.path.basename(file)}
        for mathod, func in methods:
            digest = func.hexdigest()
            if op['uppercase']:
                digest = digest.upper()
            data[mathod] = digest
        with open(file + '.hash.yaml', 'w', encoding='utf-8') as f:
                yaml.dump(data, f, **yaml_setting)


if __name__ == '__main__':
    import sys
    main(sys.argv)
