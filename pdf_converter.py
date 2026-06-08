import os
import subprocess
from tkinter import Tk, filedialog
from reportlab.pdfgen import canvas
from PIL import Image

root = Tk()
root.withdraw()

files = filedialog.askopenfilenames(
    title="Pilih File",
    filetypes=[
        ("Supported Files", "*.txt *.docx *.png *.jpg *.jpeg *.webp")
    ]
)

if not files:
    print("Tidak ada file dipilih")
    exit()

libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"

for file_path in files:

    file_name = os.path.basename(file_path)
    name_only = os.path.splitext(file_name)[0]
    ext = os.path.splitext(file_path)[1].lower()

    output_pdf = name_only + ".pdf"

    if ext == ".txt":

        c = canvas.Canvas(output_pdf)

        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        y = 800
        for line in lines:
            c.drawString(50, y, line.strip())
            y -= 20

        c.save()

        print(f"TXT → {output_pdf}")

    elif ext in [".png", ".jpg", ".jpeg", ".webp"]:

        img = Image.open(file_path)
        img = img.convert("RGB")
        img.save(output_pdf)

        print(f"IMG → {output_pdf}")

    elif ext == ".docx":

        subprocess.run([
            libreoffice_path,
            "--headless",
            "--convert-to",
            "pdf",
            file_path
        ])

        print(f"DOCX → {output_pdf}")

    else:
        print(f"Skip: {file_name}")