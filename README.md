# Interactive Image Enhancement Application Using Intensity Transformation and Histogram Analysis

## Overview

This repository contains an interactive Python-based application for evaluating digital image enhancement methods in the spatial domain. The application supports experimental analysis of grayscale image enhancement using intensity transformation and histogram-based methods.

The implemented methods include:

- Image Negative Transformation
- Power-Law Transformation / Gamma Correction
- Gray Level Slicing
- Histogram Equalization
- Histogram Matching
- Contrast Limited Adaptive Histogram Equalization (CLAHE)

## Scientific Background

Digital images often suffer from quality degradation caused by low contrast, uneven illumination, sensor limitations, and non-optimal intensity distribution. These conditions may reduce visual readability and affect subsequent image analysis processes such as segmentation, feature extraction, object detection, and classification.

This project applies two main approaches:

1. **Intensity Transformation**  
   Modifies pixel intensity values directly in the spatial domain to adjust brightness, invert intensity values, or emphasize selected gray-level ranges.

2. **Histogram-Based Enhancement**  
   Analyzes and modifies pixel intensity distribution to improve global contrast, adjust image appearance based on a reference image, or enhance local contrast adaptively.

## Research Objectives

The objectives of this project are:

- To evaluate intensity transformation methods for grayscale image enhancement.
- To analyze histogram distribution changes before and after enhancement.
- To compare enhancement methods under different image conditions.
- To observe the relationship between visual quality, histogram distribution, mean intensity, and entropy.
- To provide an interactive learning and experimental tool for digital image processing.

## Methodology

The general workflow consists of:

1. Image acquisition from standard or publicly available datasets.
2. Preprocessing, including grayscale conversion, image resizing, and pixel value standardization.
3. Application of image enhancement methods.
4. Visualization of the original image, processed image, and histogram.
5. Statistical evaluation using mean intensity and entropy.
6. Comparative analysis based on visual appearance, histogram distribution, and statistical values.

## Key Findings

The experimental results indicate that each enhancement method has different characteristics depending on the initial image condition.

- Histogram Equalization improves global contrast but may cause over-enhancement.
- CLAHE provides more stable local contrast enhancement and better preserves image details.
- Power-Law Transformation is flexible for brightness adjustment through gamma parameter selection.
- Gray Level Slicing is effective for emphasizing selected gray-level regions.
- Histogram Matching depends strongly on the selected reference image.
- No single method performs optimally for all image conditions.

## Repository Structure

```text
Interactive-Image-Enhancement-App/
│
├── image_enhancement_app.py
│   └── Main Python application
│
├── DataSet/
│   └── Test images used for experiments
│
├── figures/
│   └── Visual documentation of enhancement results
│
├── docs/
│   └── Scientific manuscript and supporting documents
│
├── requirements.txt
│   └── Python dependencies
│
└── README.md
System Requirements
Python 3.9 or later
pip
Windows, Linux, or macOS

Required Python libraries:

numpy
opencv-python
matplotlib
pillow
scipy
Installation

Clone this repository:

git clone https://github.com/Januarizky93/Interactive-Image-Enhancement-App.git
cd Interactive-Image-Enhancement-App

Create and activate a virtual environment:

Windows
python -m venv .venv
.venv\Scripts\activate
Linux or macOS
python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install --upgrade pip
pip install numpy opencv-python matplotlib pillow scipy

Or, if requirements.txt is available:

pip install -r requirements.txt
Running the Application

Run the application using:

python image_enhancement_app.py
How to Use
Click Open Image to load a test image.
Optionally, click Open Reference Image for Histogram Matching.
Adjust the gamma value if using Power-Law Transformation.
Select an enhancement method from the application panel.
Observe the processed image, histogram distribution, mean intensity, and entropy.
Compare the result with the original image.
Evaluation Metrics

This project uses two simple statistical indicators:

Mean Intensity: represents the average brightness level of an image.
Entropy: represents the complexity or variation of intensity distribution in an image.

These indicators are used as supporting measures and should not be interpreted as absolute image quality metrics.

Research Contribution

The contribution of this project includes:

Integration of multiple image enhancement methods into one interactive application.
Comparative evaluation using visual observation, histogram distribution, mean intensity, and entropy.
Real-time parameter exploration for image enhancement experiments.
Support for digital image processing learning through interactive visualization.
Practical implementation of spatial-domain image enhancement techniques using Python.
Limitations

This project has several limitations:

The evaluation uses simple statistical indicators only, namely mean intensity and entropy.
The main focus is grayscale image enhancement.
Advanced image quality metrics such as PSNR, SSIM, and NIQE are not yet implemented.
The dataset is limited to selected standard test images.
The application is desktop-based and has not yet been deployed as a web application.
Future Development

Future improvements may include:

Adding objective image quality metrics such as PSNR, SSIM, and NIQE.
Supporting batch image processing.
Adding experiment logging and automatic result comparison.
Exporting evaluation results to CSV or Excel.
Supporting color image enhancement in different color spaces.
Developing a web-based version using Streamlit or Flask.
Citation

If you use this repository for academic or research purposes, please cite:

Putra, A. J. H. (2026). Interactive Evaluation of Intensity Transformation and Histogram-Based Methods for Image Enhancement.
Author

Adhitya Januarizky Hadi Putra
Department of Informatics
Universitas Nusa Mandiri
Email: adhitya.januarizky93@gmail.com

License

This project is intended for academic and research purposes. It is recommended to use the MIT License before public release.

Keywords

Digital Image Processing, Image Enhancement, Intensity Transformation, Histogram Equalization, Histogram Matching, CLAHE, Gamma Correction, Python, OpenCV, Tkinter
