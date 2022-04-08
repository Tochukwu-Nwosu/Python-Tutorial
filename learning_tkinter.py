import tkinter as tk

# from tkinter import messagebox

# main_window = tk.Tk()  # This creates the window

# main_window.title("Dollar To Naira Converter")    # This gives our window a title
# main_window.geometry("500x500")                   # This set the size of our window

# def calculate():
#     dollar_value = eval(entry1.get())
#     naira_value = dollar_value * 400
#     label1.configure(text= naira_value)
#     # messagebox.showinfo("Dollar to Naira", naira_value)



# entry1 =tk.Entry()                               # Creating the widget
# entry1.grid(row= 0, column= 0)                   # Positioning the widget entry

# label1 = tk.Label(text="Enter Amount in Dollar:", fg= "blue", bg= "yellow")  # Creating the widget
# label1.grid(row=1, column=0)                      # Positioning the widget label

# button1 = tk.Button(text="Submit", bg= "green", command= calculate) # Creating the widget
# button1.grid(row= 2, column= 0)                 # Positioning the widget button

# main_window.mainloop()  # This makes our window to be open

# Exercise

main_window = tk.Tk()

main_window.geometry("400x400")
main_window.title("Widget")  

# Widget example
# Label Frame
label_frame = tk.LabelFrame(text="Question", padx=20, pady=20)
label_frame.grid(row= 0, column= 0)

# Label
label1 = tk.Label(label_frame, text="Do you like Python? ")
label1.grid(row= 1, column= 0)

# Radiobutton
radio_button1 = tk.Radiobutton(label_frame, text="Yes", value=1)
radio_button1.grid(row= 2, column= 0)
radio_button2 = tk.Radiobutton(label_frame, text="No", value=2)
radio_button2.grid(row= 3, column= 0)

main_window.mainloop()