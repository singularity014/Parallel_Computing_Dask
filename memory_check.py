import psutil
import os

# Querying Python interpreter's memory usage
# Function to be called before and after every operation
# Tells how much memory a python operation is using
# This operation could be as simple as sum/mul to as complex as Embedding Calculation etc.

def memory_footprint():
    """
    :return: memory in MB being used by python process
    """
    mem = psutil.Process(os.getpid()).memory_info().rss
    return (mem/ 1024**2)

