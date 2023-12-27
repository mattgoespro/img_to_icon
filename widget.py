from tkinter import ttk


def create_button(root, text, command):
    style = ttk.Style()
    style.configure(
        "Button.TButton",
        font=("Arial", 8),
        anchor="center",
    )
    button = ttk.Button(root, style="Button.TButton", text=text, command=command)
    return button


def create_frame(root, style=None):
    style = ttk.Style()
    style.configure("Frame.TFrame", relief="solid", padding=10, highlightthickness=0)
    frame = ttk.Frame(root, style=style or "Frame.TFrame", borderwidth=10)
    return frame


def create_label(root, text):
    style = ttk.Style()
    style.configure("SelectLabel.TLabel", font=("Arial", 10))
    label = ttk.Label(
        root,
        text=text,
        relief="flat",
        style="SelectLabel.TLabel",
        anchor="center",
    )
    return label
