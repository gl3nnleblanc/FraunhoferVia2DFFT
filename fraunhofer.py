# Preliminary - copied from stackoverflow (Plot the 2D FFT of an image)
from scipy import fftpack, ndimage
import matplotlib.pyplot as plt
image = plt.imread('image.png')
fft2 = fftpack.fft2(image)
plt.imshow(abs(fft2))
plt.show()
