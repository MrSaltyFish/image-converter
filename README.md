# 🖼️ Image Converter (Tkinter + PIL)

A simple GUI-based image converter built with **Python**, **Tkinter**, and **Pillow (PIL)**.
This tool allows users to select an image and convert it into another format (PNG, JPEG, GIF, TIFF, WEBP) with just a few clicks.

---

## 🚀 Features

* ✅ User-friendly GUI (built with Tkinter)
* ✅ Supports multiple input formats: `.png`, `.jpg`, `.jpeg`, `.gif`, `.tiff`, `.webp`
* ✅ Convert to **PNG, JPEG, GIF, TIFF, WEBP**
* ✅ Automatically handles images with transparency when converting to formats that don’t support it (e.g., JPEG)
* ✅ Error handling with helpful dialogs

---

## 🛠️ Requirements

Make sure you have the following installed:

* Python **3.8+**
* Tkinter (comes pre-installed with Python)
* Pillow (`PIL`)

Install dependencies:

```bash
pip install pillow
```

---

## ▶️ How to Run

1. Clone or download this repository.
2. Save the script as `image_converter.py`.
3. Run:

   ```bash
   python image_converter.py
   ```

---

## 📖 Usage

1. Launch the app → window opens.
2. Select the **output format** you want (PNG, JPEG, GIF, TIFF, WEBP).
3. Click **"Select Image and Convert"**.
4. Choose an image file from your computer.
5. The converted image will be saved in the **same folder** as the original file, with the new extension.

---

## ⚡ Example

* Input file: `example.png`
* Convert to: **JPEG**
* Output file: `example.jpeg`

---

## 📝 Notes

* JPEG and WEBP don’t support transparency. The app will automatically convert images with alpha channels (RGBA, LA, P) to **RGB**.
* The converted file **replaces only the extension** (does not overwrite original).

---

## 📜 License

MIT License – free to use, modify, and distribute.
