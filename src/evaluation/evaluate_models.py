import os
from load_data import load_data
from bilateral_filter import apply_bilateral_filter
from metrics import calculate_rmse, calculate_mae, calculate_ssim

def evaluate_models(capture_dir):
    depth_images, _ = load_data(capture_dir)
    
    results = []
    
    for depth_image in depth_images:
        # Apply the bilateral filter
        denoised_image = apply_bilateral_filter(depth_image)
        
        # Calculate metrics
        rmse = calculate_rmse(depth_image, denoised_image)
        mae = calculate_mae(depth_image, denoised_image)
        ssim_value = calculate_ssim(depth_image, denoised_image)
        
        results.append({
            'rmse': rmse,
            'mae': mae,
            'ssim': ssim_value
        })
    
    return results

if __name__ == "__main__":
    capture_dir = "data/raw/capture_YYYYMMDD_HHMMSS"  # Update with your capture directory
    results = evaluate_models(capture_dir)
    print(results) 