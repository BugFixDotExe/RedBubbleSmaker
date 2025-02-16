#!/usr/bin/env python3

import os
import zipfile
from PIL import Image

# Directory containing zip files
directory = "/home/mariecurie/Desktop/Merch_RedBubble/Zip"
files = os.listdir(directory)
zip_files = []
extract_to = '../Extracted'
unzip_files_path = []

# Collect zip files only
for file in files:
    root, ext = os.path.splitext(file)
    if ext.lower() == ".zip":
        full_path = os.path.join(directory, file)
        print(full_path)
        zip_files.append(full_path)

def image_converter():
    # Ensure output directory exists
    processed_dir = '../ProcessedandComplete'
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    for folder in unzip_files_path:
        # Process each file in the extracted folder
        for file in os.listdir(folder):
            full_file_path = os.path.join(folder, file)
            root, ext = os.path.splitext(file)
            # Check extension (note the dot before eps)
            if ext.lower() == ".eps":
                try:
                    # Use the full file path when opening the image
                    with Image.open(full_file_path) as img:
                        img.load(scale=4)
                        img = img.convert("RGB")
                        # Resize to desired dimensions using LANCZOS filter
                        resized_img = img.resize((4500, 5400), Image.Resampling.LANCZOS)
                        # Save the resized image with 300 DPI
                        output_path = os.path.join(processed_dir, f"{root}.jpeg")
                        resized_img.save(output_path, "JPEG", dpi=(300, 300), quality=100)
                        print(f"Saved {output_path}")
                except Exception as e:
                    print(f"Error processing {full_file_path}: {e}")

def unzip_packages(zip_path, folder_count):
    path = os.path.join(extract_to, str(folder_count))
    # Create the extraction path if it doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(path)
        unzip_files_path.append(path)
        print(f'Extraction complete for {zip_path} into {path}')
        # Process images in the extracted folder
        image_converter()
    except Exception as e:
        print(f"Error unzipping {zip_path}: {e}")

# Ensure the extraction directory exists
if not os.path.exists(extract_to):
    os.makedirs(extract_to)

# Unzip each zip file
folder_count = 0
for zip_file in zip_files:
    unzip_packages(zip_file, folder_count)
    folder_count += 1
