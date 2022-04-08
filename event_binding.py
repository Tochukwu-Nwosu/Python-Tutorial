# Event Binding

# import tkinter as tk
# from tkinter import messagebox

# main_window = tk.Tk()

# main_window.title("Event Binding")
# main_window.resizable(False, False)     # (width, height)
# main_window.geometry("500x500")

# def do_something(event):
#     messagebox.showinfo("Try somethig else", "You clicked the right button")


# btn1 = tk.Button(text="Click Me")
# btn1.grid(row= 0, column= 0, ipadx= 5, ipady= 5, padx= 5, pady= 5)     # pad = margin, ipad = padding
# # btn1.bind("<Button - 1>", do_something)    # LeftButton
# # btn1.bind("<Button - 3>", do_something)    # RightButton
# btn1.bind("<Return>", do_something)          # Enter key

# main_window.mainloop()


# Using tkinter in a class

# import tkinter as tk
# from tkinter import messagebox

# main_window = tk.Tk()

# main_window.title("Event Binding")
# main_window.resizable(False, False)     # (width, height)
# main_window.geometry("500x500")

# class Eventbinding:
#     def __init__(self, master):
#         self.btn1 = tk.Button(text="Click Me")
#         self.btn1.grid(row= 0, column= 0, ipadx= 5, ipady= 5, padx= 5, pady= 5)
#         self.btn1.bind("a", self.do_something)     # key a on your keyboard
    
#     def do_something(self, event):
#         messagebox.showinfo("Try somethig else", "You clicked the right button")

# obj1 = Eventbinding(main_window)

# main_window.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# main_window = tk.Tk()

# main_window.title("Event Binding")
# main_window.resizable(False, False)     # (width, height)
# main_window.geometry("500x500")

# value = 0

# def increment():
#     global value
#     value += 1
#     label1.config(text= value)

# label1 = tk.Label(text= value)
# label1.grid(row= 0, column= 4, ipadx= 3, ipady= 3, padx= 3, pady= 3)

# button1 = tk.Button(text= "Increment your label", command= increment)
# button1.grid(row= 1, column= 4, ipadx= 3, ipady= 3, padx= 3, pady= 3)

# main_window.mainloop()

"""
Assignment
Create a simple calculator
"""

