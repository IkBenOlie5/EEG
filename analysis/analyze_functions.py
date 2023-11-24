"""
This code was taken from: https://github.com/ryanlopezzzz/EEG/blob/main/analysis_tools.py
The only difference is using the fourier transform from scipy instead of numpy: https://scipy.org/faq/#what-is-the-difference-between-numpy-and-scipy 
"""

import math
import time

import numpy as np
import scipy
from scipy.special import erf


def get_power_spectrum(time_series):
    """
    Applies window function and fourier transform to time_series data and returns power spectrum of FFT: ps[freq]=|FFT(x)|^2[freq]

    :param time_series: Numpy array containing the most recent ADC voltage difference measurements.
    """
    time_series_zero_mean = time_series - np.mean(time_series)
    time_series_fft = scipy.fft.fft(time_series_zero_mean)
    ps = np.abs(time_series_fft) ** 2  # Gets square of complex number
    return ps


def get_rms_voltage(ps, freq_min, freq_max, freq, time_series_len):
    """
    Gets the Root-Mean-Square (RMS) voltage of waves with frequency between freq_min and freq_max. Parseval's Theorem says:
    \sum_{i=0}^{N-1} x[i]^2 = \frac{1}{N} \sum_{i=-(N-1)}^{N-1} |FFT(x)[i]|^2
    Using this, the RMS voltage is (first formula is definition, second is implemented evaluation):
    \sqrt{ \frac{1}{N} \sum_{i=0}^{N-1} x[i]^2 } = \frac{1}{N} \sqrt{ \sum_{freq in range} |FFT(x)[freq]|^2}

    :param ps: FFT power spectrum of time_series, ps[freq] = |FFT(x)|^2[freq].
    :param freq_min: Number corresponding to minimum alpha wave frequency in Hz.
    :param freq_max: Number corresponding to maximum alpha wave frequency in Hz.
    :param freq: Numpy array of negative and positive FFT freq, fft.fftfreq of time_series
    :param time_series_len: Integer length of time_series
    """
    freq_abs = np.abs(freq)
    ps_in_range = ps[
        (freq_abs <= freq_max) & (freq_abs >= freq_min)
    ]  # Gets power spectrum for freq in range [freq_min, freq_max]
    rms = (1 / time_series_len) * np.sqrt(np.sum(ps_in_range))
    return rms


def get_brain_wave(time_series, freq_min, freq_max, freq):
    """
    Eliminates the components of time_series which have frequency above freq_max or below freq_min giving
    brain waves.
    """
    time_series_fft = scipy.fft.fft(time_series)
    freq_abs = np.abs(freq)
    time_series_fft[
        (freq_abs > freq_max) | (freq_abs < freq_min)
    ] = 0  # set frequencies outside of [freq_min,freq_max] to 0
    brain_wave_complex = scipy.fft.ifft(time_series_fft)
    brain_wave = np.real(brain_wave_complex)  # get rid of zero imaginary component
    return brain_wave