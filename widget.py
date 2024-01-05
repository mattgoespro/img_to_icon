from tkinter import ttk
from typing import Literal

WidgetStyle = Literal[
    "Button.TButton", "Frame.TFrame", "SelectLabel.TLabel", "Checkbutton.TCheckbutton"
]

style: ttk.Style = (
    ttk.Style()
    .configure(
        "Button.TButton",
        font=("Arial", 8),
        anchor="center",
    )
    .configure(
        "Frame.TFrame",
        relief="solid",
        padding=10,
        highlightthickness=0,
    )
    .configure(
        "Checkbutton.TCheckbutton",
        font=("Arial", 8),
    )
    .configure(
        "Label.TLabel",
        font=("Arial", 10),
    )
)


def create_button(root, text, command):
    button = ttk.Button(root, style=style, text=text, command=command)
    return button


def create_frame(root):
    print(style.element_names())
    frame = ttk.Frame(root, style=style.map("Frame.TFrame"), borderwidth=10)
    return frame


def create_label(root, text):
    label = ttk.Label(
        root,
        text=text,
        relief="flat",
        style=style.map("Label.TLabel"),
        anchor="center",
    )
    return label


def create_checkbutton(root, text):
    checkbutton = ttk.Checkbutton(
        root,
        text=text,
        style=style.map("Checkbutton.TCheckbutton"),
    )
    return checkbutton


def create_style(widget_style: WidgetStyle) -> ttk.Style:
    style = ttk.Style()

    match widget_style:
        case "Button.TButton":
            style.configure(
                widget_style,
                font=("Arial", 8),
                anchor="center",
            )
        case "Frame.TFrame":
            style.configure(
                widget_style,
                relief="solid",
                padding=10,
                highlightthickness=0,
            )
        case "SelectLabel.TLabel":
            style.configure(
                widget_style,
                font=("Arial", 10),
            )
        case "Checkbutton.TCheckbutton":
            style.configure(
                widget_style,
                font=("Arial", 8),
            )

    return style
