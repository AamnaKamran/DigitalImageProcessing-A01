# DigitalImageProcessing-A01
This digital image processing assignment includes different image processing techniques, including thresholding, intensity slicing, gamma transformations, histogram plotting, and image filtering.

# 📘 Digital Image Processing Assignment

## 🔍 Overview

This repository contains solutions to several questions from a Digital Image Processing assignment using Python and OpenCV. Each function (`q1` to `q5`) demonstrates a specific image processing task such as thresholding, intensity slicing, gamma correction, histogram plotting, and image filtering.

---

## 📂 Directory Structure

```
.
├── main.py               # Main script containing all functions (q1 to q5)
├── data/                 # Folder with image files
│   ├── dental_xray.tif
│   ├── brain.tif
│   ├── 4.grain.tif
│   ├── bottle1.jpg
│   └── bottle2.jpg
```

---

## 🛠 Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

Install dependencies using:

```bash
pip install opencv-python numpy matplotlib
```

---

## 📌 Function Descriptions

### `q1()` – Thresholding and Color Highlighting

- Loads a **dental X-ray** image (`dental_xray.tif`).
- Converts it to grayscale and applies binary thresholding.
- Highlights pixels with blue channel ≥ 230 in **red**.
- Calculates and prints the percentage of affected (highlighted) pixels.

---

### `q2()` – Intensity Slicing and Pixel Count

- Loads a **brain scan** image (`brain.tif`) in grayscale.
- Performs **intensity slicing** for a specific range (200–255).
- Displays original and binary images using Matplotlib.
- Counts and prints the number of white pixels row-wise and column-wise.

---

### `q3()` – Gamma Correction

- Reads the grayscale image `4.grain.tif`.
- Applies **gamma transformation** with γ = 0.7.
- Enhances contrast using the formula: `output = c * (input^γ)`, where `c = 4`.
- Displays the transformed image.

---

### `q4()` – Histogram and Image Filtering

- Loads `4.grain.tif` and calculates the **intensity histogram**.
- Applies two box filters: `3x3` and `7x7`.
- Computes the difference between the two filtered outputs.
- Subtracts the difference from the original to produce an enhanced result.
- Displays the final enhanced image.

---

### `q5()` – Bottle Fill Detection

- Analyzes bottle images (`bottle1.jpg`, `bottle2.jpg`) to check liquid fill level.
- Converts images to grayscale and uses intensity masking to detect content.
- Calculates and prints the **filled percentage**.
- Compares with a threshold (e.g., 85%, 70%) to determine if the bottle is properly filled.

---

## ▶️ How to Run

Use the command:

```bash
python main.py
```

By default, only `q1()` is executed. To test other functions, **uncomment** the relevant function calls at the bottom of `main.py`:

```python
q1()
# q2()
# q3()
# q4()
# q5()
```

---

## 📸 Output

- OpenCV displays processed images in separate windows.
- Console prints relevant metrics like:
  - Percentage of red-highlighted areas (in `q1`)
  - Pixel distribution (in `q2`)
  - Bottle fill percentage (in `q5`)

Close image windows to proceed to the next output.
