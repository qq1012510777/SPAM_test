import tifffile
import spam.DIC
import matplotlib.pyplot as plt

grey = spam.DIC.binning(tifffile.imread("142-1.tif"), 2) # downscale the image while reading it
# tifffile.imsave("M2EA05-01-bin4.tif", grey) # save it for later
print(grey.shape)
plt.imshow(grey[:, :], cmap="Greys_r"); plt.show()

import spam.plotting
spam.plotting.plotGreyLevelHistogram(grey, showGraph=True)

# following from above
binary = grey == 1 # i.e., binary is where "grey" is bigger than or equal to 18000

print(binary.sum()) # let's count the number of "True" voxels:
# output:
# 4985517

plt.imshow(binary[:, :], cmap="Greys_r"); plt.show()

import spam.label
labelled = spam.label.watershed(binary) # about 3 minutes on Eddy's laptop
# tifffile.imsave(""M2EA05-01-bin4-watershed.tif", labelled) # save it for later

print(labelled.max())
# output:
# 3105
# *i.e.,* there are 3105 different particles

# use spam.label.randomCmap to show different labels
plt.imshow(labelled[:, :], cmap=spam.label.randomCmap); plt.show()