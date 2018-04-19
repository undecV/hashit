#!/usr/bin/python
# -*- coding: UTF-8 -*-


class AsciiProgressBar:
    def __init__(self, value=0, maximum=100, minimum=0, length=50, filled_char='#', unfilled_char='='):
        if value < 0 or value < minimum or value > maximum:
            raise ValueError('Value out of range.')
        if maximum < 0 or maximum < minimum or maximum < value:
            raise ValueError('Maximum out of range.')
        if minimum < 0 or minimum > maximum or minimum > value:
            raise ValueError('Minimum out of range.')
        if length <= 0:
            raise ValueError('Length out of range.')
        self._value = value
        self._maximum = maximum
        self._minimum = minimum
        self._length = length
        self.filled_char = filled_char
        self.unfilled_char = unfilled_char

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if length <= 0:
            raise ValueError('Length out of range.')
        self._length = length

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0 or value < self.minimum or value > self.maximum:
            raise ValueError('Value out of range.')
        self._value = value

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        if maximum < 0 or maximum < self.minimum or maximum < self._value:
            raise ValueError('Maximum out of range.')
        self._maximum = maximum

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        if minimum < 0 or minimum > self.maximum or minimum > self._value:
            raise ValueError('Minimum out of range.')
        self._minimum = minimum

    @property
    def percentage(self):
        return (self.value - self.minimum) / (self.maximum - self.minimum)

    def __str__(self):
        val_per_char = (self.maximum - self.minimum) / self.length
        filled = int((self.value - self.minimum) / val_per_char)
        return self.filled_char * filled + self.unfilled_char * (self.length - filled)


if __name__ == '__main__':
    import time
    apb = AsciiProgressBar(value=40, maximum=100, minimum=20, length=50, filled_char='#', unfilled_char='=')
    print('{} {:06.2f}%'.format(apb, apb.percentage * 100))

    maxi = 100
    apb_running = AsciiProgressBar(maximum=maxi, length=60)
    print('{} {:06.2f}%'.format(apb_running, apb_running.percentage * 100), end='')
    for i in range(0, maxi+1, 1):
        apb_running.value = i
        print('\r{} {:06.2f}%'.format(apb_running, apb_running.percentage * 100), end='')
        time.sleep(0.1)
