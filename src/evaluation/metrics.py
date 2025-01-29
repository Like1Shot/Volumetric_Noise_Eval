import numpy as np
from skimage.metrics import structural_similarity as ssim

def calculate_rmse(original, denoised):
    return np.sqrt(np.mean((original - denoised) ** 2))

def calculate_mae(original, denoised):
    return np.mean(np.abs(original - denoised))

def calculate_ssim(original, denoised):
    return ssim(original, denoised, data_range=denoised.max() - denoised.min()) 