from typing import List, Dict
import pdfplumber

def load_pdf(path: str) -> List[Dict]:
    """
    Extracts texts from PDF and returns page-level dictionaries
    """
    pages = []
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text or len(text.strip()) == 0:
                continue
            if text and len(text.strip()) > 0:
                cleaned = normalize_text(text)
                pages.append({"page_num": i + 1, 
                              "text": cleaned,
                              "source": path.split("/")[-1]
                              })
    return pages

def normalize_text(text: str) -> str:
    """
    Cleans raw text. Removing empty lines and extra white space
    """
    lines = text.splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    return " ".join(lines)