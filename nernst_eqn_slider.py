"""
Slider to study Nernst Equation. EK vs [K]o for different [K]i


Written by Darshan Mandge
05-October-2018
Please report any bugs or improvements by mailing to darshanmandge at iitb.ac.in
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.3)

#fig, ax = plt.plot()
#plt.plot(left=0.25, bottom=0.25)

delta = 0.01
ko = np.arange(0, 200.0, delta)
ki = 150
ki0 = 150

T = 298     # Kelvin
T0 = 298

R = 8.314   # J/mol-K
n = 1       # valence
F = 96500

# Ek = RT/nF ln(ko/ki)
Ek = 1000*(R*T)/(n*F)*np.log(np.divide(ko,ki)) #mV


l, = plt.plot(ko, Ek, lw=2, color='red')
# l, = plt.semilogx(ko, Ek, lw=2, color='red')
plt.grid()

plt.axis([0, 150, -150, 100])
plt.ylabel('Nernst Potential, E$_K$ (mV)')
plt.xlabel('Extracellular Potassium Concentration, [K]$_o$ (mM)')
plt.title('E$_K$ vs [K]$_o$ for different [K]$_i$ & Temp')
#plt.tight_layout(rect=(0,0.125,1,1))

axcolor = 'lightgoldenrodyellow'
axiski = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
kiamp = Slider(axiski, '[K]$_i$ (mM)', 0.1, 150.0, valinit=ki0, valstep=delta)

axistemp = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
tempamp = Slider(axistemp, 'Temperature (Kelvin)', 283, 323, valinit=T0, valstep=delta)

def update(val):
    ampki =kiamp.val
    ampT =tempamp.val
    l.set_ydata(1000*(R*ampT)/(n*F)*np.log(np.divide(ko,ampki)))
    fig.canvas.draw_idle()
kiamp.on_changed(update)
tempamp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    kiamp.reset()
    tempamp.reset()
button.on_clicked(reset)

plt.show()


# plt.tight_layout(pad=2,h_pad=2,w_pad=2)
# rect (left, bottom, right, top) 
