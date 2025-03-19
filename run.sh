#!/bin/bash

echo "Starting CloudShop CLI..."

# Ensure Python is installed
if ! command -v python &> /dev/null
then
    echo "Error: Python is not installed. Please install Python and try again."
    read -p "Press any key to exit..."
    exit 1
fi

# Set PYTHONPATH to include the src directory
export PYTHONPATH=$(pwd)/src:$PYTHONPATH

# Run the Python program
python src/main.py

# Keep the terminal open
read -p "Press any key to exit..."