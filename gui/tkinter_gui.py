import tkinter as tk
from pandastable import Table
from utils import get_data as gd

mids = gd.get_mids()
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
pt = Table(frame, dataframe=mids)
pt.show()
root.mainloop()
