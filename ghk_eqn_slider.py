"""
Slider to study GHK Equation. Vm vs [K]o for different [K]i, [Na]i, [Na]o and alpha
Written by Darshan Mandge
05-October-2018
Please report any bugs or improvements by mailing at darshanmandge at iitb.ac.in
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.4)
ko = np.arange(0, 200.0, 0.1)

ki  = 150
nai = 10
nao = 150
alpha = 0.01
T = 298 

ki0 = 150
nai0 = 10
nao0 = 150
alpha0 = 0.01
T0 = 298    # Kelvin

delta = 0.01

R = 8.314   # J/mol-K
T = 298     # Kelvin
n = 1       # valence
F = 96500

# Ek = RT/nF ln((alpha*nao+ko)/(alpha*nai+ki))
Ek = 1000*(R*T)/(n*F)*np.log(np.divide((alpha*nao+ko),(alpha*nai+ki)))

l, = plt.plot(ko, Ek, lw=2, color='red')
plt.axis([0, 150, -100, 100])
plt.ylabel('Membrane Potential, V$_m$ (mV)')
plt.xlabel('Extracellular Potassium Concentration, [K]$_o$ (mM)')
plt.title('GHK Equation V$_m$ vs [K]$_o$ for different parameters')

axcolor = 'lightgoldenrodyellow'
# ko = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axiski = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axisnai = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axisnao = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
axisalpha = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
axistemp = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)

kiamp = Slider(axiski, '[K]$_i$', 0.1, 150.0, valinit=ki0, valstep=delta)
naiamp = Slider(axisnai, '[Na]$_i$', 0.1, 150.0, valinit=nai0, valstep=delta)
naoamp = Slider(axisnao, '[Na]$_o$', 0.1, 150.0, valinit=nao0, valstep=delta)
alphaamp = Slider(axisalpha, 'alpha = P$_{Na}$/P$_K$', 0.1, 10.0, valinit=alpha0, valstep=delta)
tempamp = Slider(axistemp, 'Temperature (Kelvin)', 283, 323, valinit=T0, valstep=delta)

# samp  = Slider(axamp, '[K]i', 0.1, 10.0, valinit=a0)


def update(val):
    ampki =kiamp.val
    ampnai =naiamp.val
    ampnao =naoamp.val
    ampalpha =alphaamp.val
    ampT =tempamp.val
    l.set_ydata(1000*(R*ampT)/(n*F)*np.log(np.divide((ampalpha*ampnao+ko),(ampalpha*ampnai+ampki))))
    fig.canvas.draw_idle()

kiamp.on_changed(update)
naiamp.on_changed(update)
naoamp.on_changed(update)
alphaamp.on_changed(update)
tempamp.on_changed(update)


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# plt.axes([0.025, 0.2, 0.15, 0.15])
# plt.axes([0.025, 0.3, 0.15, 0.15])
# plt.axes([0.025, 0.4, 0.15, 0.15])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    kiamp.reset()
    naiamp.reset()
    naoamp.reset()
    alphaamp.reset()

button.on_clicked(reset)

#plt.axes([0.025, 10, 0.15, 0.15], facecolor=axcolor)


plt.show()