from Drawing import GUI
from DrawingFunctions import DrawingHelperFunctions
if __name__ =="__main__":
    gui=GUI()
    Manager=DrawingHelperFunctions(gui)
    Manager.Bind()
    gui.Run()