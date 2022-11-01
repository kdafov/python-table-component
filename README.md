# Python module to create a table with custom items

This python module will allow you to create fully customisable excel-like tables with 2 simple steps in Python's graphic user interface Tkinter. The code can run independently or integrated into another Tkinter program. 

## Requirements
* Git installed on local PC
* Python 3.x


## Download necesary files to run configuration
***On Windows:***
1. Open command prompt (cmd) in the folder where you want to use the script
2. Run the command `git clone https://github.com/kdafov/python-table-component.git`

***On MacOS/Linux:***
1. Open terminal in the folder where you want to use the script
2. Run the command `git clone https://github.com/kdafov/python-table-component.git`

***Other:***\
If none of the above works, then download the `data.config`, `Register.py`, and `ScrollTable.py` files in the folder where you want to run the table script.


## Configure the `data.config` file
The data.config file is a configuration file which is used to tell the program how you want to design your table, what items you want to add, the background and foreground colors of each item, padding/margin and other settings (as explained below).

The configuration file will look like this at first:
```
# Size of window
550x400

# Size of canvas (holding the table)
# Note: Recommended size is 50 pixels less than size of window
500x350

# Configuration syntax for items:
# text -> The text of the item
# bg -> The background of the block containing the item
# fg -> The color of the text within the block
# font -> The font of the text
# font_size -> The size of the font
# font_style -> Add styling to the text (bold, italic, underline)
# wrap_length -> Maximum length of text before writing on next line (0 - NONE)
# X_coordinate -> X position of item on the grid
# Y_coordinate -> Y position of item on the grid
# row_span -> How many rows to span across (1 - DEFAULT)
# column_span -> How many columns to span vertically (1 - DEFAULT)
# margin_left -> External space on the left side of the text
# margin_top -> External space on the top side of the text
# margin_right -> External space on the right side of the text
# margin_bottom -> External space on the bottom side of the text
# padding_left_right -> Internal space on the left/right of the text
# padding_top_bottom -> Internal space on the top/bottom of the text

# List of items 

Text of label 1,grey,red,Helvetica,10,bold,0,0,0,1,1,0,0,0,0,10,10
Text of label 2,grey,red,Helvetica,10,bold,0,0,1,1,1,0,0,0,0,0,0
Text of label 3,green,red,Helvetica,10,bold,0,1,0,1,1,0,0,0,0,0,0
Text of label 4,green,red,Helvetica,10,bold,0,1,1,1,1,2,2,2,2,0,0
```

At the top of the file you can adjust the size of the main frame (holding the sub-frame and scroll bars), and the size of the sub-frame (the one holding the content of the table). The rest of the file is the configuration for the items. In order to add a new item, you need to define all of the properties listed above (text, bg, fg, font, font_size, font_style, wrap_length, X_coordinate, Y_coordinate, row_span, column_span, margin_left, margin_top, margin_right, margin_bottom, padding_left_right, padding_top_bottom).

The space in which you input X and Y coordinates looks like this:\
![image](https://user-images.githubusercontent.com/94061728/199350589-49ac81e6-5253-4258-9b8a-f9bffd0cd8ee.png)\

The padding and margin configuration:\
![image](https://user-images.githubusercontent.com/94061728/199351615-3e59326a-6772-4ba4-a832-8b79abebbd84.png)

Rowspan and columnspan meanings:\
![image](https://user-images.githubusercontent.com/94061728/199352010-78554fb8-6aa1-4405-ae5d-d5df9ad4bb42.png)


## Example of `data.config` file

Let's say we want to create the following table:\
![image](https://user-images.githubusercontent.com/94061728/199352568-079622c2-fc73-4e1f-950c-f8454e095e7d.png)

Then our configuration file will look like this:
```
# Size of window
600x300

# Size of canvas (holding the table)
# Note: Recommended size is 50 pixels less than size of window
550x250

# List of items 
1,yellow,red,Helvetica,10,bold,100,0,0,1,1,0,0,0,0,15,0
2,green,black,Helvetica,10,bold,100,1,0,1,1,0,0,0,0,15,0
3,yellow,red,Helvetica,10,bold,100,2,0,1,1,0,0,0,0,15,0
4,blue,white,Helvetica,10,bold,100,0,1,1,1,0,0,0,0,0,0
5,black,white,Helvetica,12,italic,100,1,1,1,1,0,0,0,0,0,0
6,blue,white,Helvetica,10,bold,100,2,1,1,1,0,0,0,0,0,0
7,yellow,red,Helvetica,10,bold,100,0,2,1,1,0,0,0,0,0,0
8,green,black,Helvetica,10,bold,100,1,2,1,1,0,0,0,0,0,0
9,yellow,red,Helvetica,10,bold,100,2,2,1,1,0,0,0,0,0,0
```
*Note:* In the script above there is also the option for text_wrap=100 to ***ALL*** elements and padding_x_y=15 to the ***TOP THREE*** elements only as python's tkinter will automatically adjust the rest of the columns according to the biggest element in each one.

**Result:**\
![image](https://user-images.githubusercontent.com/94061728/199353961-ce179003-11ed-43ca-8ffa-a33e86e4b6cb.png)


## Running the script
Once you got the configuration file (`data.config`) setup, you can either run the code independently or as part of another GUI.

**To run independent:**
* Run the `ScrollTable.py` file


**To run as part of another program:**

Let's assume you got the following code:
```
import tkinter as tk

app = tk.Tk()
app.geometry("850x650")

button = tk.Button(app, text="Click to import table", bg="green", fg="white")
button.grid(row=0,column=0)

app.mainloop()
```

...and you want to make it so when you click the button, the table with numbers gets added below in the *same* window.
1. Import the `ScrollTable` module by adding the following line of code to the top:
```
import ScrollTable
```

2. Add command option to the button
```
button = tk.Button(app, text="Click to import table", command=importTable, \
                   bg="green", fg="white")
```

3. Create a frame which will hold the table with numbers:
```
tableFrame = tk.Frame(app)
tableFrame.grid(row=1,column=0)
```

4. Create `importTable` function to handle the button click, and once clicked to call the constructor of the ScrollTable module which will insert the table with numbers to the frame we created above:
```
def importTable():
    ScrollTable.Main(tableFrame)
```


## Thank you
*Thank you for using this code snippet, hopefully it helped you. Feel free to DM me for any suggestions/improvements.*
