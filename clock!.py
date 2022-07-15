from tkinter import *
import time

root = Tk()
root.title("Clock")
width = 1000
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)- (width/2)
y = (screen_height/2)- (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
#root.resizable(0, 0)
root.config(bg="red")
def tick():

    setTime=time.strftime('Time: %I: %M %S %p')
    clock.config(text=setTime)
    clock.after(200,tick)
Top = Frame(root, width=1000, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=1000)
Mid.pack(side=TOP, expand=1)
lbl_title = Label(Top, text="kir arshia", width=1000, font=("Arial Black", 20))
lbl_title.pack(fill=X)


clock= Label(Mid, font=('BAUHS93.TTF', 50 , 'bold'), fg="red", bg="black")
clock.pack()
if __name__=='__main__':
    tick()
    root.mainloop()