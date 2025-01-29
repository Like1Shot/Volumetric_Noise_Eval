import os
import cv2
import numpy as np

def load_data(capture_dir):
    depth_images = []
    color_images = []
    
    depth_dir = os.path.join(capture_dir, 'depth')
    color_dir = os.path.join(capture_dir, 'color')
    
    for filename in sorted(os.listdir(depth_dir)):
        if filename.endswith('.png'):
            depth_image = cv2.imread(os.path.join(depth_dir, filename), cv2.IMREAD_UNCHANGED)
            depth_images.append(depth_image)
    
    for filename in sorted(os.listdir(color_dir)):
        if filename.endswith('.png'):
            color_image = cv2.imread(os.path.join(color_dir, filename))
            color_images.append(color_image)
    
    return depth_images, color_images 