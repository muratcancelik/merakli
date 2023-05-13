import tkinter as tk
from tkinter import *
import time
from tkinter import messagebox
import vlc
import winsound



def center_window(w=300, h=200):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
     # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))



class x():
    def __init__(self):
        self.l1 = tk.Label(text="Şu an ne yapıyorsun ?",font=("Arial",15),fg='#aaa')
        self.l1.place(x=190, y=1)
        self.E1 = tk.Text(width=70)
        self.E1.place(x=20, y=50,height=60)
        self.B1=tk.Button(text="Bunları yaptım.",command=self.save)
        self.B1.place(x=210,y=120)
    def save(self):
        self.a=(self.E1.get(1.0, "end-1c"))
        self.txt=open("C:\\Users\\Muroc\\Desktop\\Bunları yaptım.txt","a+")
        self.txt.write("{}\n".format(self.a))
        self.txt.close()
        self.msg=messagebox.showwarning("Meraklı","Merakımı giderdiğin için teşekkür ederim :)")
        self.E1.delete("1.0",END)
        window.withdraw()
        for i in range(10, 0, -1):
            time.sleep(1)
            print(i)
            if i == 5:
                window.deiconify()
                #duration=3000
                #freqz=400
                #winsound.MessageBeep(freqz,duration)

    def clear(self):
        pass

window = tk.Tk()
window.title("Meraklı")
#window.geometry("600x150")
center_window(600,150)

x()
window.mainloop()
