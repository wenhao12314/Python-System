#Wenhao Dou ET 6152590
import numpy as np
import scipy.signal as sg
import matplotlib.pyplot as plt
import math

#5.1 a)
#H(z)/z = 1/(z-0.25)-1/(z+0.75)
#H(z) = z/(z-0.25)-z/(z+0.75)

#5.1 b)
s1=sg.lti([0,1,0],[1,0.5,-0.1875])
st,sy=sg.step2(s1)
it,iy=sg.impulse2(s1)
sy1,=plt.plot(st,sy,label="step")
iy1,=plt.plot(it,iy,label="impluse")

plt.legend(handles=[sy1,iy1],loc="upper right")
plt.grid(True)
plt.show()

#5.1 c)
z,p,k = sg.tf2zpk([0,1,0],[1,0.5,-0.1875])
print("NullStellen: " + str(z))
print("Polstellen: " + str(p))
print("Verstärkungsfaktor: " + str(k)+"\n")

#5.1 d)
a,b,c,d = sg.tf2ss([0,1,0],[1,0.5,-0.1875])
print("Zustandsraumdarstellung: " + str(a)+str(b)+str(c)+str(d)+"\n")

#5.2 a)
s2=sg.lti([1,0,1],[1,-1,0.5])
w,h=sg.freqs([1,0,1],[1,-1,0.5])
plt.figure("5.2 a")
plt.semilogx(w,20*np.log10(abs(h)))
plt.xlabel("Frequency")
plt.ylabel("Amplitude response")
plt.grid(True)
plt.show()

#5.2 b)
#z=sg.lfilter([1,0,1],[1,-1,0.5],sg.lfilter([1,0,1],[1,-1,0.5],s2))
#plt.figure("5.2 b")
#plt.semilogx(20*np.log10(abs(z)))
#plt.grid(True)
#plt.show()

#5.3 a)
pi=math.pi
fir_filter=sg.firwin(6, 0.2*pi)
w,h=sg.freqz(fir_filter)
plt.figure("5.3 a Tiefpass")
plt.semilogx(w,20*np.log10(abs(h)))
plt.xlabel("Frequency")
plt.ylabel("Amplitude response")
plt.grid(True)
plt.show()

#5.3 b)
#Es ist ein Tiefpassfilter

#5.3 c) Hoch_pass
b,a=sg.butter(5,0.2*pi,"highpass",analog=True)
w,h=sg.freqz(b,a)
plt.figure("5.3 c Hochpass")
plt.semilogx(w,20*np.log10(abs(h)))
plt.xlabel("Frequency")
plt.ylabel("Amplitude response")
plt.grid(True)
plt.show()

#5.3 d) Band_pass
b,a=sg.butter(5,[0.1*pi,0.2*pi],"bandpass")
w,h=sg.freqz(b,a)
plt.figure("5.3 d Bandpass")
plt.semilogx(w,20*np.log10(abs(h)))
plt.xlabel("Frequency")
plt.ylabel("Amplitude response")
plt.grid(True)
plt.show()