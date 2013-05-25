'''
Created on May 21, 2013

@author: pshu
'''
#import matplotlib.pyplot as plot
# from pylab import hist,plot
from pylab import *
import numpy as np
from matplotlib.colors import colorConverter


def pastel(colour, weight=2.4):
    """ Convert colour into a nice pastel shade"""
    rgb = np.asarray(colorConverter.to_rgb(colour))
    # scale colour
    maxc = max(rgb)
    if maxc < 1.0 and maxc > 0:
        # scale colour
        scale = 1.0 / maxc
        rgb = rgb * scale
        # now decrease saturation
    total = rgb.sum()
    slack = 0
    for x in rgb:
        slack += 1.0 - x

    # want to increase weight from total to weight
    # pick x s.t.  slack * x == weight - total
    # x = (weight - total) / slack
    x = (weight - total) / slack

    rgb = [c + (x * (1.0 - c)) for c in rgb]

    return rgb


def get_colours(n):
    """ Return n pastel colours. """
    base = np.asarray([[1, 1, 0], [0, 1, 0], [0, 0, 1]])

    if n <= 3:
        return base[0:n]

    # how many new colours to we need to insert between
    # red and green and between green and blue?
    needed = (((n - 3) + 1) / 2, (n - 3) / 2)

    colours = []
    for start in (0, 1):
        for x in np.linspace(0, 1, needed[start] + 2):
            colours.append((base[start] * (1.0 - x)) +
                           (base[start + 1] * x))

    return [pastel(c) for c in colours[0:n]]


if __name__ == '__main__':
    f = open('pie.txt', 'r')
    years = []
    lines = []
    while True:
        line = f.readline()
        if len(line) != 0:
            num_line, year = line.split()[0:2]
            lines.append(int(num_line))
            years.append(int(year))
        else:
            break

    line_rep = zip(years, lines)
    # print lines
    figure(1, figsize=[10, 10])
    ax = axes([0.1, 0.1, 0.8, 0.8])

    pie(lines, autopct='%1.2f%%', labels=["%d" % (y) for y in years], shadow=True, labeldistance=1.1,
        colors=get_colours(len(years)))
    title('Lines of Code from year', bbox={'facecolor': '0.8', 'pad': 5})
    show()
