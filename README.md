# Depth Camera Noise Reduction

This repository contains implementations and evaluations of different methods for reducing depth noise in camera systems, specifically focused on the Intel RealSense D435i camera.

## Setup

### Prerequisites
- Python 3.8+
- [uv](https://github.com/astral/uv) - Fast Python package installer and resolver
- [Intel RealSense SDK 2.0](https://github.com/IntelRealSense/librealsense/releases/tag/v2.56.3)

### Installation

1. Install the Intel RealSense SDK:
```bash
#brew install librealsense  # For MacOS dont use! 
# Just go with Ubuntu

# For Ubuntu 
sudo apt update
sudo apt upgrade
sudo apt install -y libusb-1.0-0-dev libgtk-3-dev cmake build-essential pkg-config libssl-dev

sudo apt install cmake

git clone https://github.com/IntelRealSense/librealsense.git

cd librealsense

mkdir build
cd build

cmake ..
make
sudo make install

# Verify the Installation
realsense-viewer

```

2. Clone and setup the project:
```bash
chmod +x setup.sh
./setup.sh
```

3. Activate the virtual environment:
```bash
source .venv/bin/activate
```

## Project Structure
```
depth-noise-reduction/
├── configs/
│   └── camera_configs/     # Camera-specific configurations
│       └── d435i_config.yaml
├── data/
│   ├── raw/               # Raw depth camera captures
│   └── processed/         # Processed and filtered data
├── src/
│   ├── preprocessing/     # Data preprocessing scripts
│   ├── models/           # Noise reduction implementations
│   ├── evaluation/       # Evaluation metrics and tools
│   ├── utils/           # Utility functions
│   └── realsense/       # RealSense camera interface
├── notebooks/           # Jupyter notebooks for analysis
└── results/
    ├── figures/         # Generated plots and visualizations
    └── metrics/         # Evaluation results
```

## Usage

### Data Capture
To capture data from the RealSense camera:

```bash
python src/realsense/capture.py
```

This will:
- Read configuration from `configs/camera_configs/d435i_config.yaml`
- Capture both depth and color frames
- Save the data to `data/raw/capture_YYYYMMDD_HHMMSS/`

### Configuration
Camera settings can be modified in `configs/camera_configs/d435i_config.yaml`:
- Stream resolution and FPS
- Post-processing filters
- IMU settings

## Development

The project uses:
- `uv` for dependency management and virtual environments
- Intel RealSense SDK 2.0 for camera interface
- OpenCV and NumPy for image processing
- Open3D for 3D visualization

## Contributing
1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## License
[MIT License](LICENSE)
