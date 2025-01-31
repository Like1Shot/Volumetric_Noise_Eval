import os
import logging
from preprocessing.load_data import load_data
from models.bilateral_filter import apply_bilateral_filter
from metrics import calculate_rmse, calculate_mae, calculate_ssim

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def evaluate_models(capture_dir):
    logging.info(f"Loading data from directory: {capture_dir}")
    depth_images, _ = load_data(capture_dir)
    logging.info(f"Loaded {len(depth_images)} depth images.")

    results = []
    
    for index, depth_image in enumerate(depth_images):
        logging.info(f"Processing image {index + 1}/{len(depth_images)}")
        
        # Apply the bilateral filter
        denoised_image = apply_bilateral_filter(depth_image)
        logging.info(f"Applied bilateral filter to image {index + 1}")

        # Calculate metrics
        rmse = calculate_rmse(depth_image, denoised_image)
        mae = calculate_mae(depth_image, denoised_image)
        ssim_value = calculate_ssim(depth_image, denoised_image)
        
        results.append({
            'rmse': rmse,
            'mae': mae,
            'ssim': ssim_value
        })
        logging.info(f"Metrics for image {index + 1}: RMSE={rmse}, MAE={mae}, SSIM={ssim_value}")

    return results

if __name__ == "__main__":
    capture_dir = "data/raw/capture_YYYYMMDD_HHMMSS"  # Update with your capture directory
    logging.info(f"Starting evaluation for capture directory: {capture_dir}")
    results = evaluate_models(capture_dir)
    logging.info(f"Evaluation results: {results}")
    print(results) 