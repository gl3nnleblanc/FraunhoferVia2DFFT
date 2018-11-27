# Preliminary - copied from stackoverflow (Plot the 2D FFT of an image)
from scipy import fftpack, ndimage
import matplotlib.pyplot as plt
image = plt.imread('rect2.png')
fft2 = fftpack.fft2(image)
plt.imshow(fft2.imag)
plt.show()
