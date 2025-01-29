import pyrealsense2 as rs
import numpy as np
import cv2
import yaml
import os
from datetime import datetime

class RealSenseCapture:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.pipeline = rs.pipeline()
        self.config_rs = rs.config()
        
    def setup_device(self):
        # Configure streams
        cfg = self.config['stream_config']
        self.config_rs.enable_stream(
            rs.stream.depth,
            cfg['depth']['width'],
            cfg['depth']['height'],
            rs.format.z16,
            cfg['depth']['fps']
        )
        
        self.config_rs.enable_stream(
            rs.stream.color,
            cfg['color']['width'],
            cfg['color']['height'],
            rs.format.rgb8,
            cfg['color']['fps']
        )
        
        if self.config['imu']['enabled']:
            self.config_rs.enable_stream(rs.stream.accel, rs.format.motion_xyz32f)
            self.config_rs.enable_stream(rs.stream.gyro, rs.format.motion_xyz32f)
            
    def start_capture(self, duration_seconds=10):
        self.pipeline.start(self.config_rs)
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_dir = f"data/raw/capture_{timestamp}"
            os.makedirs(save_dir, exist_ok=True)
            
            frame_count = 0
            while frame_count < duration_seconds * self.config['stream_config']['depth']['fps']:
                frames = self.pipeline.wait_for_frames()
                
                # Get depth frame
                depth_frame = frames.get_depth_frame()
                depth_image = np.asanyarray(depth_frame.get_data())
                
                # Get color frame
                color_frame = frames.get_color_frame()
                color_image = np.asanyarray(color_frame.get_data())
                
                # Save frames
                cv2.imwrite(f"{save_dir}/depth_{frame_count:06d}.png", depth_image)
                cv2.imwrite(f"{save_dir}/color_{frame_count:06d}.png", color_image)
                
                frame_count += 1
                
        finally:
            self.pipeline.stop()

if __name__ == "__main__":
    capture = RealSenseCapture("configs/camera_configs/d435i_config.yaml")
    capture.setup_device()
    capture.start_capture() 