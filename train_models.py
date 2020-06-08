#train_models.py

import cPickle
import numpy as np
import os
import re
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture as GMM 
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")

#path to training data
train_file = 'development_set_enroll.txt'
file_paths = open(train_file,'r')

#path where training speakers will be saved
os.system("mkdir speaker_models")
dest = "speaker_models/"        

count = 1

# Extracting features for each speaker (5 files per speakers)
features = np.asarray(())
for path in file_paths:    
    path = path.strip() 
    print path
    
    # read the audio
    sr,audio = read(path)
    
    # extract 40 dimensional MFCC & delta MFCC features
    vector   = extract_features(audio,sr)
    
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
    # when features of 5 files of speaker are concatenated, then do model training
    if count == 5:    
        gmm = GMM(n_components = 16, max_iter = 200, covariance_type='diag',n_init = 3)
        gmm.fit(features)
        
        # dumping the trained gaussian model
        seperate = path.split('/')
        path = seperate[len(seperate)-1]
        path = re.sub('.wav','',path)

        name = re.sub(" ","",path)
        picklefile = name.split("-")[0]+".gmm"
        cPickle.dump(gmm,open(dest + picklefile,'w'))
        print '+ modeling completed for speaker:',picklefile," with data point = ",features.shape    
        features = np.asarray(())
        count = 0
    count = count + 1
    
