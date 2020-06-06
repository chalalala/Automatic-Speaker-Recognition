import os

file_name = 'development_set_enroll.txt'
os.system('find dataset/ -name *.wav >' + file_name)
