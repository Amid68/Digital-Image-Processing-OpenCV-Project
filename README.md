# Digital Image Processing with OpenCV

A comprehensive image processing project developed for the Digital Image Processing course at An-Najah National University.

## Authors
- Ameed Othman (12220692)
- Yahya Musmar (12112501)

## Description
This project demonstrates various digital image processing techniques using OpenCV and Python. It's divided into two main parts:

1. **Part 1**: A sequence of image processing operations applied to a static image
2. **Part 2**: A real-time camera filter application with multiple effect options

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Project Structure

### Part 1: Basic Image Processing Pipeline
- `main.py` - Image loading and watermarking
- `step1_grayscale_stats.py` - Grayscale conversion and statistics
- `step2_brightness_modification.py` - Brightness adjustment
- `step3_brightness_correction.py` - Histogram equalization
- `step4_add_noise.py` - Salt-and-pepper noise addition
- `step5_noise_filtering.py` - Mean and median filtering
- `step6_sharpening.py` - Image detail enhancement

### Part 2: Real-time Camera Filter Application
- `main.py` - Camera filter application with multiple modes
- `edge_detection.py` - Canny edge detection implementation
- `grayscale_quantization.py` - Intensity level reduction
- `contrast_enhancement.py` - Histogram-based contrast improvement
- `soft_appearance.py` - Bilateral filtering for soft appearance
- `cartoon_filter.py` - Stylized cartoon effect

## Features
- Grayscale conversion and statistical analysis
- Brightness modification with parameter control
- Histogram equalization for contrast enhancement
- Salt-and-pepper noise simulation and removal
- Comparison of mean and median filters
- Image sharpening with custom kernels
- Real-time camera effects with 6 different filter modes

## How to Run

### Part 1
Run each script in sequence (1-6) to see the step-by-step image processing:
```
python part1/main.py
python part1/step1_grayscale_stats.py
...
```

### Part 2
Run the camera application:
```
python part2/main.py
```

Controls:
- Press 0-5 to switch between filter modes
- Press Q to quit

Available filters:
- Normal view (0)
- Edge detection (1)
- Grayscale quantization (2)
- Contrast enhancement (3)
- Soft appearance (4)
- Cartoon filter (5)

## Project Report
For detailed information about the implementation, results, and analysis, refer to the project report PDF.
