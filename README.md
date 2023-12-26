# Image Filtering and Adjustment Project

This project focuses on image processing techniques such as convolution, averaging, Gaussian filtering, median filtering, and contrast/brightness adjustment. The implementation details and usage instructions are provided below.

## Project Files

1. **image_filtering.py**: Python script containing implementations for convolution, averaging filter, Gaussian filter, median filter, and contrast/brightness adjustment.
2. **Noisy_image.png**: Original image with noise.
3. **convolved_image.png**: Output of convolution applied to the noisy image.
4. **average_image.png**: Output of averaging filter applied to the noisy image.
5. **gaussian_image.png**: Output of Gaussian filter applied to the noisy image.
6. **median_image.png**: Output of median filter applied to the noisy image.
7. **Uexposed.png**: Original image for contrast/brightness adjustment.
8. **adjusted_image.png**: Output of contrast and brightness adjustment applied to the Uexposed image.
9. **README.md**: Project documentation.


## Convolution
Convolution is a fundamental operation in image processing. It involves applying a filter (kernel) to an image to highlight or extract certain features. In this project, convolution is applied to the original noisy image (Noisy_image.png) using a 3x3 averaging kernel. The result is saved as convolved_image.png

## Averaging Filter
The averaging filter is a smoothing technique used to reduce noise in an image. It replaces each pixel value with the average of its neighboring pixels. In this project, the averaging filter is applied to the original noisy image, and the result is saved as average_image.png.

## Gaussian Filter
The Gaussian filter is a smoothing filter that gives more weight to the central pixel and decreases the weight as you move away from the center, following a Gaussian distribution. In this project, the Gaussian filter is applied to the original noisy image, and the result is saved as gaussian_image.png.

## Median Filter
The median filter is a nonlinear filtering technique effective in removing salt-and-pepper noise. It replaces each pixel value with the median of its neighboring pixels. In this project, a 5x5 median filter is applied to the original noisy image, and the result is saved as median_image.png.

## Contrast and Brightness Adjustment
Contrast and brightness adjustment is a technique used to enhance or reduce the contrast and brightness of an image. In this project, contrast and brightness adjustment are applied to the original image (Uexposed.png), and the result is saved as adjusted_image.png. This adjustment is achieved by scaling and shifting pixel values

