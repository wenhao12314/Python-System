#Wenhao Dou ET 6152590
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft
from scipy.signal import tf2ss
import scipy.signal as sg

#6.1 a)
t=np.linspace(0,1,10)
x1=np.sin(2*t)/np.pi*t
fft_x=fft(x1)

plt.figure("6.1 a")
plt.plot(t,fft_x)
plt.show()

#6.1 b)
t=np.linspace(0,1,50)
m1=np.cos(2*t)
m2=np.cos(4*t)
fft_m1=fft(m1)
fft_m2=fft(m2)

plt.figure("6.1 b_1")
plt.plot(t,fft_m1)
plt.show()
plt.figure("6.1 b_2")
plt.plot(t,fft_m2)
plt.show()

#6.2
range_1=1
funk=lambda x,y:2*y+x

#6.2 a)
def expliziten_euler(range_1,h,funk,x0,y0):
    step=int(range_1/h)
    x=[x0]+[h*i for i in range(step)]
    u=[y0]+[0 for i in range(step)]
    for i in range(step):
        u[i+1]=u[i]+h*funk(x[i],u[i])
    plt.plot(x,u,label="expliziten_euler")
    return u    

expliziten_euler(range_1,0.25,funk,0,1)
plt.legend()
plt.show()

#6.2 b)
def impliziten_euler(range_1,h,funk,x0,y0):
    step=int(range_1/h)
    x=[x0]+[h*i for i in range(step)]
    u=[y0]+[0 for i in range(step)]
    for i in range(step):
        u[i+1]=u[i]+h*funk(x[i+1],u[i+1])
    plt.plot(x,u,label="impliziten_euler")
    return u 

impliziten_euler(range_1,0.25,funk,0,1)
plt.legend()
plt.show()

#6.2 c)
def trapez(range_1,h,funk,x0,y0):
    step=int(range_1/h)
    x=[x0]+[h*i for i in range(step)]
    u=[y0]+[0 for i in range(step)]
    for i in range(step):
        u[i+1]=u[i]+h/2*(funk(x[i+1],u[i+1])+funk(x[i],u[i]))
    plt.plot(x,u,label="trapez")
    return u 

trapez(range_1,0.25,funk,0,1)
plt.legend()
plt.show()

#6.3 a)
a,b,c,d=tf2ss([0,0,1,-1],[1,20.1,102.01,100.01])
print("Zustandsmodell: "+str(a)+str(b)+str(c)+str(d))

#6.3 b)
e=np.linalg.eig(a)
print("Eigenwerte: "+str(e[0]))

#6.3 c)
s1=sg.lti([0,0,1,-1],[1,20.1,102.01,100.01])
it,iy=sg.impulse2(s1)
plt.figure("6.3 c ")
plt.plot(it,iy,label="impluse")
plt.grid(True)
plt.show()

#6.3 d)
s1=sg.lti([0,0,1,-1],[1,20.1,102.01,100.01])
t=np.linspace(0,1,50)
u=np.sin(2*np.pi*t)
tout,y,x=sg.lsim(s1,u,t)
plt.figure("6.3 d ")
plt.plot(t,y)
plt.show()

#6.3 e)
#s1=sg.lti([0,0,1,-1],[1,20.1,102.01,100.01])
#t=np.linspace(10,1,50)
#plt.figure("6.3 e ")
#plt.plot(t,sg.impulse2(s1),label="impluse")
#plt.grid(True)
#plt.show()