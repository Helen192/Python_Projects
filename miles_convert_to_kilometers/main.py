from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

# label 1
label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)
label_1.config(padx=10, pady=10)

# entry where user enter number of miles
entry = Entry()
entry.insert(END, string='0')
entry.grid(column=1, row=0)

# button
def convert():
    # get Strings that user enter and convert it to an integer
    input = float(entry.get())
    result = input*1.609
    label_converted["text"] = str(result)

button_calculate = Button(text="Calculate", command=convert)
button_calculate.grid(column=1, row=2)


# label 2
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)
label_miles.config(padx=10)

# label result
label_converted = Label(text="0")
label_converted.grid(column=1, row=1)

#label 4
label_Km = Label(text="Km")
label_Km.grid(column=2, row=1)
label_Km.config(padx=10)



window.mainloop()
