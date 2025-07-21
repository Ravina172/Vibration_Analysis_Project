##1. Loading Dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data (vibration amplitude over time)
data = pd.read_csv('bike_vibration_data.csv')  # Replace with your local path if needed
signal = data['Amplitude'].values

# Set parameters
fs = 1000  # Sampling rate (1000 samples per second)
t = np.linspace(0, 1, len(signal), endpoint=False)

# Plot time domain signal
plt.figure(figsize=(10, 4))
plt.plot(t, signal)
plt.title("Time Domain: Simulated Vibration Signal of 2W Chassis")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("vibration_time_plot.png")  # Save for interview
plt.show()

##2. Applying FFT (Frequency Domain Analysis)

from scipy.fft import fft

# Apply FFT
N = len(signal)
fft_result = fft(signal)
frequencies = np.fft.fftfreq(N, 1/fs)
magnitude = 2.0 / N * np.abs(fft_result[:N // 2])  # Only positive frequencies

# Plot frequency domain
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:N // 2], magnitude)
plt.title("Frequency Domain: FFT of Vibration Signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("vibration_fft_plot.png")  # Save for interview
plt.show()

##3. Detect Critical Vibration Frequencies

# Threshold to identify possible resonant frequencies
threshold = 0.15
critical_freqs = frequencies[:N//2][magnitude > threshold]

print("🚨 Critical Frequencies Detected:")
for freq in critical_freqs:
    print(f"{freq:.2f} Hz")


