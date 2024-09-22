#学习使用signal.lfilter函数，该函数用来 输出差分方程的解
#y(n)-0.6y(n-1)=x(n)+2x(n-1),初始条件为y(-1)=1,求输入为x（n）=(0.1*a)^n*u(n)时系统的零状态、零输入、全响应
#，并绘图，a=7
#解差分方程
# y[n]-0.6y[n-1]=x[n]+2x[n-1],初始条件：y[-1]=1,输入信号：x[n]=(0.1a)**n*u[n],a=7

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

nmin=0
nmax=8
n=np.arange(nmin,nmax+1,1)#n的取值从min到max,间隔为1

den=np.array([1,0.6])#y[n]的系数
num=np.array([1,2])#x[n]的系数

xn=(0.1*7)**n#输入信号x[n]
x01=np.array([0])
zi1=signal.lfilter_zi(num,den)#差分方程

#解差分方程
y3,_=signal.lfilter(num,den,xn,zi=zi1)#x[n]带入了差分方程

#计算单位冲激响应
#t4,y4=signal.dimpulse((num,den,1),n=nl)

plt.subplot(211)
plt.stem(n,xn)
plt.ylim(-1,2.5)
plt.title("x[n]")

plt.subplot(212)
plt.stem(n,y3)
plt.ylim(-1,2.5)
plt.title("y[n]")

plt.show()