# fake_oscillator.py

import numpy as np
import time

def slime_oscillator(num_points=1000, noise_level=0.05):
    """Generates slime mold-like voltage oscillations"""
    time_series = np.linspace(0, 50, num_points)
    signal = 0.4 * np.sin(0.2 * time_series) + \
             0.1 * np.sin(1.0 * time_series) + \
             np.random.normal(0, noise_level, num_points)
    return time_series, signal

if __name__ == "__main__":
    t, s = slime_oscillator()
    for i in range(len(t)):
        print(f"{t[i]:.2f}s → {s[i]:.3f}V")
        time.sleep(0.05)
