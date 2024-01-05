import tkinter as tk
from tkinter import filedialog, ttk

from PIL import Image, ImageFilter, ImageTk

import widget


class GUI:
    def __init__(self):
        self.root = self.create_root()

        self.file_path = tk.StringVar()
        self.output_name = tk.StringVar()
        self.anti_aliasing = tk.BooleanVar(value=True)

        (
            self.frame_left,
            self.file_select_label,
            self.open_button,
            self.anti_aliasing_checkbox,
        ) = self.create_left_frame(self.root)

        (
            self.frame_right,
            self.preview_frame,
            self.preview_label,
            self.img,
        ) = self.create_right_frame(self.root)

        self.convert_button = ttk.Button(
            self.root, text="Convert to ICO", command=self.convert_to_ico
        )
        self.convert_button.config(state="disabled")
        self.convert_button.pack(side="bottom", fill="x")
        self.frame_left.pack(side="left", fill="y", expand=True)
        self.frame_right.pack(side="right", fill="both", expand=True)

    def create_root(self):
        root = tk.Tk()
        root.title("Image to ICO Converter")
        root.configure(padx=50, pady=50)

        window_width = 600
        window_height = 400
        x_offset = int((root.winfo_screenwidth() / 2) - (window_width / 2))
        y_offset = int((root.winfo_screenheight() / 2) - (window_height / 2))

        root.geometry(f"600x400+{x_offset}+{y_offset}")
        return root

    def create_left_frame(self, window_root: tk.Tk):
        frame_left = widget.create_frame(window_root)

        (
            file_select_label,
            open_button,
            anti_aliasing_checkbox,
        ) = self.create_left_frame_content(frame_left)

        return frame_left, file_select_label, open_button, anti_aliasing_checkbox

    def create_left_frame_content(self, frame_root):
        # self.status_label = ttk.Label(self.frame_left, text="")
        # self.status_label.pack(side="left", fill="x")
        file_select_label = widget.create_label(frame_root, "Select an image:")
        file_select_label.grid(row=0, column=0)

        open_button = widget.create_button(
            frame_root,
            text="Open File",
            command=self.open_file_dialog,
        )
        open_button.grid(
            row=0,
            column=1,
        )

        anti_aliasing_style = widget.create_style("Checkbutton.TCheckbutton")
        anti_aliasing_checkbox = ttk.Checkbutton(
            frame_root,
            text="Anti-aliasing",
            variable=self.anti_aliasing,
            style=anti_aliasing_style,
        )
        anti_aliasing_checkbox.grid(row=1, column=0)

        return file_select_label, open_button, anti_aliasing_checkbox

    def create_right_frame(self, window_root: ttk.Frame):
        frame_right = widget.create_frame(window_root)

        preview_frame, preview_label, img = self.create_right_frame_content(frame_right)

        return frame_right, preview_frame, preview_label, img

    def create_right_frame_content(self, frame_root: ttk.Frame):
        preview_frame = widget.create_frame(
            frame_root,
        )
        preview_frame.pack(side="top", fill="both", expand=True)

        img = ttk.Label(preview_frame)
        img.pack(fill="both", expand=True)

        preview_label_style = ttk.Style()
        preview_label_style.configure(
            "PreviewLabel.TLabel",
            background="#dbdbdb",
            relief="flat",
            font=("Arial", 8),
        )
        preview_label = ttk.Label(
            preview_frame,
            style="PreviewLabel.TLabel",
            text="Select an image to preview",
            anchor="center",
        )
        preview_label.pack(side="bottom", fill="both", expand=True)

        return frame_root, preview_label, img

    def convert_to_ico(self):
        input_image_path = self.file_path.get()
        output_image_name = f"{self.file_path.get().split(".")[0]}.ico"

        if not input_image_path or not output_image_name:
            # self.status_label.config(
            #     text="Please select an input image and provide an output name."
            # )
            return

        try:
            img = Image.open(input_image_path)

            if self.anti_aliasing.get():
                img = img.filter(ImageFilter.SMOOTH_MORE)

            img.save(f"{output_image_name}.ico", format="ICO")

            # self.status_label.config(
            #     text=f"Conversion successful! Saved as {output_image_name}.ico"
            # )
        except IOError as error:
            # self.status_label.config(text=f"Error: {str(error)}")
            print(error)

    def open_file_dialog(self):
        self.file_path.set(
            filedialog.askopenfilename(
                filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
            )
        )

        # Clear the preview when there is no image
        if not self.file_path.get():
            self.img.config(image=None)
            self.preview_label.config(text="")
            return

        self.preview_label.config(text="Preview:")
        preview_image = Image.open(self.file_path.get())

        # Check if the image is in palette mode and convert it to RGBA if it contains transparency
        if preview_image.mode == "P" and "transparency" in preview_image.info:
            preview_image = preview_image.convert("RGBA")

        if self.anti_aliasing.get():
            preview_image = preview_image.filter(ImageFilter.SMOOTH_MORE)

        preview_image.thumbnail((200, 200))
        self.img.photo = ImageTk.PhotoImage(preview_image)
        self.img.config(image=self.img.photo)

        # enable the convert button
        self.convert_button.config(state="enabled")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = GUI()
    app.run()
