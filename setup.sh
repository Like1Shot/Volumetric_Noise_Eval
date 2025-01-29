#!/bin/bash

# Create project directory and navigate into it
mkdir depth-noise-reduction
cd depth-noise-reduction

# Check if uv is installed, if not install it
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Create and activate virtual environment using uv
uv venv
source .venv/bin/activate

# Create directory structure
mkdir -p data/{raw,processed}
mkdir -p src/{preprocessing,models,evaluation,utils,realsense}
mkdir -p results/{figures,metrics}
mkdir notebooks
mkdir configs
mkdir -p configs/camera_configs

# Install requirements using uv (much faster than pip)
uv pip install --upgrade pip
uv pip install -r requirements.txt

# Initialize git repository
git init
echo "data/" >> .gitignore
echo "results/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".DS_Store" >> .gitignore
echo ".venv/" >> .gitignore 