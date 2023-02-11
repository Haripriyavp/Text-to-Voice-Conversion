from gtts import gTTS
import os
from tkinter import *
root=Tk()
can=Canvas(root,width=400,height=350,bg="sky blue")
can.pack()
lab=Label(root,text="Type Something")
can.create_window(200,100,window=lab)
def text_speak():
    text=enter_input.get()
    output=gTTS(text=text,lang='en',slow=False)
    output.save('text_speak.mp3')
    os.system('start text_speak.mp3')

enter_input=Entry(root)
can.create_window(200,180,window=enter_input)
btn=Button(text="Start",command=text_speak)
can.create_window(200,250,window=btn)
root.mainloop()
