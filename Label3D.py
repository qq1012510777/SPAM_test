import tifffile
import spam.DIC
import matplotlib.pyplot as plt
import sys

numArgumeng=len(sys.argv)-1

if numArgumeng < 3:
    print("Please input three parameters:")
    print(" argv[1]: the filename (tif or tiff)")
    print(" argv[2]: binning (int) - The number of pixels/voxels to average together")
    print(" argv[3]: output file name (tiff or tif)")
    exit(0)

filename = str(sys.argv[1])
binningNum = int(sys.argv[2])
outputfilename = str(sys.argv[3])

grey = spam.DIC.binning(tifffile.imread(filename), binningNum)

print('data size: ', grey.shape)

#import spam.plotting
#spam.plotting.plotGreyLevelHistogram(grey, showGraph=True)

# following from above
binary = grey == 1 # 1 is the rock/soil

print("the number of \"True\" voxels", binary.sum()) # let's count the number of "True" voxels:

print("identifying particles ......")
import spam.label
labelled = spam.label.watershed(binary) # 

print("writting labelled data ......")
tifffile.imwrite(outputfilename, labelled[:,:,:]) # 

print("how many particles: ", labelled.max())