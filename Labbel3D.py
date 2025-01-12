import tifffile
import spam.DIC
import matplotlib.pyplot as plt

grey = spam.DIC.binning(tifffile.imread("142.tif"), 2)

print('data size: ', grey.shape)

import spam.plotting
spam.plotting.plotGreyLevelHistogram(grey, showGraph=True)

# following from above
binary = grey == 1 # 1 is the rock/soil

print("the number of \"True\" voxels", binary.sum()) # let's count the number of "True" voxels:

print("identifying particles ......")
import spam.label
labelled = spam.label.watershed(binary) # 

print("writting labelled data ......")
tifffile.imwrite("Result.tiff", labelled[:,:,:]) # 

print("how many particles: ", labelled.max())