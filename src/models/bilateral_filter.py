import cv2
import numpy as np

def apply_bilateral_filter(depth_image, d=5, sigma_color=75, sigma_space=75):
    return cv2.bilateralFilter(depth_image, d, sigma_color, sigma_space) 