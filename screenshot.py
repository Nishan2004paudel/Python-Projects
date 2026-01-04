import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import pyscreenshot as ImageGrab

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def takeScreenshot():
    save_path = asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if save_path:
        im = ImageGrab.grab()
        im.save(save_path)

myButton = tk.Button(text="Take Screenshot", command=takeScreenshot, font=10)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()







