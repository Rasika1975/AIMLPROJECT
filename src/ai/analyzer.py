# ai/analyzer.py
import re

def analyze_text(text):
    """
    Analyze extracted text from OCR and identify key insights.
    Example: find invoice fields or document type.
    """
    results = {}

    # Basic example: extract invoice-related info
    vendor = re.search(r'(?i)vendor[:\- ]+(.*)', text)
    date = re.search(r'(?i)date[:\- ]+(\S+)', text)
    total = re.search(r'(?i)total[:\- ]+([\d,\.]+)', text)

    results["vendor"] = vendor.group(1).strip() if vendor else None
    results["date"] = date.group(1).strip() if date else None
    results["total"] = total.group(1).strip() if total else None

    return results
