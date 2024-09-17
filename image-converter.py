import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image as PILImage

def convert_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.tiff;*.webp")])
    if not file_path:
        return

    new_format = format_var.get()
    if not new_format:
        messagebox.showerror("Error", "Please select a format to convert to.")
        return

    try:
        with PILImage.open(file_path) as img:
            if img.mode in ('RGBA', 'LA', 'P') and new_format in ('jpeg', 'webp'):
                img = img.convert('RGB')
            new_file_path = file_path.rsplit('.', 1)[0] + '.' + new_format
            img.save(new_file_path, format=new_format.upper())
            messagebox.showinfo("Success", f"Image converted to {new_format.upper()} and saved.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Image Converter")

tk.Label(root, text="Select the format to convert to:").pack(pady=5)

format_var = tk.StringVar()
tk.Radiobutton(root, text="PNG", variable=format_var, value="png").pack(anchor=tk.W)
tk.Radiobutton(root, text="JPEG", variable=format_var, value="jpeg").pack(anchor=tk.W)
tk.Radiobutton(root, text="GIF", variable=format_var, value="gif").pack(anchor=tk.W)
tk.Radiobutton(root, text="TIFF", variable=format_var, value="tiff").pack(anchor=tk.W)
tk.Radiobutton(root, text="WEBP", variable=format_var, value="webp").pack(anchor=tk.W)

tk.Button(root, text="Select Image and Convert", command=convert_image).pack(pady=10)

root.mainloop()
