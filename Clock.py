from datetime import datetime
import pytz
from tkinter import *
import time

root = Tk()

label_0 = Label(root, text="WORLD CLOCK..!!", width=16, font=("bold", 20),  bg='white' )
label_0.place(x=380, y=55)

root.geometry("1200x400")
image_icon = PhotoImage(file="WorldClock.png")
root.iconphoto(False, image_icon)

def times():
    home = pytz.timezone("Asia/Kolkata")  # Fix the typo in the timezone name
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M:%S")  # Fix the format specifier
    clock.config(text=current_time)
    name.config(text="India")
    clock.after(200,times)

    home2 = pytz.timezone("America/New_york")  # Fix the typo in the timezone name
    local_time2 = datetime.now(home2)
    current_time2= local_time2.strftime("%a %H:%M:%S")  # Fix the format specifier
    clock2.config(text=current_time2)
    name2.config(text="NewYork")
    clock2.after(200,times)

    home3 = pytz.timezone("Europe/London")  # Fix the typo in the timezone name
    local_time3 = datetime.now(home3)
    current_time3= local_time3.strftime("%a %H:%M:%S")  # Fix the format specifier
    clock3.config(text=current_time3)
    name3.config(text="London")
    clock3.after(200,times)

    home4 = pytz.timezone("Asia/Tokyo")  # Fix the typo in the timezone name
    local_time4 = datetime.now(home4)
    current_time4 = local_time4.strftime("%a %H:%M:%S")  # Fix the format specifier
    clock4.config(text=current_time4)
    name4.config(text="Tokyo")
    clock4.after(200,times)
    
#first timezone

f = Frame(root, bd=5)
f.place(x=10, y=118, width=220, height=150)

name = Label(f, font=("Helvetica", 30, "bold"))  # Fix the typo here
name.place(x=50, y=10)

logo = PhotoImage(file="in.png")
image_label = Label(root, image=logo)
image_label.place(x=20, y=150)

clock = Label(f, font=("Helvetica", 20))
clock.place(x=5, y=80)


#second time zone

f2 = Frame(root, bd=5)
f2.place(x=300, y=118, width=220, height=150)

name2 = Label(f2, font=("Helvetica", 30, "bold"))  # Fix the typo here
name2.place(x=30, y=10)

logo2 = PhotoImage(file="us.png")
image_label2 = Label(root, image=logo2)
image_label2.place(x=290, y=150)

clock2 = Label(f2, font=("Helvetica", 20))
clock2.place(x=5, y=80)

#third time zone

f3 = Frame(root, bd=5)
f3.place(x=600, y=118, width=220, height=150)

name3 = Label(f3, font=("Helvetica", 30, "bold"))  # Fix the typo here
name3.place(x=50, y=10)

logo3 = PhotoImage(file="gb.png")
image_label3 = Label(root, image=logo3)
image_label3.place(x=600, y=150)

clock3 = Label(f3, font=("Helvetica", 20))
clock3.place(x=5, y=80)


#fourth time zone

f4= Frame(root, bd=5)
f4.place(x=900, y=118, width=220, height=150)

name4 = Label(f4, font=("Helvetica", 30, "bold"))  # Fix the typo here
name4.place(x=50, y=10)

logo4 = PhotoImage(file="jp.png")
image_label4 = Label(root, image=logo4)
image_label4.place(x=900, y=150)

clock4 = Label(f4, font=("Helvetica", 20))
clock4.place(x=5, y=80)


times()


root.mainloop()
