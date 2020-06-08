import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def record():
    fs=16000 # sampling rate
    duration = 5  # seconds
    audio = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='float32')
    print "Recording Audio"
    sd.wait()
    print "Audio recording complete"
    return fs,audio
