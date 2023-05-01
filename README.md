# Raw Data Preprocessing

## Introduction: 
This repository contains the raw data processing code for both the public dataset and the JPC3A dataset. 

## Datasets:
In order to train or run any of the files in this model repository, the corresponding data files must be located in your directory. 
 
### Public Dataset:
The public dataset has been provided by Yousefi et al. [1] and can be obtained online via https://github.com/ermongroup/Wifi_Activity_Recognition. 
 
### JPC3A Dataset:
Due to the size of the JPC3A dataset, it has not been provided in the repositories. However, the dataset can be accessed by contacting Julie McCann at Imperial College London. 

## Raw Data Preprocessing
Once the datasets have been obtained, the raw data processing files can be run. Please ensure that any data paths defined in the python files are changed to be compatible with your local directory. 
 
### Public Raw Data Preprocessing:
To run the raw data preprocessing on the public dataset, run the following python files:
* Public Data: “raw_data_processing.py” followed by "public_dataset_preprocessing.py"
 
### JPC3A Raw Data Preprocessing:
To run the raw data preprocessing on the JPC3A dataset, run the respective python files:
* 1 Person Clean: “process_clean_data_1.py”
* 2 Person Clean: “process_clean_data_2.py”
* 1 Person Noisy: “process_noisy_data_1.py”
* 2 Person Noisy: “process_noisy_data_2.py”

## Output Data Format: 
After running the raw data processing files, the data will be saved as a pickle file. For the public dataset this data is a list with four entries: the CSI data, pre-split into train and test sets, followed by the corresponding labels for each set. For the JPC3A dataset this data is a list composed of two entries: the CSI data and the labels. The data and the labels are an array/list (public/JPC3A) of numpy arrays with each entry corresponding to one sample. 

### Public Output Format:
For the public dataset, the length of each sample is 90000, as a sliding window of 1000 has been applied and the 1000 samples have been flattened into a 1D vector. 90 is the feature vector size which is composed of 3 transmitting antennae and 30 subcarriers. 

### JPC3A Output Data Format:
For the JPC3A dataset, the length of each data sample is N*270 where N is the number of packets received for a particular recording. 270 is the feature vector size which is composed of 3 transmitting antennae, 3 receiving antennae, and 30 subcarriers. 

The output labels of each sample is a 1x5 dimensional vector with a 1 indicating that an activity is present and a 0 indicating that an activity is not present. The activity label entries are as follows: 1 = jump, 2 = run, 3 = sit, 4 = stand, 5 = walk. Please note that data point 95 for the stand_run combination is missing from the JPC3A clean dataset.

## References:
[1] Siamak Yousefi, Hirokazu Narui, Sankalp Dayal, Stefano Ermon, and Shahrokh Valaee. A survey on behavior recognition using wifi channel state information. IEEE Communications Magazine, 55(10):98–104, 2017.
