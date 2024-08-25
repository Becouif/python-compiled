import tkinter as tk
import pyjokes
from locale import windows_locale
joke = pyjokes.get_joke()
# creating the main window
screen = tk.Tk()

screen.title('Pyjokes')

# add a label to the windows
label = tk.Label(screen, text=joke, font=('Arial', 40))
label.pack()

# run the window
screen.mainloop()