from tkinter import *
from tkinter import messagebox

win = Tk()

result1 = messagebox.askokcancel("Creating Account", "Do you really want to create an account? ")
print(result1) #Yes = True , No = False

result2 = messagebox.askyesno("Confirmation", "Do you really want to proceed? ")
print(result2) #Yes = True , No = False

result3 = messagebox.askyesnocancel("You're about to enter the page of creation", "Are you ready to proceed? ")
print(result3) #Yes = True , No = False , cancel = None

messagebox.showinfo("Message", "a Tk MessageBox")
messagebox.showwarning("Warning", "a Tk warning")
messagebox.showerror("Error", "a Tk error")

win.mainloop()