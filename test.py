import math
# 光速
c = 3e8
# 谐振频率
f = 3.5e9
# 相对介电常数
er = 2.2
# 介质层厚度
h = 6e-3

# 矩形贴片实际宽度
w = c/(2*f)*(math.sqrt(2/(er+1)))
print("w:", w)
# 中间参数Ee
ee = (er+1)/2+(er-1)/2*(1+12*h/w)**(-0.5 )
print("ee:", ee)
# 辐射缝隙长度
deltaL = 0.412*h*(er+0.3)*(w/h+0.264)/(er-0.258)/(w/h+0.8)
print("deltaL:", deltaL)
# 矩形贴片实际长度
L = c/(2*f*math.sqrt(ee))-2*deltaL
print("L:", L)
# 计算xf中间参数
EreL = (er+1)/2+(er-1)/2*(1+12*h/L)**(-0.5)
print("EreL:", EreL)
# xf位置
xf = L/(2*math.sqrt(EreL))
print("xf:", xf)
# 参考地长度和宽度
LGNDmin = L+6*h
WGNDmin = w+6*h
print("LGNDmin:", LGNDmin)
print("WGNDmin:", WGNDmin)

