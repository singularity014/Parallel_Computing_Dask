import psutil
import os

# Querying Python interpreter's memory usage
# Function to be called before and after every operation
def memory_footprint():
    """
    :return: memory in MB being used by python process
    """
    mem = psutil.Process(os.getpid()).memory_info().rss
    return (mem/ 1024**2)

