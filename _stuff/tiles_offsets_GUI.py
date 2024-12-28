import tkinter as tk

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def generate_copy_text_equal(base, tile):
    return f"{base}({tile}) == {entry_value.get()}"

def generate_copy_text_not_equal(base, tile):
    return f"{base}({tile}) != {entry_value.get()}"

root = tk.Tk()
root.resizable(False, False)
root.title("Tile Selector")
root.configure(bg="lightgrey")
root.bind("<Escape>", lambda event: root.destroy())

entry_text = tk.StringVar(value="nearby_tile_water_class")
entry_widget = tk.Entry(root, textvariable=entry_text, font=("Tahoma", 12))
entry_widget.grid(row=0, column=0, columnspan=6, pady=(10, 5), padx=5, sticky="we")

entry_value = tk.StringVar(value="WATER_CLASS_NONE")
entry_widget = tk.Entry(root, textvariable=entry_value, font=("Tahoma", 12))
entry_widget.grid(row=1, column=0, columnspan=6, padx=5, sticky="we")

buttons = [
    {"text": "-1, -1", "row": 2, "column": 2, "span": 2},
    {"text": "0, -1",  "row": 3, "column": 1, "span": 2},
    {"text": "-1, 0",  "row": 3, "column": 3, "span": 2},
    {"text": "1, -1",  "row": 4, "column": 0, "span": 2},
    {"text": "0, 0",   "row": 4, "column": 2, "span": 2},
    {"text": "-1, 1",  "row": 4, "column": 4, "span": 2},
    {"text": "1, 0",   "row": 5, "column": 1, "span": 2},
    {"text": "0, 1",   "row": 5, "column": 3, "span": 2},
    {"text": "1, 1",   "row": 6, "column": 2, "span": 2},

    {"text": "-1, -1", "row": 7, "column": 2, "span": 2},
    {"text": "0, -1",  "row": 8, "column": 1, "span": 2},
    {"text": "-1, 0",  "row": 8, "column": 3, "span": 2},
    {"text": "1, -1",  "row": 9, "column": 0, "span": 2},
    {"text": "0, 0",   "row": 9, "column": 2, "span": 2},
    {"text": "-1, 1",  "row": 9, "column": 4, "span": 2},
    {"text": "1, 0",   "row": 10, "column": 1, "span": 2},
    {"text": "0, 1",   "row": 10, "column": 3, "span": 2},
    {"text": "1, 1",   "row": 11, "column": 2, "span": 2}
]

button_font = ("Helvetica", 14, "bold")

for button in buttons[0:9]:
    btn = tk.Button(root, text=button["text"], width=6, height=2, font=button_font, background="white",
                    command=lambda t=button["text"]: copy_to_clipboard(generate_copy_text_equal(entry_text.get(), t))  )
    btn.grid(row=button["row"], column=button["column"], columnspan=button["span"], padx=40, pady=5)
for button in buttons[9:]:
    btn = tk.Button(root, text=button["text"], width=6, height=2, font=button_font, background="white", fg="brown",
                    command=lambda t=button["text"]: copy_to_clipboard(generate_copy_text_not_equal(entry_text.get(), t))  )
    btn.grid(row=button["row"], column=button["column"], columnspan=button["span"], padx=40, pady=5)

root.mainloop()
