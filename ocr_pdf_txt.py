import os
from pathlib import Path
from pdf2image import convert_from_path
import pytesseract

OCR_FOLDER = "ocr"
DATA_FOLDER = "data"

os.makedirs(DATA_FOLDER, exist_ok=True)

for pdf_file in Path(OCR_FOLDER).glob("*.pdf"):
    images = convert_from_path(str(pdf_file))
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    out_path = Path(DATA_FOLDER) / (pdf_file.stem + ".txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
print("OCR complete. Text files saved to 'data' folder.")
