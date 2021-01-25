import tkinter as tk
from tkinter import *

first = tk.Tk()
first.title("Serial Position Effect")

base = tk.Canvas(first,bg='light cyan', width = 800, height = 400)
base.pack()

head = tk.Label(first, text='Instructions')
head.config(font=('Times', 30),bg='light cyan')
base.create_window(400, 70, window=head)

in1 = tk.Label(first, text='1. Once you click the get started button, a window appears displaying a list of 10 animals.')
in1.config(font=('Times', 15),bg='light cyan')
base.create_window(400, 150, window=in1)

in2 = tk.Label(first, text='2. It appears only for 10 seconds. Try to memorize the animals displayed in the list.')
in2.config(font=('Times', 15),bg='light cyan')
base.create_window(374, 200, window=in2)

in3 = tk.Label(first, text='3. After completion of 10 seconds, another window appears which contains 18 animals.')
in3.config(font=('Times', 15),bg='light cyan')
base.create_window(393, 250, window=in3)

in4 = tk.Label(first, text='4. Select the previously memorized animals and click on the button below.')
in4.config(font=('Times', 15),bg='light cyan')
base.create_window(340, 300, window=in4)

def click_me():
    first.destroy()
    import main

z = Button(first, text="Get Started", command=click_me)
z.config(font=('georgia', 15),fg='white smoke',bg='black')
z.pack(padx=15, pady=15)
first.mainloop()