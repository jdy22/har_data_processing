import numpy as np
import scipy.io as scio
import pickle

folder = "/home/joanna/clean_data/csi_mat_20230302/"

all_data = []
labels = []

print("Starting data processing...")

for activity in ["jump", "run", "sit", "stand", "walk"]:
    if activity == "jump":
        label = np.array([1, 0, 0, 0, 0])
    elif activity == "run":
        label = np.array([0, 1, 0, 0, 0])
    elif activity == "sit":
        label = np.array([0, 0, 1, 0, 0])
    elif activity == "stand":
        label = np.array([0, 0, 0, 1, 0])
    elif activity == "walk":
        label = np.array([0, 0, 0, 0, 1])

    for index in range(1, 121):
        filename = "csi_c_1p_" + activity + "_" + str(index).rjust(3, "0") + ".mat"
        
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
with open("clean_data_1.pk1", "wb") as target:
    pickle.dump(out, target)

print("Done")