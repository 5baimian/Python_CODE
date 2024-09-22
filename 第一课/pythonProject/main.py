#使用numpy和matplotlib第三方软件包

import numpy as np #读取信号模块
import matplotlib.pyplot as plt  #画图模块
#生成离信号
t=np.linspace(0,1,1000)  #（起点，终点，点数）
f=10
#信号频率
y=np.sin(2*np.pi*f*t)
#进行傅里叶变换
y_fft=np.fft.fft(y)
#计算幅度谱
y_fft_abs=np.abs(y_fft)
#计算频率轴
freqs=np.fft.fftfreq(len(y),t[1]-t[0])
#绘制时域图
plt.subplot(121),plt.plot(t,y)
#绘制幅度谱图
plt.subplot(122),plt.plot(freqs,y_fft_abs)

plt.show()