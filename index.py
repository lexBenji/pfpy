from path import path
from random import choice
from time import sleep as delay
from stdio import *
from characters import *

br = [list(x) for x in path]

current = None

y = 1
x = 1
py = y
px = x

drs = [
        'l',
        'h',
        'j',
        'k'
        ]
dr = None

found = False

while found == False:
    write('\033c')
    writeln(y,' ',x)
    writeln(py,' ',px)
    writeln(dr)
    writeln(current)
    br[py][x] = br[py][x].replace('2','3')
    br[y][px] = br[y][px].replace('2','3')
    br[y][x] = '2'
    for i in br:
        for j in i:
            if j == '0':
                write(pt)
            elif j == '1':
                write(wl)
            elif j == '2':
                write(ai)
            elif j == '3':
                write(gp)
            elif j == 'g':
                write(gl)
        writeln()

    if current == 'g':
        break

    delay(.15)

    if dr == None:
        dr = choice(drs)
    elif dr == 'l':
        if br[y][x + 1] == '1':
            dr = None
        else:
            px = x
            x = x + 1
            dr = None
    elif dr == 'h':
        if br[y][x - 1] == '1':
            dr = None
        else:
            px = x
            x = x - 1
            dr = None
    elif dr == 'j':
        if br[y + 1][x] == '1':
            dr = None
        else:
            py = y
            y = y + 1
            dr = None
    elif dr == 'k':
        if br[y - 1][x] == '1':
            dr = None
        else:
            py = y
            y = y - 1
            dr = None

    current = br[y][x]
