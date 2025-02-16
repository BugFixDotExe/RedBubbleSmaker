# RedBubbleSmaker - EPS to JPEG Converter with ZIP Extraction

This project extracts ZIP files from a specified folder, searches for EPS files within them, and converts those EPS files into high-quality JPEG images. The converted images are resized to 4500 x 5400 pixels, rendered at 300 DPI, and saved for further use (for example, on print-on-demand platforms like Redbubble).

## Features

- **ZIP Extraction:** Automatically scans a designated directory for ZIP files and extracts each into its own folder.
- **EPS File Detection:** Processes extracted folders and identifies EPS files by checking their file extension.
- **High-Quality Conversion:** Converts EPS files to JPEG using Pillow with the following processing steps:
    - Uses Ghostscript for high-quality EPS rendering.
    - Increases the rendered resolution via a scale factor.
    - Resizes the image to 4500 x 5400 pixels using a high-quality resampling filter.
    - Saves the final JPEG image with 300 DPI and a high quality (95).
- **Automatic Directory Management:** Creates necessary output directories (`Extracted` and `ProcessedandComplete`) if they do not exist.

## Requirements

- **Python 3.x**
- [Pillow](https://pillow.readthedocs.io/en/stable/) (version 11 or newer)
- [Ghostscript](https://www.ghostscript.com/)  *(Note: Ghostscript is required for rendering EPS files.)*

## Installation

1. **Clone this repository:**

   ```bash
   git clone [https://github.com/your-username/eps-to-jpeg-converter.git](https://github.com/your-username/eps-to-jpeg-converter.git)
   cd eps-to-jpeg-converter


2. **Install Python dependencies:**

   ```bash
   pip install Pillow
   
   
   
3. **Install Ghostscript:**

   ```bash
   sudo pacman -S ghostscript
   
   ```bash Ubuntu/Debian:
   sudo apt-get install ghostscript
   
   ```bash macOS (via Homebrew):
   brew install ghostscript
   


1. **Clone this repository:**

   ```bash
   git clone [https://github.com/your-username/eps-to-jpeg-converter.git](https://github.com/your-username/eps-to-jpeg-converter.git)
   cd eps-to-jpeg-converter


## Usage

### 1. Prepare Your ZIP Files

Place your ZIP files containing EPS images in the input directory. Update the script to reflect your input path.

For example:
```
/home/mariecurie/Desktop/Merch_RedBubble/Zip
```

### 2. Run the Script

```bash
python3 your_script.py
```

### 3. Output Structure

- **Extracted Directory:** ZIP files will be extracted here (relative to the script's location).
- **ProcessedandComplete Directory:** Converted JPEG images will be saved here.

## Code Overview

### ZIP Extraction
- Scans a specified directory for `.zip` files.
- Extracts each ZIP into its own folder under `./Extracted`.
- Tracks and processes the extraction paths.

### EPS Conversion
For each extracted folder, the script:

1. Searches for files with the `.eps` extension.
2. Opens each EPS file using `Pillow` (leveraging Ghostscript for vector rendering).
3. Uses `img.load(scale=4)` to increase the rendering resolution.
4. Converts the image to RGB and resizes it to **4500 x 5400 pixels** using `Image.Resampling.LANCZOS`.
5. Saves the image as a JPEG with **300 DPI** and quality set to **95**.

### Directory Management
- Automatically creates the required directories (`Extracted` and `ProcessedandComplete`) if they do not exist.

## Troubleshooting

### Low-Quality Output

- Ensure **Ghostscript** is properly installed and updated.
- Adjust the rendering resolution by changing the `scale` factor in `img.load(scale=4)` (e.g., try `3` or `5`).
- Confirm images are saved with high-quality settings (e.g., `quality=95`).

### Directory Issues

- Verify the input directory exists and contains ZIP files.
- Ensure the script has appropriate permissions to create directories and write files.

### Pillow Version

Ensure your Pillow version supports `Image.Resampling.LANCZOS` (available from **Pillow 11**). Update Pillow if needed:

```bash
pip install --upgrade Pillow
```

## License

This project is licensed under the [MIT License](LICENSE).

