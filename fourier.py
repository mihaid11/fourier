import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Initial parameters
frequency1 = 4
amplitude1 = 4.5
frequency2 = 5
amplitude2 = 3.5

# Graphs
x = np.linspace(0, 2 * np.pi, 1000)
fig, axs = plt.subplots(3, 1, figsize=(12, 12)) 
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.35, hspace=0.75) 

def create_wave(x, frequency, amplitude):
    return amplitude * np.sin(frequency * x)

wave1_line, = axs[0].plot(x, create_wave(x, frequency1, amplitude1), label='Wave 1')
axs[0].set_title('First Wave', fontsize=16)
axs[0].set_ylim(-8, 8)
axs[0].grid(True)
axs[0].legend()

wave2_line, = axs[1].plot(x, create_wave(x, frequency2, amplitude2), label='Wave 2', color='orange')
axs[1].set_title('Second Wave', fontsize=16)
axs[1].set_ylim(-8, 8)
axs[1].grid(True)
axs[1].legend()

combined_wave_line, = axs[2].plot(x, create_wave(x, frequency1, amplitude1) + create_wave(x, frequency2, amplitude2), label='Combined Wave', color='green')
axs[2].set_title('Combined Wave', fontsize=16)
axs[2].set_ylim(-8, 8)  
axs[2].grid(True)
axs[2].legend()

ax_freq1 = plt.axes([0.1, 0.05, 0.65, 0.03])
ax_amp1 = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_freq2 = plt.axes([0.1, 0.15, 0.65, 0.03])
ax_amp2 = plt.axes([0.1, 0.2, 0.65, 0.03])
ax_save = plt.axes([0.8, 0.1, 0.2, 0.05])

# Sliders
slider_freq1 = Slider(ax_freq1, 'Freq 1', 0.1, 7.5, valinit=frequency1)
slider_amp1 = Slider(ax_amp1, 'Amp 1', 0.1, 7.5, valinit=amplitude1) 
slider_freq2 = Slider(ax_freq2, 'Freq 2', 0.1, 7.5, valinit=frequency2)
slider_amp2 = Slider(ax_amp2, 'Amp 2', 0.1, 7.5, valinit=amplitude2) 

def update(val):
    freq1 = slider_freq1.val
    amp1 = slider_amp1.val
    freq2 = slider_freq2.val
    amp2 = slider_amp2.val

    wave1_line.set_ydata(create_wave(x, freq1, amp1))
    wave2_line.set_ydata(create_wave(x, freq2, amp2))
    combined_wave_line.set_ydata(create_wave(x, freq1, amp1) + create_wave(x, freq2, amp2))

    fig.canvas.draw_idle()

# Save image
def save_figure(event):
    plt.savefig('combined_wave.png', bbox_inches ='tight')
    print("Figure saved as 'combined_wave.png'.")

slider_freq1.on_changed(update)
slider_amp1.on_changed(update)
slider_freq2.on_changed(update)
slider_amp2.on_changed(update)

# Save button mechanic
save_button = Button(ax_save, 'Save figure')
save_button.on_clicked(save_figure)

plt.show()
