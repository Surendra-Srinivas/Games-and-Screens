import os,sys
import threading
from tkinter import *
def main():
    class Mymenu:
        def __init__(self,root):
            self.menubar=Menu(root)#create a Menubar
            root.config(menu=self.menubar)#attach it to the root window
            self.filemenu=Menu(root,tearoff=0)#Create a file menu
            # Create menu items in file menu
            self.filemenu.add_command(label="New File",command=self.donothing)
            self.filemenu.add_command(label="Open File",command=self.donothing)
            self.filemenu.add_command(label="Save File",command=self.donothing)
            self.filemenu.add_separator() # Add a horizontal line as seperator.
            self.filemenu.add_command(label="Exit",command=root.destroy)
            self.filemenu.add_cascade(label="File",menu=self.filemenu) # Name the filemenu as "File". 
            self.editmenu=Menu(root,tearoff=0) # create edit menu.
            #Create menu items in the Edit menu.
            self.editmenu.add_command(label="Copy",command=self.donothing)
            self.editmenu.add_command(label="Paste",command=self.donothing)
            self.editmenu.add_command(label="Cut",command=self.donothing)
            self.editmenu.add_command(label="Exit",command=root.destroy)
            self.editmenu.add_cascade(label="Edit",menu=self.editmenu)
        def donothing(self):
            pass
    root=Tk()
    root.title("A menu example.")
    mm=Mymenu(root)
    root.geometry("600x350")
    root.mainloop()
sys.setrecursionlimit(2097152)    # adjust numbers
threading.stack_size(134217728)   # for your needs
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
print(sys.getrecursionlimit())
main()