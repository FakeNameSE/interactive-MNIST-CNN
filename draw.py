#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import subprocess
import sys

class Paint(object):

    DEFAULT_PEN_SIZE = 10
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Hal")

        self.eraser_button = Button(self.root, text='Clear', command=self.clear)
        self.eraser_button.grid(row=0, column=0)
        
        self.done_button = Button(self.root, text='Done', command=self.done)
        self.done_button.grid(row=0, column=1)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=2)
        self.choose_size_button.set(10)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None
        
    def clear(self):
        self.c.delete("all")
        self.setup()
        
    def close_window (self, window): 
        window.destroy()
		    
    def done(self):
        self.c.postscript(file="imgs/interactive.ps", colormode='gray')
        tkMessageBox.showinfo("Done", "Click OK to watch the magic happen!")
        
        subprocess.check_output(['convert','-background', 'white', 
        '-alpha', 'remove','imgs/interactive.ps', 'imgs/interactive.png'])
        
        subprocess.check_output(['rm','imgs/interactive.ps'])
        
        subprocess.check_output(['convert', '-trim', '-border', '20', 
        '-bordercolor', 'white', 'imgs/interactive.png', 'imgs/interactive.png'])
        
        subprocess.call('python2 predict.py', shell=True)

        self.close_window(self.root)


ge = Paint()
