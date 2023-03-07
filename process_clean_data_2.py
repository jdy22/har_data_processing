import numpy as np
import scipy.io as scio
import pickle

folder = "/home/joanna/clean_data/csi_mat_20230303/"

all_data = []
labels = []

print("Starting data processing...")

for activity in ["jump_sit", "jump_run", "sit_stand", "walk_sit", "jump_stand", "stand_run", "jump_walk", "walk_run", "sit_run", "walk_stand"]:
    label = np.array([0, 0, 0, 0, 0])
    if "jump" in activity:
        label[0] = 1
    if "run" in activity:
        label[1] = 1
    if "sit" in activity:
        label[2] = 1
    if "stand" in activity:
        label[3] = 1
    if "walk" in activity:
        label[4] = 1
    assert label.sum() == 2

    for index in range(1, 121):
        filename = "csi_c_2p_" + activity + "_" + str(index).rjust(3, "0") + ".mat"

        # Account for missing file
        if activity == "stand_run" and index == 95:
            continue
        
        path = folder + filename
        data = scio.loadmat(path)["var_mat"]
        data = np.abs(data) # Take amplitude for CSI information
        data = np.reshape(data, -1)

        all_data.append(data)
        labels.append(label)

    print(activity + " finished...")

print("Data processing finished!")

print(len(all_data))
print(len(labels))

# Write out data files
print("Writing out data...")
out = [all_data, labels]
with open("clean_data_2.pk1", "wb") as target:
    pickle.dump(out, target)

print("Done")