import numpy as np
import pandas as pd
import datetime

# 导入气象资料
df_ferrara = pd.read_csv('WeatherData/ferrara_270615.csv')
df_milano = pd.read_csv('WeatherData/milano_270615.csv')
df_mantova = pd.read_csv('WeatherData/mantova_270615.csv')
df_ravenna = pd.read_csv('WeatherData/ravenna_270615.csv')
df_torino = pd.read_csv('WeatherData/torino_270615.csv')
df_asti = pd.read_csv('WeatherData/asti_270615.csv')
df_bologna = pd.read_csv('WeatherData/bologna_270615.csv')
df_piacenza = pd.read_csv('WeatherData/piacenza_270615.csv')
df_cesena = pd.read_csv('WeatherData/cesena_270615.csv')
df_faenza = pd.read_csv('WeatherData/faenza_270615.csv')

# 导入必要的包

# %matplotlib inline # 在输出中进行绘画，运行代码可注释，在IPython编译器里直接使用，作用是内嵌画图，省略掉plt.show()这一步，直接显示图像，使用plt.show()代替。
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser


# 取出我们要分析的温度和日期数据
y1 = df_milano['temp']
x1 = df_milano['day']

# 把日期数据转换成 datetime 的格式
day_milano = [parser.parse(x) for x in x1]

# 调用 subplot 函数, fig 是图像对象，ax 是坐标轴对象
fig, ax = plt.subplots()

# 调整x轴坐标刻度，使其旋转70度，方便查看
plt.xticks(rotation=70)

# 设定时间的格式
hours = mdates.DateFormatter('%H:%M')

# 设定X轴显示的格式
ax.xaxis.set_major_formatter(hours)

# 画出图像，day_milano是X轴数据，y1是Y轴数据，‘r’代表的是'red' 红色
ax.plot(day_milano ,y1, 'r')

plt.show()

# 把图片存储为png图
# plt.savefig('figpath.png', dpi=400, bbox_inches='tight')




