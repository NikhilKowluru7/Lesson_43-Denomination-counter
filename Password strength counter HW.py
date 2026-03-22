from tkinter import *
window = Tk()
window.title("Length Converter App")
window.geometry("400x400")
lbl = Label(text="Enter your password: ")
lbl.pack()
e = Entry(show="*")
e.pack()
result = Label(text="")
result.pack()
def check_strength():
    password = e.get()
    length = len(password)
    if length <= 5:
        result.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result.config(text="Medium", fg=" dark yellow")
    elif 9 <= length <= 12:
        result.config(text="Strong", fg="light green")
    else:
        result.config(text="Very Strong", fg="dark green")
btn = Button(text="Check Strength", command=check_strength)
btn.pack()
window.mainloop()