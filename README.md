# collected_data_preprocessing

- [ ] noisy_data_1.pk1 contains all of the 1-person data from the noisy room
- [ ] noisy_data_2.pk1 contains all of the 2-person data from the noisy room
- [ ] Both contain a list with two entries: the first is the data and the second is the labels
- [ ] Data and labels are both lists of numpy arrays with each entry corresponding to one data sample
- [ ] Length of each data sample is n*270, where n (<4000) is variable and is the number of packets received, and 270 is the size of the feature vector
- [ ] 270 features = 3 transmitting antennae * 3 receiving antennae * 30 subcarriers (only 90 features in the public dataset as they only use one antenna for transmission)
- [ ] Length of each label is 5, with 1 indicating that an activity is present (and 0 indicating that it is not present)
- [ ] Activity 1 = jump, 2 = run, 3 = sit, 4 = stand, 5 = walk
- [ ] Similarly for the clean data 
- [ ] Note data point 95 for stand_run is missing from the clean data (so lengths are 1 shorter than expected)