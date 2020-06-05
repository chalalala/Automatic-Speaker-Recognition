import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def record():
    fs=16000 # sampling rate
    duration = 5  # seconds
    audio = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
    print "Recording Audio"
    sd.wait()
    print "Audio recording complete"
    sd.play(audio,fs)
    return fs,audio
