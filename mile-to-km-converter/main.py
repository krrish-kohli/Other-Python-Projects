from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


def button_clicked():
    new_unit = float(miles.get()) * 1.609
    km.config(text=new_unit)


# Entry for number of miles
miles = Entry(width=7)
miles.grid(column=1, row=0)

# Writing Miles as a unit after the number.
text_miles = Label(text="Miles")
text_miles.grid(column=2, row=0)

# Writing "is equal to" text on the window.
text_equal = Label(text="is equal to")
text_equal.grid(column=0, row=1)

# Getting and writing the converted km on screen.
km = Label(text="0")
km.grid(column=1, row=1)

# Writing Km as a unit after the number.
text_km = Label(text="Km")
text_km.grid(column=2, row=1)

# Adding the calculate button.
calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)


window.mainloop()
