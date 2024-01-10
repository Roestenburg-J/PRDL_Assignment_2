#merge all files into one dataset
import os
import h5py
import numpy as np
dir_path = r'../pdata/Intra/train/'

def get_dataset_name(file_name_with_dir):
    filename_without_dir = file_name_with_dir.split("/")[-1]
    temp = filename_without_dir.split("_")[:-1]
    datasetname = "_".join(temp)
    return datasetname

def get_label(filename):
    if 'rest' in filename:
        label = 0
    elif 'math' in filename:
        label = 1
    elif 'memory' in filename:
        label = 2
    elif 'motor' in filename:
        label = 3
    return label

def get_all_matrices(dir_path):
    dataset = []
    labels = []
    for filename in os.listdir(dir_path):
        if filename.endswith(".h5"):
            filename_path = dir_path + filename
            with h5py.File(filename_path, 'r') as f:
                dataset_name = get_dataset_name(filename_path)
                label = get_label(filename)
                matrix = f.get(dataset_name)[()]
                dataset.append(matrix)
                labels.append(label)
              

    return dataset, labels

dataset = get_all_matrices(dir_path)[0]
# subjects x sensors x time
dataset_X = np.stack(dataset) 
labels = get_all_matrices(dir_path)[1]
