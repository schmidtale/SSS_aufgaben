import pyaudio
import numpy
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
# 225280 = samples
# length of recording: ca. 5 seconds
p = pyaudio.PyAudio()
print("running")

stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                input=True, frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES * FRAMESIZE)
decoded = numpy.frombuffer(data, "int16")
stream.stop_stream()
stream.close()
p.terminate()
numpy.save("aufnahme 2", decoded)
print("done")
plt.plot(decoded)
plt.show()

