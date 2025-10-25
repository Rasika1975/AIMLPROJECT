import pytesseract
from PIL import Image
import re

# 👇 Add this line to set the Tesseract path manually
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """Extract text from an image file using pytesseract."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""

def extract_invoice_fields(text):
    """Extract common invoice fields from the extracted text."""
    vendor = re.search(r'(?<=Vendor:\s)(.*)', text)
    date = re.search(r'(?<=Date:\s)(.*)', text)
    invoice_number = re.search(r'(?<=Invoice Number:\s)(.*)', text)
    total_amount = re.search(r'(?<=Total Amount:\s)(.*)', text)

    return {
        "vendor": vendor.group(0) if vendor else None,
        "date": date.group(0) if date else None,
        "invoice_number": invoice_number.group(0) if invoice_number else None,
        "total_amount": total_amount.group(0) if total_amount else None,
    }
