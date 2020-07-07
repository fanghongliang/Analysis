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

# -------------------------------------------------------------------------------
# 米兰温度时间分析表
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

# ---------------------------------------------------------------
# 绘制折线图- 隐式创建figure画布对象
# x = [1, 3, 5, 7]
# y = [4, 9, 1, 9]
#
# plt.plot(x, y)
# plt.show()


# ----------------------------------------------------------------
# 显示创建画布，可控制axes
figure = plt.figure()
axes1 = figure.add_subplot(2, 1, 1)
axes2 = figure.add_subplot(2, 1, 2)

axes1.plot([1, 3, 5, 7], [2, 4, 6, 8], ':b')
axes2.plot([1, 2, 4, 6], [9, 3, 5, 6])

# figure.show()
plt.title('title')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
plt.show()     # pycharm 中绘图调用

# -----------------------------------------------------------------
# 频率分布图
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]
a = np.array(data)
hist, bins = np.histogram(a, bins = [0, 20, 40, 60, 80, 100])
print(hist)
print(bins)

plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")
plt.show()

# ---------------------------------------------------------------------
# desc 不同城市海洋距离影响气温的图表
# 读取温度和日期数据
y1 = df_ravenna['temp']
x1 = df_ravenna['day']
y2 = df_faenza['temp']
x2 = df_faenza['day']
y3 = df_cesena['temp']
x3 = df_cesena['day']
y4 = df_milano['temp']
x4 = df_milano['day']
y5 = df_asti['temp']
x5 = df_asti['day']
y6 = df_torino['temp']
x6 = df_torino['day']

# 把日期从 string 类型转化为标准的 datetime 类型
day_ravenna = [parser.parse(x) for x in x1]
day_faenza = [parser.parse(x) for x in x2]
day_cesena = [parser.parse(x) for x in x3]
day_milano = [parser.parse(x) for x in x4]
day_asti = [parser.parse(x) for x in x5]
day_torino = [parser.parse(x) for x in x6]

# 调用 subplots() 函数，重新定义 fig, ax 变量
fig, ax = plt.subplots()
plt.title('temp-sea')
plt.xticks(rotation=70)

hours = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(hours)

# 这里需要画出三根线，所以需要三组参数， 'g'代表'green'
ax.plot(day_ravenna, y1, 'r', day_faenza, y2, 'r', day_cesena, y3, 'r')
ax.plot(day_milano, y4, 'g', day_asti, y5, 'g', day_torino, y6, 'g')

plt.show()


# ----------------------------------------------------------------------

