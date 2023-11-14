import matplotlib.pyplot as plt
import numpy as np
import scipy
import soundfile as sf
from analyze_functions import (get_brain_wave, get_power_spectrum,
                               get_rms_voltage)

FILE = ""
SECONDS = 10
RESAMPLE_RATE = 128
nsamples = int(SECONDS * RESAMPLE_RATE)
sinterval = 1 / RESAMPLE_RATE
freq_min = 8  # minimum frequency for alpha waves
freq_max = 12  # maximum frequency for alpha waves


data, _ = sf.read(FILE, dtype="float32")
data = scipy.signal.resample(data, nsamples)

xpoints = np.arange(0, SECONDS, sinterval)


f1, ax1 = plt.subplots()
ax1.plot(xpoints, data)
ax1.set(xlabel="Time (s)", ylabel="Voltage", title="Raw Signal")
f1.show()

ps = get_power_spectrum(data)
freq = np.fft.fftfreq(nsamples, d=sinterval)  # frequencies for FFT of data
f2, ax2 = plt.subplots()
ax2.plot(freq, ps)
ax2.set(xlabel="Frequency (Hz)", ylabel="Power", title="Power Spectrum")
f2.show()

brain_wave = get_brain_wave(data, freq_min, freq_max, freq)
f3, ax3 = plt.subplots()
ax3.plot(xpoints, brain_wave)
ax3.set(xlabel="Time (s)", ylabel="Voltage", title="Alpha Wave")
f3.show()

rms = get_rms_voltage(ps, freq_min, freq_max, freq, nsamples)
print("Alpha wave root mean square (rms) voltage is: ", rms)
input("\nPress <Enter> to exit...\n")
