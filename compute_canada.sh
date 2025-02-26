#!/bin/bash
#SBATCH --nodes 1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-task=1
#SBATCH --cpus-per-task=12
#SBATCH --mem=64G
#SBATCH --time=2:00:00
#SBATCH --output=/home/j46lei/projects/rrg-dclausi/j46lei/IC-Light/output/log/%u_%x_%j.log
#SBATCH --account=rrg-dclausi
#SBATCH --mail-user=junf137@outlook.com
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=REQUEUE

# check parameters
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <env_path>"
    exit 1
fi

env_path=$1
# remove if the last char in env_path is "/"
if [ "${env_path: -1}" == "/" ]; then
    env_path=${env_path::-1}
fi


# Purge all loaded modules
echo "Purging all loaded modules..."
module --force purge

# Load necessary modules
echo "Loading required modules..."
module load StdEnv gcc opencv
module load python/3.10.13

# Activate the virtual environment
source $env_path/bin/activate

echo "Running the python script..."
python gradio_demo.py
