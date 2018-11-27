import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
res=100
# A is input array; currently square
A=np.zeros((res,res))
for i in range(40,60):
    for j in range(40,60):
        A[i][j] = .01

# Set up axes x and y
x=[] #[1,2,...,99,1,2,...,99...]
y=[] #[1,1,...,1,2,2,...2,...99,99]
for i in range(res):
    for j in range(res):
        x+=[int(j-res/2)]
        y+=[int(i-res/2)]

# Do fft on A with numpy
A_fft=np.abs(np.fft.fftshift(np.fft.fft2(A)))**2
# Convert A_fft to one looong list for plotting
fft_results=[]
for i in range(res):
    fft_results+=list(A_fft[i])
# Convert A to one loong list for plotting
B=[]
for i in range(res):
    B+=list(A[i])

# Plot
fig=plt.figure()
ax = fig.gca(projection='3d')
#ax.scatter(x,y,B,color='blue')
ax.plot(x,y,fft_results,color='red')
plt.show()
