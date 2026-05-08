import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("280x380")
root.configure(bg="#000")

display = tk.StringVar(value="0")
tk.Label(root, textvariable=display, bg="#111",
         fg="#0ff", font=("Arial", 24, "bold"),
         height=2).pack(fill="x", padx=10, pady=10)

def click(btn):
    current = display.get()
    if btn == "C":
        display.set("0")
    elif btn == "⌫":
        display.set(current[:-1] if len(current) > 1 else "0")
    elif btn == "=":
        try:
            result = str(eval(current))
            display.set(result)
        except:
            display.set("Error")
    else:
        display.set(current + btn if current != "0" else btn)

def on_enter(e, btn_widget):
    btn_widget.config(cursor="hand2")
    original_bg = btn_widget.cget("bg")
    if original_bg == "#ff9f04":
        btn_widget.config(bg="#ffb033")
    elif original_bg == "#093de9":
        btn_widget.config(bg="#1a4dff")
    elif original_bg == "#8e03ca":
        btn_widget.config(bg="#a933d9")
    elif original_bg == "#222222":
        btn_widget.config(bg="#333333")

def on_leave(e, btn_widget):
    original_bg = btn_widget.cget("bg")
    if "#ffb033" in original_bg or original_bg == "#ffb033":
        btn_widget.config(bg="#ff9f04")
    elif "#1a4dff" in original_bg or original_bg == "#1a4dff":
        btn_widget.config(bg="#093de9")
    elif "#a933d9" in original_bg or original_bg == "#a933d9":
        btn_widget.config(bg="#8e03ca")
    elif "#333333" in original_bg or original_bg == "#333333":
        btn_widget.config(bg="#222222")

buttons = [
    ["C", "⌫", "", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["", "0", ".", "="]
]

for i, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#000")
    frame.pack(fill="x", padx=10, pady=2)
    for j, btn in enumerate(row):
        if btn == "":
            tk.Label(frame, text="", bg="#000", width=12, height=2).pack(side="left", padx=2)
            continue
        
        if btn in "+-*/=":
            color = "#e2ff04"
        elif btn == "C":
            color = "#093de9"
        elif btn == "⌫":
            color = "#8e03ca"
        else:
            color = "#222222"
            
        btn_widget = tk.Button(frame, text=btn, font=("Arial", 20, "bold"), bg=color, fg="white",
                              width=5, height=2, relief="flat", bd=0,
                              command=lambda b=btn: click(b))
        btn_widget.bind("<Enter>", lambda e, w=btn_widget: on_enter(e, w))
        btn_widget.bind("<Leave>", lambda e, w=btn_widget: on_leave(e, w))
        btn_widget.pack(side="left", padx=2)

root.mainloop()
