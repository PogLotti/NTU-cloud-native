echo "Starting setup..."

# Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Error: Python is not installed. Please install Python and try again."
    exit 1
fi

export PYTHONPATH=$(pwd)/src:$PYTHONPATH
echo "PYTHONPATH set to: $PYTHONPATH"

echo "CloudShop setup completed."

# Keep the terminal open
read -p "Press any key to exit..."