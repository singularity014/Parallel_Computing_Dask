from memory_check import memory_footprint
import numpy as np
import pandas as pd


# To be called before we do any operation
before = memory_footprint()


# Let us create a numpy array which takes 50 MB from memory
N = (1024**2)//8 # number of floats that  takes 1 MB memory
x = np.random.randn(N*50) #numpy array which takes 1*50 = 50 MB of memory
after = memory_footprint()

print(f"Memory usage before numpy array creation : {before} MB")
print(f"Memory usage after numpy array creation : {after} MB")

print()
before = memory_footprint()
# Square the numpy array without assigning it back to x
x**2
after = memory_footprint()
print(f"Memory usage before squaring : {before} MB")
print(f"Memory usage after squaring : {after} MB")


# ------- further checks ------------
# nbytes in numpy tells the memory usage, then we convert it to MB
print(x.nbytes // (1024 **2))
print()

# memory usage of a dataframe of x
df = pd.DataFrame(x)
print(f'{df.memory_usage(index=False)// (1024**2)} MB taken by dataframe')

