import tkinter as tk
from tkinter import messagebox 
import sys

sys.path.append("Path to module")

import Generator 
generator = Generator.Generator(16)



def generate():
	pass_ = generator.make_it_more_randomly()
	messagebox.showinfo("Password", f"Your new password is  {pass_}")

root = tk.Tk()


label_1 = tk.Label(root, 
				text='Password generator and saver').grid(row=0, 
														column=0)
label_2 = tk.Label(root, 
				text='Try to generate your new password').grid(row=1, 
															column=0)

but = tk.Button(root, text="Tap to generate", command=generate).grid(row=2,
																	column=0)
root.mainloop()

