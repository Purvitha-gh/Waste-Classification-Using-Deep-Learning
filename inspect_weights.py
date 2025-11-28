import h5py

file_path = "model/model_80%_binary.h5"

def print_structure(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(f"{name} -> {obj.shape}")

with h5py.File(file_path, "r") as f:
    print("\n🔍 Full structure of model file:\n")
    f.visititems(print_structure)
