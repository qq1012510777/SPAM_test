import tifffile
import spam.DIC
import matplotlib.pyplot as plt

SliceToShow = 0
grey = spam.DIC.binning(tifffile.imread("Test3D.tif"), 3) # downscale the image while reading it
# tifffile.imsave("M2EA05-01-bin4.tif", grey) # save it for later
print(grey.shape)
plt.imshow(grey[SliceToShow, :, :], cmap="Greys_r"); plt.show()

import spam.plotting
spam.plotting.plotGreyLevelHistogram(grey, showGraph=True)

# following from above
binary = grey == 0 # i.e., binary is where "grey" is bigger than or equal to 18000

print(binary.sum()) # let's count the number of "True" voxels:
# output:
# 4985517

plt.imshow(binary[SliceToShow, :, :], cmap="Greys_r"); plt.show()

import spam.label
labelled = spam.label.watershed(binary) # about 3 minutes on Eddy's laptop
tifffile.imwrite("test3D_watershed.tiff", labelled[:,:,:]) # save it for later

print(labelled.max())
print(labelled.shape)
# output:
# 3105
# *i.e.,* there are 3105 different particles

# use spam.label.randomCmap to show different labels
plt.imshow(labelled[SliceToShow, :, :], cmap=spam.label.randomCmap); plt.show()