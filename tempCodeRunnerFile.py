import tkinter as tk
class MainWindow:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Interactive GUI")
        self.root.geometry("300x200")
        
        self.label = tk.Label(root,text="Click the button!")
        self.label.pack()
        
        self.button = tk.Button(root,text="Click Me",command=self.on_button_click)
        self.button.pack()
    def on_button_click(self):
        self.label.config(text="Button Clicked")
        
root= tk.Tk()
app = MainWindow(root)
root.mainloop()