import pyaudio
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100  # Sample rate in Hz
FRAMESIZE = 1024  # Frame size
NOFFRAMES = 220  # Number of frames
DURATION = 1  # Duration of the final signal in seconds
TRIGGER_THRESHOLD = 250  # Reduced amplitude threshold for the trigger
PRE_TRIGGER_SAMPLES = int(SAMPLEFREQ * 0.15)  # Include 150 ms before trigger
CUT_OFF_SAMPLES = 5000  # Number of initial samples to cut off
WINDOW_SIZE = 5  # Number of consecutive samples required above threshold

# Initialize PyAudio
p = pyaudio.PyAudio()
print("Running")

# Open the audio stream
stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                input=True, frames_per_buffer=FRAMESIZE)

# Read data from the stream
data = stream.read(NOFFRAMES * FRAMESIZE)

# Decode the raw audio data into a NumPy array
decoded = np.frombuffer(data, dtype=np.int16)

# Stop and close the audio stream
stream.stop_stream()
stream.close()
p.terminate()

# Cut off the first 5000 samples
decoded = decoded[CUT_OFF_SAMPLES:]

# Trigger function: Refine trigger to ensure robustness by requiring multiple consecutive samples
trigger_candidates = np.convolve((np.abs(decoded) > TRIGGER_THRESHOLD).astype(int),
                                  np.ones(WINDOW_SIZE, dtype=int), mode='valid')
trigger_index = np.argmax(trigger_candidates >= WINDOW_SIZE)

# Ensure some pre-trigger samples are included
trigger_index = max(0, trigger_index - PRE_TRIGGER_SAMPLES)

# Ensure the extracted signal is exactly 1 second long
num_samples_1s = SAMPLEFREQ * DURATION
end_index = trigger_index + num_samples_1s

# Extract the triggered signal and pad with zeros if needed
triggered_signal = decoded[trigger_index:end_index]
if len(triggered_signal) < num_samples_1s:
    padding = np.zeros(num_samples_1s - len(triggered_signal), dtype=np.int16)
    triggered_signal = np.concatenate((triggered_signal, padding))

# Save the processed signal
np.save("test_alex_rechts5", triggered_signal)
print("Done")

# Plot the original and triggered signals
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.title("Original Signal")
plt.plot(decoded)
plt.axvline(x=trigger_index, color='r', linestyle='--', label='Trigger Point')
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Triggered Signal (1 second)")
plt.plot(triggered_signal)
plt.tight_layout()
plt.show()
