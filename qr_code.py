from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()
def generate():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name+ ".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_lab=Label(image=image)
    image_lab.image=image
    canvas.create_window(200,450,window=image_lab)
canvas=Canvas(root,width=400,height=600,bg="black")
canvas.pack()
app_lab=Label(root,text="Q R Code Generator",fg="white",bg="black",font=("Arial",30))
canvas.create_window(200,50,window=app_lab)
name_lab=Label(root,text="Link Name",font=(12))
link_lab=Label(root,text="Link",font=(12))

canvas.create_window(200,100,window=name_lab)
canvas.create_window(200,160,window=link_lab)
name_entry=Entry(root)
link_entry=Entry(root)

canvas.create_window(200,130,window=name_entry)
canvas.create_window(200,180,window=link_entry)
btn=Button(text="Generate",command=generate,font=(12))
canvas.create_window(200,230,window=btn)
root.mainloop()
