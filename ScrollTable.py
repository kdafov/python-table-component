import tkinter as tk
import Register

class Config(tk.Frame):
    """
    Config class which will create the required frame, scrollbars, and
    set the size of all elements. Additionally, it will add all elements
    configured by the user from the .config file
    """
    
    canvas, xbar, ybar = None, None, None
    instructions = []
    
    def __init__(self, parent, *args, **kwargs):
        # Constructor
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.getInstructions()
        self.setSize(parent)
        self.createCanvas(parent)
        self.createScrollBars(parent)
        self.populateFrame(parent)

    def getInstructions(self):
        # Store list of commands locally
        self.instructions = Register.Main().getInstructions()

    def setSize(self,parent):
        # Set size of frame
        try:
            #Apply geometry settings (if Tk())
            parent.geometry(self.instructions[0])
        except:
            #If not Tk() but Frame given
            parent.config(width=self.instructions[0].split("x")[0],\
                          height=self.instructions[0].split("x")[1])

    def createCanvas(self,parent):
        # Create canvas to hold all items in table
        self.canvas = tk.Canvas(parent, width= \
                            self.instructions[1].split("x")[0],\
                            height=self.instructions[1].split("x")[1])
        self.canvas.grid(row=0,column=0)

    def configCanvas(self,event):
        # <Configure> event handler
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
    def createScrollBars(self,parent):
        # Create horizontal and vertical scroll bars and configure them
        self.ybar = tk.Scrollbar(parent, command=self.canvas.yview, \
                            width=(int(self.instructions[0].split("x")[0])\
                            - int(self.instructions[1].split("x")[0])))
        self.ybar.grid(row=0,column=1,sticky=tk.NS)

        self.xbar = tk.Scrollbar(parent, command=self.canvas.xview, \
                            orient=tk.HORIZONTAL, width=(int(self.instructions\
                            [0].split("x")[1]) - int(self.instructions[1]\
                            .split("x")[1])))
        self.xbar.grid(row=2,column=0,sticky=tk.EW,columnspan=2)

        self.canvas.configure(yscrollcommand=self.ybar.set)
        self.canvas.configure(xscrollcommand=self.xbar.set)
        self.canvas.bind('<Configure>', self.configCanvas)

    def populateFrame(self,parent):
        # Add all items set by the user (in the config file) to the canvas
        frame = tk.Frame(self.canvas,highlightbackground="black",\
                             highlightthickness=1,bg="black")
        self.canvas.create_window((0,0), window=frame, anchor='nw')

        for item in self.instructions[2:]:
            cnf = item.split(",")
            label = tk.Label(frame,text=cnf[0],bg=cnf[1],fg=cnf[2],font=\
                             (cnf[3],int(cnf[4]),cnf[5]),wraplength=int(cnf[6]))
            label.grid(row=cnf[8],column=cnf[7],rowspan=cnf[9],columnspan=cnf\
                               [10],sticky=tk.W+tk.E+tk.S+tk.N,padx=(cnf[11],\
                                cnf[13]),pady=(cnf[12],cnf[14]),ipadx=cnf[15],\
                                   ipady=cnf[16])
        

class Main(tk.Frame):
    """
    Create a new Tk() window and call the config class
    """
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        Config(self.parent)

        

if __name__ == "__main__":
    app = tk.Tk()
    Main(app)
    app.mainloop()
