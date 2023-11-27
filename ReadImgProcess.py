from matplotlib import pyplot as plt
from matplotlib import image as mpimg

img = mpimg.imread("SavedByProcess\pieFig.png")
# it give us grids in order to remove that we do it.
plt.axis("off")
plt.imshow(img[:,:,1],cmap="hot")