from tkinter import *
import time






def start():



    try:
        num = inp.get()
        int_answer = int(num)+1

        while int_answer > 0:
            time.sleep(1)
            result.config(text="")
            int_answer = int_answer - 1

            display.config(text=int_answer)
            root.update()
        result.config(text="Countdown is over!")


    except:
        display.config(text="Please enter a Number")
        root.update()

root = Tk()
root.geometry("250x300")
root.title("Timer")
root.resizable(False,False)
display = Label(root,bg="#b5d9ff",width=300,text="")
display.pack()
inp = Entry(root,bg="white")
inp.pack()
button = Button(root,text="Start",command=start)

button.pack()

result = Label(root,text="",font="arial,30",fg="red")
result.pack()



root.mainloop()