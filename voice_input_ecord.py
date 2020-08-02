import sounddevice
from scipy.io.wavfile import write

#Voice Recording
fs=44100
second=10
print("Recording....")
recor_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
record =write("outpur.wav",fs,recor_voice)