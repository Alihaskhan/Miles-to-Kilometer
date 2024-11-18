from tkinter import *


def calculate_miles_to_km():
    miles_input = float(input.get())
    km_output = miles_input * 1.6
    label_num_km.config(text=km_output)

    label_num_km.grid(column=1, row=2)



window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=250, height=125)
window.config(pady=20, padx=20)

input = Entry(width=10)
input.grid(column=1, row=1)



label_num_km = Label()

label_mil = Label(text="Miles")
label_mil.grid(column=2, row=1)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=2)

label_km = Label(text="Kilometers")
label_km.grid(column=2, row=2)

button_calc = Button(text="Calculate", command=calculate_miles_to_km)
button_calc.grid(column=1, row=3)


window.mainloop()
