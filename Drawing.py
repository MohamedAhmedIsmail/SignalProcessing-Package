import tkinter as tk
from tkinter import ttk
class GUI:
    RadioOption1=None
    RadioOption2=None
    WriteToMyFile=None
    ReadMyFirstSignal=None
    PlotMyResultedSignal=None
    PlotmyGeneratedSignal=None
    def __init__(self):
        self.root=tk.Tk()
        self.phase=0
        self.flag=0
        self.root.geometry("1100x650")
        self.root.title("Signal Package")
        self.var1=tk.IntVar()
        self.var2 = tk.IntVar()
        self.InitializeComponents()
    def Run(self):
        self.root.mainloop()
        
    def InitializeComponents(self):
        tk.Label(self.root, text="Signal Processing ", font=('Comic Sans MS', 15)).grid(row=0)
        rows = 0
        while rows < 50:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows += 1
        nb=ttk.Notebook(self.root)
        nb.grid(row=1,column=0,columnspan=50,rowspan=50,sticky='NESW')
        #--------------------------------------------Task1---------------------------------------------------------------#
        page1=ttk.Frame(nb)
        nb.add(page1,text="Task1")
        ttk.Label(page1, text="Generate Signal", font=('Comic Sans MS', 15)).grid(row=1)
        ttk.Label(page1, text="Range Numbers ", font=('Comic Sans MS', 10)).grid(row=2,column=0)
        self.textbox1=ttk.Entry(page1)
        self.textbox1.grid(row=2,column=1)
        ttk.Label(page1, text="no. Samples ", font=('Comic Sans MS', 10)).grid(row=3,column=0)
        self.textbox2=ttk.Entry(page1)
        self.textbox2.grid(row=3,column=1)
        ttk.Button(page1,text='Writ to File', command=self.WriteToMyFile).grid(row=4,column=1,sticky=tk.W)
        ttk.Button(page1,text='Read Signal', command=self.ReadMyFirstSignal).grid(row=4,column=2,sticky=tk.W)
        ttk.Radiobutton(page1,text="Discrete",command=self.RadioOption1,value=1).grid(row=4,column=3,sticky=tk.W)
        ttk.Radiobutton(page1,text="Continuous",command=self.RadioOption2,value=2).grid(row=4,column=4,sticky=tk.W)
        #----------------------------------------------End Task1---------------------------------------------------------#
        #-----------------------------------------------Task2-------------------------------------------------------------#
        page2=ttk.Frame(nb)
        nb.add(page2,text="Task2")
        ttk.Label(page2, text="Operations On Signal", font=('Comic Sans MS', 15)).grid(row=1)
        #/Amplitude / Kernal/ Omega
        tk.Label(page2, text="Multiply/no.Bits/no.level", font=('Comic Sans MS', 10)).grid(row=7,column=0)
        self.textbox3=ttk.Entry(page2)
        self.textbox3.grid(row=7,column=1)
        mainframe = ttk.Frame(page2)
        mainframe.grid(column=0,row=3, sticky=(tk.N,tk.W,tk.E,tk.S) )
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        choices = ['Choose Operation','Multiply','Adding','Subtract','QuantizationBits','QuantizationLevels']
        self.DropDown = tk.StringVar(page2)   
        self.DropDown.set('Choose Operation') # set the default option         
        popupMenu = tk.OptionMenu(mainframe, self.DropDown, *choices)
        popupMenu.grid(row = 3, column =0)
        ttk.Button(page2,text='Read Signal', command=self.ReadMyFirstSignal).grid(row=2,column=0,sticky=tk.W)
        ttk.Button(page2,text='Resulted Signal',command=self.PlotMyResultedSignal).grid(row=2,column=1,sticky=tk.W)
        ttk.Radiobutton(page2,text="Discrete",command=self.RadioOption1,value=1).grid(row=2,column=2,sticky=tk.W)
        ttk.Radiobutton(page2,text="Continuous",command=self.RadioOption2,value=2).grid(row=2,column=3,sticky=tk.W)
        #----------------------------------------------End Task2----------------------------------------------------------#
        #-----------------------------------------------Task3-------------------------------------------------------------#
        page3=ttk.Frame(nb)
        nb.add(page3,text="Task3")
        ttk.Label(page3, text="More Operations On Signal", font=('Comic Sans MS', 15)).grid(row=1)
        ttk.Button(page3,text='Read Signal', command=self.ReadMyFirstSignal).grid(row=2,column=0,sticky=tk.W)
        ttk.Button(page3,text='Plot Generated Signal', command=self.PlotmyGeneratedSignal).grid(row=2,column=1,sticky=tk.W)
        ttk.Button(page3,text='Resulted Signal',command=self.PlotMyResultedSignal).grid(row=2,column=2,sticky=tk.W)
        ttk.Label(page3, text="Number Of Sampling").grid(row=3,column=0)
        self.textbox2=ttk.Entry(page3)
        self.textbox2.grid(row=3,column=1)
        ttk.Label(page3, text="Amplitude").grid(row=4,column=0)
        self.textbox4=ttk.Entry(page3)
        self.textbox4.grid(row=4,column=1)
        ttk.Label(page3, text="Analog Frequency").grid(row=5,column=0)
        self.textbox6=ttk.Entry(page3)
        self.textbox6.grid(row=5,column=1)
        ttk.Label(page3, text="Sampling Frequency").grid(row=6,column=0)
        self.textbox5=ttk.Entry(page3)
        self.textbox5.grid(row=6,column=1)
        ttk.Label(page3, text="Phase Shift").grid(row=7,column=0)
        self.textbox7=ttk.Entry(page3)
        self.textbox7.grid(row=7,column=1)
        ttk.Label(page3, text="Kernel").grid(row=8,column=0)
        self.textbox1=ttk.Entry(page3)
        self.textbox1.grid(row=8,column=1)
        ttk.Label(page3,text="Choose Your Operation:").grid(row=9,column=0)
        mainframe2 = tk.Frame(page3)
        mainframe2.grid(column=1,row=9, sticky=(tk.N,tk.W,tk.E,tk.S) )
        mainframe2.columnconfigure(0, weight = 1)
        mainframe2.rowconfigure(0, weight = 1)
        self.DropDown2 = tk.StringVar(page3)         
        choices2 = [ 'Choose Operation','Sin','Cosine','Normalize01','Normalize-11','Moving Average','Derivative'
                    ,'DC Component']
        self.DropDown2.set('Choose Operation') # set the default option         
        popupMenu2 = tk.OptionMenu(mainframe2, self.DropDown2, *choices2)
        popupMenu2.grid(row =9, column =1)
        ttk.Radiobutton(page3,text="Discrete",command=self.RadioOption1,value=1).grid(row=2,column=3,sticky=tk.W)
        ttk.Radiobutton(page3,text="Continuous",command=self.RadioOption2,value=2).grid(row=2,column=4,sticky=tk.W)
        #----------------------------------------------End Task3----------------------------------------------------------#
        #-----------------------------------------------Task4-------------------------------------------------------------#
        page4=ttk.Frame(nb)
        nb.add(page4,text="Task4")
        ttk.Label(page4, text="DFT And IDFT", font=('Comic Sans MS', 15)).grid(row=1)
        ttk.Button(page4,text='Read Signal', command=self.ReadMyFirstSignal).grid(row=2,column=0,sticky=tk.W)
        ttk.Button(page4,text='Plot Generated Signal', command=self.PlotmyGeneratedSignal).grid(row=2,column=1,sticky=tk.W)
        ttk.Radiobutton(page4,text="Discrete",command=self.RadioOption1,value=1).grid(row=2,column=3,sticky=tk.W)
        ttk.Radiobutton(page4,text="Continuous",command=self.RadioOption2,value=2).grid(row=2,column=4,sticky=tk.W)
        ttk.Label(page3,text="Choose Your Operation:").grid(row=3,column=0)
        mainframedft = tk.Frame(page4)
        mainframedft.grid(column=1,row=3, sticky=(tk.N,tk.W,tk.E,tk.S) )
        mainframedft.columnconfigure(0, weight = 1)
        mainframedft.rowconfigure(0, weight = 1)
        self.DropDowndft = tk.StringVar(page4)         
        choices2 = [ 'Choose Operation','DFT','IDFT']
        self.DropDowndft.set('Choose Operation') # set the default option         
        popupMenudft = tk.OptionMenu(mainframedft, self.DropDowndft, *choices2)
        popupMenudft.grid(row =3, column =1)
        #----------------------------------------------End Task4----------------------------------------------------------#
        #-----------------------------------------------Task5-------------------------------------------------------------#
        page5=ttk.Frame(nb)
        nb.add(page5,text="Task5")
        ttk.Label(page5, text="FFT and IFFT", font=('Comic Sans MS', 15)).grid(row=1)
        ttk.Button(page5,text='Read Signal', command=self.ReadMyFirstSignal).grid(row=2,column=0,sticky=tk.W)
        ttk.Button(page5,text='Plot Generated Signal', command=self.PlotmyGeneratedSignal).grid(row=2,column=1,sticky=tk.W)
        ttk.Button(page5,text='Resulted Signal',command=self.PlotMyResultedSignal).grid(row=2,column=2,sticky=tk.W)
        ttk.Radiobutton(page5,text="Discrete",command=self.RadioOption1,value=1).grid(row=2,column=3,sticky=tk.W)
        ttk.Radiobutton(page5,text="Continuous",command=self.RadioOption2,value=2).grid(row=2,column=4,sticky=tk.W)
        ttk.Label(page5, text="Shift Signal").grid(row=3)
        self.textboxshift=ttk.Entry(page5)
        self.textboxshift.grid(row=3,column=1)
        ttk.Label(page5,text="Choose Your Operation:").grid(row=4,column=0)
        mainframeifft = tk.Frame(page5)
        mainframeifft.grid(column=1,row=4, sticky=(tk.N,tk.W,tk.E,tk.S) )
        mainframeifft.columnconfigure(0, weight = 1)
        mainframeifft.rowconfigure(0, weight = 1)
        self.DropDownifft = tk.StringVar(page5)         
        choices2 = [ 'Choose Operation','FFT','IFFT','FoldSignal','RemoveDcComponent'
                   ,'ShiftSignal','ShiftFoldedSignal','Accumulate','ZeroCrossing']
        self.DropDownifft.set('Choose Operation') # set the default option         
        popupMenuifft = tk.OptionMenu(mainframeifft, self.DropDownifft, *choices2)
        popupMenuifft.grid(row =4, column =1)
        #----------------------------------------------End Task5----------------------------------------------------------#
        #-----------------------------------------------Task6-------------------------------------------------------------#
        page6=ttk.Frame(nb)
        nb.add(page6,text="Task6")
        ttk.Label(page6, text="Convolution and Correlation", font=('Comic Sans MS', 15)).grid(row=0)
        ttk.Button(page6,text='Read Signal', command=self.ReadMyFirstSignal).grid(row=1,column=0,sticky=tk.W)
        ttk.Button(page6,text='Plot Generated Signal', command=self.PlotmyGeneratedSignal).grid(row=1,column=1,sticky=tk.W)
        ttk.Radiobutton(page6,text="Discrete",command=self.RadioOption1,value=1).grid(row=1,column=3,sticky=tk.W)
        ttk.Radiobutton(page6,text="Continuous",command=self.RadioOption2,value=2).grid(row=1,column=4,sticky=tk.W)
        ttk.Label(page6, text="Choose Convolution").grid(row=2)
        mainframe3 = ttk.Frame(page6)
        mainframe3.grid(column=1,row=2, sticky=(tk.N,tk.W,tk.E,tk.S) )
        mainframe3.columnconfigure(0, weight = 1)
        mainframe3.rowconfigure(0, weight = 1)
        self.DropDown3 = tk.StringVar(page6)         
        choices3 = ['Direct Convolution','Fast Convolution']
        self.DropDown3.set('Choose') # set the default option
        popupMenu3 = tk.OptionMenu(mainframe3, self.DropDown3, *choices3)
        popupMenu3.grid(row =2, column =1)       
        tk.Label(page6, text="Choose Correlation").grid(row=3,column=0)
        mainframe4 = ttk.Frame(page6)
        mainframe4.grid(column=1,row=3, sticky=(tk.N,tk.W,tk.E,tk.S) )
        mainframe4.columnconfigure(0, weight = 1)
        mainframe4.rowconfigure(0, weight = 1)
        self.DropDown4 = tk.StringVar(page6)         
        choices4 = {'Direct Auto Norm','Direct Auto NonNorm','Fast Auto Norm','Fast Auto NonNorm','Direct Cross Norm','Direct Cross NonNorm','Fast Cross Norm','Fast Cross NonNorm'}
        self.DropDown4.set('Choose') # set the default option
        popupMenu4 = tk.OptionMenu(mainframe4, self.DropDown4, *choices4)
        popupMenu4.grid(row=3, column=1)
        #----------------------------------------------End Task6----------------------------------------------------------#
        #-----------------------------------------------Task7-------------------------------------------------------------#
        page7=ttk.Frame(nb)
        nb.add(page7,text="Task7")
        ttk.Label(page7, text="Filters", font=('Comic Sans MS', 15)).grid(row=1)
        ttk.Label(page7, text="Fs", font=('Comic Sans MS', 10)).grid(row=2,column=0)
        self.textbox8=ttk.Entry(page7)
        self.textbox8.grid(row=2,column=1)
        ttk.Label(page7, text="Stop Band Attenuation", font=('Comic Sans MS', 10)).grid(row=3,column=0)
        self.textbox9=ttk.Entry(page7)
        self.textbox9.grid(row=3,column=1)
        ttk.Label(page7, text="Cutt Off Frequency", font=('Comic Sans MS', 10)).grid(row=4,column=0)
        self.textbox10=ttk.Entry(page7)
        self.textbox10.grid(row=4,column=1)
        ttk.Label(page7, text="Cutt Off Frequency2", font=('Comic Sans MS', 10)).grid(row=5,column=0)
        self.textbox12=ttk.Entry(page7)
        self.textbox12.grid(row=5,column=1)
        ttk.Label(page7, text="Transition Band", font=('Comic Sans MS', 10)).grid(row=6,column=0)
        self.textbox11=ttk.Entry(page7)
        self.textbox11.grid(row=6,column=1)
        ttk.Label(page7, text="Filters", font=('Comic Sans MS', 10)).grid(row=7,column=0)
        mainframe5 = ttk.Frame(page7)
        mainframe5.grid(column=1,row=7, sticky=(tk.N,tk.W,tk.E,tk.S))
        mainframe5.columnconfigure(0, weight = 1)
        mainframe5.rowconfigure(0, weight = 1)
        self.DropDown5 = tk.StringVar(page7)
        self.DropDown5.set("Choose Filter") # set the default option         
        choices5 = ['Choose Filter','Low Pass Filter','High Pass Filter','Band Pass Filter','Band Stop Filter']        
        popupMenu5 = ttk.OptionMenu(mainframe5, self.DropDown5, *choices5)
        popupMenu5.grid(row =19, column =1)
        ttk.Checkbutton(page7,text="Coeffecients",variable=self.var1).grid(row=12,sticky=tk.W)
        ttk.Checkbutton(page7,text="Filter",variable=self.var2).grid(row=13,sticky=tk.W)
        ttk.Button(page7,text='Read Signal', command=self.ReadMyFirstSignal).grid(row=2,column=3,sticky=tk.W)
        ttk.Button(page7,text='Plot Generated Signal', command=self.PlotmyGeneratedSignal).grid(row=2,column=4,sticky=tk.W)
        ttk.Radiobutton(page7,text="Discrete",command=self.RadioOption1,value=1).grid(row=3,column=3,sticky=tk.W)
        ttk.Radiobutton(page7,text="Continuous",command=self.RadioOption2,value=2).grid(row=3,column=4,sticky=tk.W)
        #------------------------------------------End Task7-------------------------------------------------------------#