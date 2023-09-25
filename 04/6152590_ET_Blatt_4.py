#Wenhao Dou ET 6152590
import numpy as np
import matplotlib.pyplot as plt
#4.1.a
x_k1 = np.zeros(101)
x_k1[50] = 1
print(x_k1)

x_f1=np.fft.fft(x_k1)
print(np.abs(x_f1)**2)

plt.figure(1)
plt.plot(x_k1)
plt.grid()

plt.figure(2)
plt.plot(abs(x_f1)**2)
plt.ylim([0,2])
plt.grid()
#4.1.b
x_k2 = np.zeros(101)
x_k2[30:71] = 1
print(x_k2)

x_k2_q=np.fft.fftfreq(101)
x_f2=np.fft.fft(x_k2)
print(np.abs(x_f2))

plt.figure(3)
plt.plot(x_k2)
plt.grid()

plt.figure(4)
plt.plot(x_k2_q,abs(x_f2))
plt.grid()
#4.2
k1 = list()
for i in range(20):
    k1.append(0.9**i)
print(k1)
x1 = np.array(k1)
print(x1)

x2 = np.ones(5)
print(x2)

f1 = np.convolve(x1,x2)
f2 = np.convolve(x2,x1)
f3 = np.convolve(x2,x2)

plt.figure(5)
plt.plot(f1)
plt.grid()

plt.figure(6)
plt.plot(f2)
plt.grid()

plt.figure(7)
plt.plot(f3)
plt.grid()
#4.3.a
plt.show()