Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

fig1 = plt.figure()

ax1 = fig1.add_subplot(1,1,1)

def animate(p):
    plot_data = open('testdata.csv','r').read()

    line_data = plot_data.split('\n')
    x1=[]
    y1=[]

    for line in line_data:
        if len(line)>1:
            x,y = line.split(',')
            x1.append(x)
            y1.append(y)


        ax1.clear()
        ax1.plot(x1,y1)

anime_data = animation.FuncAnimation(fig1, animate, interval = 500)

plt.show()