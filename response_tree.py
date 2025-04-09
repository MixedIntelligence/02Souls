# response_tree.py

import numpy as np
from fake_oscillator import slime_oscillator

def interpret_signal(voltage):
    """Basic slime mold brain: decision tree"""
    if voltage > 0.2:
        return "MOVE_FORWARD"
    elif voltage < -0.2:
        return "TURN_LEFT"
    else:
        return "PAUSE"

def simulate_behavior_loop():
    t, signal = slime_oscillator(num_points=200)
    for i in range(len(t)):
        action = interpret_signal(signal[i])
        print(f"t={t[i]:.2f}s | V={signal[i]:.3f}V → Action: {action}")
        
if __name__ == "__main__":
    simulate_behavior_loop()
