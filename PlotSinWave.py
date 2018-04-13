import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as Tk
class sin:
    def __init__(self):
        self.line=None
        self.root=None
     # update the data
    def animate(self,i):
        self.line.set_ydata(np.sin(self.x+i/10.0)) 
    def draws(self,root):
        self.root = Tk.Tk()
        self.fig=plt.Figure(figsize=(3,3))
        self.x=np.arange(0, 2*np.pi, 0.01)
        canvas = FigureCanvasTkAgg(self.fig, master=root)
        canvas.get_tk_widget().grid(row=7,column=0)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title ("Welcome To My Signal Package", fontsize=10)
        self.ax.set_ylabel("Y", fontsize=8)
        self.ax.set_xlabel("X", fontsize=8)
        self.line, = self.ax.plot(self.x,np.sin(self.x))
        ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, 200), interval=20, blit=False)
        self.root.mainloop()
    
        
        