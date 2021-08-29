import librosa
import matplotlib.pyplot as plt
import librosa.display
import os
import math
import string
import random

def generate_random_string(string_length = 8):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(string_length))

def generate_spectogram(file, path, jump):
    total_time = librosa.get_duration(filename = file)
    till = math.ceil(total_time / jump)
    for i in range(till):
        x, sr = librosa.load(file, offset = i * jump, duration = jump)
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'log', cmap = 'gray_r')
        plt.xlabel('')
        plt.ylabel('')
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)
        file_save = generate_random_string() + '.png'
        if not os.path.exists(path):
            os.makedirs(path)
        file_save = os.path.join(path, file_save)
        plt.savefig(file_save, dpi = 1200)
        # plt.show()

def traverse(root):
    for folder in os.listdir(root):
        print(f'switched to {folder}')
        for file in os.listdir(os.path.join(root, folder)):
            path_name = os.path.join(root, folder, file)
            if ".wav" in path_name:
                print(path_name)
                generate_spectogram(path_name, os.path.join('train_data_spectogram', folder, '_spectogram'), jump = 90)

traverse('train_data')