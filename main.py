from Tkinter import *
from TkfinalClass import *
import webbrowser
import tkMessageBox
from groceryClass import *
import io
import time

def main():
    root = Tk()
    window1 = TkClass(root, "BrokeNhungry", "white", '300x380+400+100', "logo.gif")
    window1.setupmainwin()

main()