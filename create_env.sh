#!/bin/bash

# Usage: bash create_env_new.sh <env_name>

# Ensure an environment name is provided
if [ -z "$1" ]; then
    echo "Error: No environment name provided."
    echo "Usage: bash create_env_new.sh <env_name>"
    exit 1
fi

ENV_NAME=$1
ENV_BASE_DIR=~/.venvs
ENV_DIR=$ENV_BASE_DIR/$ENV_NAME

# Create the base directory if it doesn't exist
mkdir -p $ENV_BASE_DIR

# Check if the environment already exists
if [ -d "$ENV_DIR" ]; then
    echo "Warning: Virtual environment '$ENV_NAME' already exists in $ENV_DIR."
    read -p "Do you want to overwrite it? (y/N): " confirm
    if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
        echo "Aborting."
        exit 0
    fi
    rm -rf "$ENV_DIR"  # Remove existing environment if confirmed
fi

# Purge all loaded modules
echo "Purging all loaded modules..."
module --force purge

# Load necessary modules
echo "Loading required modules..."
module load StdEnv gcc opencv
module load python/3.10.13

# Create virtual environment
echo "Creating virtual environment: $ENV_NAME in $ENV_DIR"
virtualenv "$ENV_DIR"
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment."
    exit 1
fi

# Activate the virtual environment
source "$ENV_DIR/bin/activate"

# Upgrade pip and install dependencies
echo "Upgrading pip and installing dependencies..."
pip install --no-index --upgrade pip
pip install --ignore-installed numpy Pillow
pip install scikit-learn ipywidgets \
            torch torchvision torchmetrics torch-summary \
            diffusers transformers huggingface-hub==0.25.2 \
            safetensors einops peft protobuf==3.20

# Check whether all the packages are installed
echo "Checking installed packages..."
packages=("numpy" "Pillow" "scikit-learn" "ipywidgets" \
          "torch" "torchvision" "torchmetrics" "torch-summary" \
          "diffusers" "transformers" "huggingface_hub" "safetensors" \
          "einops" "peft" "protobuf")
for package in "${packages[@]}"; do
    if ! python -m pip show -q "$package"; then
        echo "Error: Package '$package' not properly installed"
    fi
done

echo "Environment setup complete! Activate using: source $ENV_DIR/bin/activate"
