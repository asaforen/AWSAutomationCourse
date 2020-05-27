

import os, sys
import tkinter
import time

global timeout
timeout = 5

def display_file(gifname):
    dirpath = './Bitmaps'
    gifname = gifname.upper()
    if not gifname.endswith('GIF'):
        raise ValueError("Invalid name: <"+gifname+">")
    
    gifpath = os.path.join(dirpath, gifname)
    if not os.path.isfile(gifpath):
    	raise IOError("Incorrect file name: <"+gifpath+">")
  
    global root
    
    root = tkinter.Tk()  
    root.title("Display")
    root.geometry("100x100+0+0")
    #root.wm_iconbitmap('qa.ico')

    Fm = tkinter.Frame(padx=15, pady=15)
    Fm.pack()
    img = tkinter.Label()
    img.pack()

    gif = tkinter.PhotoImage(file=gifpath)
    img.config(image=gif)
    
    #root.after(timeout*1000,remove)
    root.mainloop()
    
def remove():
    global root
      
    try:
        root.destroy()
    except KeyboardInterrupt:
        exit('Ending...');
            
def set_timeout(secs):
    global timeout
    timeout = secs