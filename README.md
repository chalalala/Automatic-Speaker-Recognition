#  Speaker Identification Using GMMs
This is done for final project of Digital Signal Processing.  

The code and instruction is written (or modified) for Linux and is made to be more suitable for our usage. In Window, there will be some differences in paths and commands.

## Installation
### 1. Install Anacoda 64-bit Python 2.7 version
Go to the following link: Anaconda.com/downloads.
Copy the bash (.sh file) installer link.  

Open command line  
Use wget to download the bash installer
```
$ cd ~
$ mkdir tmp
$ cd tmp
$ wget <bash-link>
```

Run the bash script to install Anacoda
```
$ ls <bash file of Anacoda>
$ bash <bash file of Anacoda>  
```

Source the .bash-rc file to add Anacoda to your PATH
```
$ cd ~
$ source .bashrc
```

Verify the installation
```
$ python

Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 18:21:58)
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### 2. Install packages
Required packages:  
- python_speech_features
- sklearn
- scipy
- sounddevice
To install package
```
pip install <package-name>
```
In case `pip` is not downloaded
```
apt install python-pip
```

### 3. Install PortAudio library
To install `libportaudio2`
```
sudo apt-get install libportaudio2
```

## Dataset
Audios using for this project will be stored in *development_set*
### 1. Training Data
Dataset (file to be trained) need to be located in folder *dataset*.  
File name must be in the format "Name - order".
For example, Mai-01.wav  

To generate list of (path) file to be trained
```
python train_list_generator.py
``` 
A file named *speaker_models* will be produced.  
Training model will be stored in *speaker_models* folder.

### 2. Testing Data
Testing data need to be located in folder *testing_data*.  
To generate list of (path) file to be tested
```
python test_list_generator.py
```
A file named *development_set_test.txt* will be produced.

## Implementation
### 1. Training
To train model
```
python train_models.py
```

### 2. Testing
Currently, the code just test for existing testing audios (which placed in testing_data), not from the microphone. To test model (to identify who is the speaker)
```
python test_speaker.py
```

## Reference
Source code: https://github.com/abhijeet3922/Speaker-identification-using-GMMs
