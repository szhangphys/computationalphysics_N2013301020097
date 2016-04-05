#第六次作业

## 2.9 题

>代码在**这里**。

-------------------
空气阻力的计算式为
$$ F_{drag} = - \left(1 - \frac{ay}{T_{0}}\right)^\alpha B_{2} v^{2} $$

其中各参数为$\alpha = 2.5$，$a = 6.5 \times 10^{-3} K/m $，$T_{0} = 300K$，$ \frac{B_2}{m} = 4 \times 10^{-5} m^{-1}$。

程序的伪代码为：
```
def update(dt):
	x += v_x * dt
	y += v_y * dt
	v_x += F_drag_x / m * dt
	v_y += (F_drag_y / m  + gravity) * dt

dt = 0.1 #s
for i in range(1000):
	update(dt) 
```

对初始条件分别为『初速度$700m/s$，出射角$45^{\circ}$，有密度修正』和『初速度$700m/s$，出射角$35^{\circ}$，没有密度修正』的两种加农炮做计算，得到了和图 2.5 相似的图像：
![Cannon shell trajectory](https://lh3.googleusercontent.com/-l-03DK53UXk/VwPMhsinzYI/AAAAAAAAAIA/iEOWRGDE_6YF4V5w8pSrNGLp_7PqlhzAQ/s0/Cannon+shell+trajectory.png "Cannon shell trajectory.png")

现在以『有密度修正』作为实际情况，初速度定为$700m/s$，不断改变角度，实验得到射程最大的角度为$43.55^{\circ}$，此时射程为$24519.8m$。


## 2.10题

>代码在**这里**。

------------------
设目标水平距离为 20km。
程序原理是以各种角度和初速度向目标发射炮弹，水平距离到达 20km 时终止，记录此时炮弹的海拔高度。多次试验后将初速度与海拔高度的绘图如下：
![minimum speed](https://lh3.googleusercontent.com/-2xJE7JJeQRc/VwPMOwditnI/AAAAAAAAAH4/DYmxD_0b48saJW0Yxq-ThBkbLjtGrBgxA/s0/minimum+speed.png "minimum speed.png")

可以看出，右下分界线就是最小出射速度与目标海拔高度的变化曲线。


