import tkinter as tk
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
        self.root.geometry("1300x750")
        self.textbox1=tk.Entry(self.root)
        self.textbox2=tk.Entry(self.root)
        self.textbox3=tk.Entry(self.root)
        self.textbox4=tk.Entry(self.root)
        self.textbox5=tk.Entry(self.root)
        self.textbox6=tk.Entry(self.root)
        self.textbox7=tk.Entry(self.root)
        self.InitializeComponents()
    
    def Run(self):
        self.root.mainloop()
        
    def InitializeComponents(self):
        tk.Label(self.root, text="Signal Processing ", font=('Comic Sans MS', 15)).grid(row=0)
        tk.Label(self.root, text="Enter The Range Of Your Numbers ", font=('Comic Sans MS', 10)).grid(row=1,column=0)
        self.textbox1.grid(row=1,column=1)
        tk.Label(self.root, text="Enter The no of Samples ", font=('Comic Sans MS', 10)).grid(row=2,column=0)
        tk.Label(self.root, text="Amplitude / Kernal/ Omega ", font=('Comic Sans MS', 10)).grid(row=3,column=0)
        self.textbox4.grid(row=3,column=1)
        tk.Label(self.root, text="Analog Frequency ", font=('Comic Sans MS', 10)).grid(row=3,column=2)
        self.textbox5.grid(row=3,column=3)
        tk.Label(self.root, text="Sampling Frequency ", font=('Comic Sans MS', 10)).grid(row=3,column=4)
        self.textbox6.grid(row=3,column=5)
        tk.Label(self.root,text="Choose Your Operation:" , font=('Comic Sans MS', 10)).grid(row=2,column=2)
        
        mainframe = tk.Frame(self.root)
        mainframe.grid(column=3,row=2, sticky=(tk.N,tk.W,tk.E,tk.S) )
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        self.DropDown = tk.StringVar(self.root)         
        choices = { 'Multiply','Adding','Subtract','QuantizationBits','QuantizationLevels','FoldSignal','DcComponent'
                   ,'ShiftSignal','ShiftFoldedSignal','Accumulate','ZeroCrossing'}
        self.DropDown.set('Choose Operation') # set the default option         
        popupMenu = tk.OptionMenu(mainframe, self.DropDown, *choices)
        popupMenu.grid(row = 3, column =3)
        
        mainframe2 = tk.Frame(self.root)
        mainframe2.grid(column=4,row=2, sticky=(tk.N,tk.W,tk.E,tk.S) )
        mainframe2.columnconfigure(0, weight = 1)
        mainframe2.rowconfigure(0, weight = 1)
        self.DropDown2 = tk.StringVar(self.root)         
        choices2 = { 'Sin','Cosine','Normalize01','Normalize-11','Moving Average','Derivative'
                    ,'DC Component','DFT','IDFT','FFT','IFFT'}
        self.DropDown2.set('Sin') # set the default option         
        popupMenu2 = tk.OptionMenu(mainframe2, self.DropDown2, *choices2)
        popupMenu2.grid(row = 3, column =4)
        
        tk.Label(self.root, text="Enter the value of your Operation",font=('Comic Sans MS', 10)).grid(row=1,column=2)
        tk.Label(self.root, text="Phase Shift",font=('Comic Sans MS', 10)).grid(row=1,column=4)
        self.textbox7.grid(row=1,column=5)
        self.textbox3.grid(row=1,column=3)
        self.textbox2.grid(row=2,column=1)
        tk.Label(self.root, text="Create and Choose Your File ", font=('Comic Sans MS', 10)).grid(row=4,column=0)
        tk.Button(text='Writ to File', command=self.WriteToMyFile).grid(row=4,column=1,sticky=tk.W)
        tk.Button(text='Plot Generated Signal', command=self.PlotmyGeneratedSignal).grid(row=4,column=2,sticky=tk.W)
        tk.Label(self.root, text="Read And Plot Your Files ", font=('Comic Sans MS', 10)).grid(row=5,column=0)
        tk.Button(text='Read Signal', command=self.ReadMyFirstSignal).grid(row=5,column=1,sticky=tk.W)
        
        tk.Button(text='Resulted Signal',command=self.PlotMyResultedSignal).grid(row=5,column=2,sticky=tk.W)
        tk.Radiobutton(self.root,text="Discrete",command=self.RadioOption1,value=1).grid(row=5,column=3,sticky=tk.W)
        tk.Radiobutton(self.root,text="Continuous",command=self.RadioOption2,value=2).grid(row=5,column=4,sticky=tk.W)   