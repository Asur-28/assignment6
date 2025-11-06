# assignment6:


import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.set(result)
        except Exception as e:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = tk.StringVar()
entry_field = tk.Entry(root, textvar=entry, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry_field.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(btn_frame)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", padx=20, pady=10)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
