import pytesseract
from PIL import Image
import pdf2image

class OCREngine:
    """
    OCR engine using Tesseract.
    Converts PDF → images → text.
    """

    def load(self, file_path: str):
        images = pdf2image.convert_from_path(file_path)
        results = []

        for idx, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            cleaned = text.strip()
            if cleaned:
                results.append({
                    "text": cleaned,
                    "source": "ocr",
                    "type": "ocr_page",
                    "metadata": {
                        "page_number": idx + 1
                    }
                })

        return results
