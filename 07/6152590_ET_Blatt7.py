#Wenhao Dou ET 6152590
import sympy
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg

#7.1
a=sympy.symbols("a")
t=sympy.symbols("t")
s=sympy.symbols("s")
y=sympy.exp(-a*t)
H=sympy.integrals.laplace_transform(y, t, s)
print("Laplace-Transformation: "+str(H[0]))

#7.2 a)
trans=sg.TransferFunction([1],[1,2,2,1])

print("zeros :"+str(trans.zeros))
print("poles :"+str(trans.poles))
plt.figure()
plt.plot(np.real(trans.zeros), np.imag(trans.zeros),"go")
plt.plot(np.real(trans.poles), np.imag(trans.poles),"rx")
plt.plot([-2, 2], [0, 0], "g-", linewidth=1)
plt.plot([0, 0], [-2, 2], "g-", linewidth=1)
plt.legend()
plt.show()

#7.2 b) i)
st,sy=sg.step2(trans)
it,iy=sg.impulse2(trans)
sy1,=plt.plot(st,sy,label="step")
iy1,=plt.plot(it,iy,label="impluse")

plt.legend(handles=[sy1,iy1],loc="upper right")
plt.grid(True)
plt.show()

#7.2 b) ii)
r,p,k=sg.residue([1],[1,2,2,1])
print("Residuen: "+str(r))

#7.2 c)
w, mag, phase = sg.bode(trans)

plt.figure("Amplitude")
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure("Phase")
plt.semilogx(w, phase)  # Bode phase plot
plt.show()

#7.3 Butterworth
ord,wn=sg.buttord(1000*2*np.pi,1400*2*np.pi,0.5,30,analog=True) 
b,a=sg.butter(ord,wn,"low",analog=True)
w,mag,phase=sg.bode((b,a))
z,p,k=sg.tf2zpk(b,a)

plt.figure()
plt.semilogx(w/2/np.pi,mag)
plt.show()

plt.figure()
plt.plot(np.real(z),np.imag(z),"go")
plt.plot(np.real(p),np.imag(p),"rx")
plt.legend()
plt.show()

#7.3 Tschebyscheff Typ I
ord,wn=sg.cheb1ord(1000*2*np.pi,1400*2*np.pi,0.5,30,analog=True) 
b,a=sg.cheby1(ord,0.5,wn,"low",analog=True)
w,mag,phase=sg.bode((b,a))
z,p,k=sg.tf2zpk(b,a)

plt.figure()
plt.semilogx(w/2/np.pi,mag)
plt.show()

plt.figure()
plt.plot(np.real(z),np.imag(z),"go")
plt.plot(np.real(p),np.imag(p),"rx")
plt.legend()
plt.show()

#7.3 Tschebyscheff Typ II
ord,wn=sg.cheb2ord(1000*2*np.pi,1400*2*np.pi,0.5,30,analog=True) 
b,a=sg.cheby2(ord,0.5,wn,"low",analog=True)
w,mag,phase=sg.bode((b,a))
z,p,k=sg.tf2zpk(b,a)

plt.figure()
plt.semilogx(w/2/np.pi,mag)
plt.show()

plt.figure()
plt.plot(np.real(z),np.imag(z),"go")
plt.plot(np.real(p),np.imag(p),"rx")
plt.legend()
plt.show()

#7.3 Cauer
ord,wn=sg.ellipord(1000*2*np.pi,1400*2*np.pi,0.5,30,analog=True) 
b,a=sg.ellip(ord,0.5,30,wn,"low",analog=True)
w,mag,phase=sg.bode((b,a))
z,p,k=sg.tf2zpk(b,a)

plt.figure()
plt.semilogx(w/2/np.pi,mag)
plt.show()

plt.figure()
plt.plot(np.real(z),np.imag(z),"go")
plt.plot(np.real(p),np.imag(p),"rx")
plt.legend()
plt.show()

#7.4 a)
t=np.linspace(-5,5,80)
y=np.sin(2*np.pi*t)

plt.figure()
plt.stem(t, y)
plt.show()

#7.4 b)
#t2=np.linspace(-5,5,10000)
#y2=y1*0
#for i in range(len(t2)):
    #index = np.sum(t2[i] >= t1) -1
    #y2[i] = y1[index]

#plt.figure()
#plt.plot(t2, y2)
#plt.legend(loc='lower right')
#plt.show()

