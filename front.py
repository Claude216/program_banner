import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Simple Tkinter App")

    # Create a label widget
    lbl_hello = tk.Label(root, text="Hello, Tkinter!")
    lbl_hello.pack()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()