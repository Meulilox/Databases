import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

#PARAMETERS
N = 10
T = 10
t = np.linspace(0,T,N)
x = np.linspace(0,T,N)
y = np.linspace(0,T,N)


#%% PLOT
# create the figure and the axis
fig, ax = plt.subplots()
line1, = ax.plot(x,y, lw=2)
ax.set_xlabel('t')
ax.set_ylabel('y(t)')
plt.axis([0,10,0,10])
plt.title("Test")

# adjust the main plot to make room for the sliders
fig.subplots_adjust(bottom=0.25)

# Make a horizontal slider to control Re(A)
axA = fig.add_axes([0.25, 0.1, 0.65, 0.03])
A_slider = Slider(
    ax=axA,
    label='t',
    valmin=0,
    valmax=10,
    valinit=0,
)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    A_slider.reset()
button.on_clicked(reset)

def update(val):
    line1.set_ydata(??????)   
    fig.canvas.draw_idle()

# register the update function with each slider
A_slider.on_changed(update)

plt.show()