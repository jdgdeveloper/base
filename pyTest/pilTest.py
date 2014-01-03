import Tkinter as tk
from PIL import Image,ImageTk

root=tk.Tk()
root.title('background image')

imageFile="chair.jpg"
image1=ImageTk.PhotoImage(Image.open(imageFile))

w=image1.width()
h=image1.height()

x=0
y=0

root.geometry("%dx%d+%d+%d" % (w,h,x,y))
panel1=tk.Label(root,image=image1)
panel1.pack(side='top',fill='both',expand='yes')

button2=tk.Button(panel1,text='button2')
button2.pack(side='top')

panel1.image=image1

root.mainloop()
