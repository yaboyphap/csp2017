

from Tkinter import *   
import PIL    
from PIL import ImageTk 

import os.path              
__dir__ = os.path.dirname(os.path.abspath(__file__))  
filename = os.path.join(__dir__, 'hillery.JPG')


img = PIL.Image.open(filename)

root = Tk() 

rotation = IntVar()
rotSlider = Scale(root,variable=rotation, from_=1, to=20,
                  orient=VERTICAL, label='Degrees')
rotation.set(10)
rotSlider.grid(column=0, row=0, sticky=W)


iteration = IntVar()
iterSlider = Scale(root,variable=iteration, from_=1, to=15,
                   orient=VERTICAL, label='Iterations')
iteration.set(6)
iterSlider.grid(column=0, row=1, sticky=W)


reduction = DoubleVar()
reduceSlider = Scale(root,variable=reduction, from_=0.5, to=0.99,
                     orient=VERTICAL, resolution=.01, label='Reduction')
reduction.set(.95)
reduceSlider.grid(column=0, row=2, sticky=W)


ccw = IntVar()
direction = Checkbutton(root, variable=ccw,
                        text='Reverse', offvalue=-1) 
ccw.set(1)
direction.grid(column=0, row=3, sticky=W)


canvas = Canvas(root, height=600, width=600, bg= '#b3ffb3')
canvas.grid(column=1, row=0, rowspan=4, sticky=W)


canvas.imglist=[] 


def stamp(event):
    def iterate(iterations_remaining):
        if iterations_remaining>0:
            # Resize
            i = iteration.get() - iterations_remaining
            iterated_img = img.resize( 
                                       ( int(width*reduction.get()**i), 
                                         int(height*reduction.get()**i)
                                       ) 
                                     )                
                                 
           
            iterated_img = iterated_img.rotate(i*rotation.get()*ccw.get(),
                                               expand=True) 
        
           
            iterated_img = iterated_img.convert('RGBA')
    
           
            bounds = iterated_img.getbbox()
            iterated_img = iterated_img.crop(bounds)

            
            tkimg = PIL.ImageTk.PhotoImage(iterated_img)
            canvas.imglist.append(tkimg)
            canvas.create_image(event.x, event.y, image=tkimg)

            
            canvas.after(100, iterate, 
                         iterations_remaining-1) 

  
    width, height = img.size
    iterate(iteration.get())
    
                

canvas.bind('<ButtonPress-1>', stamp)
 
root.mainloop() 