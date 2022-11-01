import tkinter as tk
import ScrollTable # <--------------- Import ScrollTable module 

app = tk.Tk()
app.geometry("850x650")

def importTable():
    ScrollTable.Main(tableFrame) # <------- Call the ScrollTable constructor

button = tk.Button(app, text="Click to import table", command=importTable, \
                   bg="green", fg="white")
button.grid(row=0,column=0)

tableFrame = tk.Frame(app) # <---------- Create a frame to hold the ScrollTable
tableFrame.grid(row=1,column=0)

app.mainloop()
