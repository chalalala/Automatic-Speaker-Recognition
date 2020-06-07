#test_speaker.py

import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time

#path to training data
#source   = "development_set"   

modelpath = "speaker_models/"

test_file = "development_set_test.txt"        

file_paths = open(test_file,'r')

gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

#Load the Gaussian gender Models
models    = [cPickle.load(open(fname,'r')) for fname in gmm_files]
speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
              in gmm_files]

count = 0
accuracy = 0 
# Read the test directory and get the list of test audio files 
for path in file_paths:   
    
    path = path.strip()   
    print path
    test_person = path[13:path.find('-')]
    sr,audio = read(path)
    vector   = extract_features(audio,sr)
    
    log_likelihood = np.zeros(len(models)) 
    
    for i in range(len(models)):
        gmm    = models[i]         #checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
    
    winner = np.argmax(log_likelihood)
    print path,"\ndetected as - ", speakers[winner]
    count = count +1
    if (test_person.rstrip().lower() == speakers[winner].rstrip().lower()):
        accuracy = accuracy + 1
    time.sleep(1.0)
print "Accuracy rate: ",round((float(accuracy)/float(count))*100,2) , "%"


