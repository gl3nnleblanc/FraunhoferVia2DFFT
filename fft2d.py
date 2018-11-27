import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cv2
from mpl_toolkits.mplot3d import Axes3D
# Import square image with appropriate filepath for aperture. white-> opening; black-> blockage
img_path='./aperture6.png'
img=cv2.imread(img_path,0).astype(float)*.001
res=len(img)

# Do fft on image with numpy
img_fft=np.abs(np.fft.fftshift(np.fft.fft2(img))).transpose()
plt.imshow(img_fft, cmap=cm.plasma)
plt.show()
