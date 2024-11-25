import os
import zipfile

# Define input and output directories
in_folder = "in"
out_folder = "out"

# Ensure the output folder exists
os.makedirs(out_folder, exist_ok=True)

# Iterate over all ZIP files in the input folder
for file_name in os.listdir(in_folder):
    if file_name.endswith(".zip"):
        zip_path = os.path.join(in_folder, file_name)
        extract_path = os.path.join(out_folder, os.path.splitext(file_name)[0])  # Create a folder for each zip file

        # Extract the ZIP file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            print(f"Extracted: {zip_path} -> {extract_path}")