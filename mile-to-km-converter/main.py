import tkinter

window = tkinter.Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


def calculate_function():
    miles = float(miles_entry.get())
    result = round(miles * 1.609, 1)
    km_result = str(result)
    km_output.config(text=km_result)

#Labels
label_1 = tkinter.Label(text="is equal to", font=("Arial", 14, "normal"))
label_1.grid(column=0, row=1)

miles_label = tkinter.Label(text="Miles", font=("Arial", 14, "normal"))
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km", font=("Arial", 14, "normal"))
km_label.grid(column=2, row=1)

km_output = tkinter.Label(text="0")
km_output.grid(column=1, row=1)

#Entries
miles_entry = tkinter.Entry(width=10)
miles_entry.get()
miles_entry.grid(column=1, row=0)


#Buttons
button = tkinter.Button(text="Calculate", command=calculate_function)
button.grid(column=1, row=2)





window.mainloop()