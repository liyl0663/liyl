import tkinter
from functools import partial
root = tkinter.Tk()
lb = tkinter.Label(root,text='hello world',font='20')
#b1 = tkinter.Button(root,bg='blue',fg='white',text='Button 1')
MyButton = partial(tkinter.Button,root,bg='blue',fg='white')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
b3 = MyButton(text='Button 3')
b4 = MyButton(text='Quit',command=root.quit)
for item in [lb,b1,b2,b3,b4]:
    item.pack()
root.mainloop()