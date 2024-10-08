# -*- coding: utf-8 -*-
"""2024.09.14-hello wolrd.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KbmJPar911j7PNrxvpP9eoilQPbKFlJ1
"""

import pylab as py

x_deg = py.arange(-180, 180+1 ,)
x_rad = py.deg2rad(x_deg)
y = py.sin(x_rad)

py.plot(x_deg, y)

py.xlabel('x (deg)')
py.ylabel('sin(x)')
py.grid(True)