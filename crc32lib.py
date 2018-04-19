# !/usr/bin/python
# -*- coding: UTF-8 -*-
import binascii


class crc32:
    def __init__(self):
        self.crc = binascii.crc32(bytes())

    def update(self, buff: bytes):
        self.crc = binascii.crc32(buff, self.crc)

    def hexdigest(self):
        return '{:08x}'.format(self.crc)


if __name__ == '__main__':
    crc = crc32()
    print(crc.hexdigest())
    crc.update(b'hello world')
    print(crc.hexdigest())
    crc2 = crc32()
    crc2.update(b'hello')
    crc2.upate(b' world')
    print(crc2.hexdigest())
