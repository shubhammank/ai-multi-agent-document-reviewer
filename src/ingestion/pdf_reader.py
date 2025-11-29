import pypdf
from unstructured.partition.pdf import partition_pdf

class PDFReader:
    """
    Extracts text and layout-aware elements from PDFs.
    Combines:
    - Unstructured for high-fidelity layout text
    - PyPDF for fallback extraction
    """

    def __init__(self):
        pass

    def load(self, file_path: str):
        items = []

        # High-resolution parsing (Unstructured)
        try:
            elements = partition_pdf(
                filename=file_path,
                strategy="hi_res",
                infer_table_structure=True
            )

            for el in elements:
                text = getattr(el, "text", "").strip()
                if len(text) == 0:
                    continue

                items.append({
                    "text": text,
                    "source": "pdf",
                    "type": el.__class__.__name__,
                    "metadata": {
                        "page_number": getattr(el.metadata, "page_number", None),
                        "coordinates": getattr(el.metadata, "coordinates", None)
                    }
                })
        except Exception:
            pass

        # Fallback extraction using PyPDF
        try:
            pdf = pypdf.PdfReader(file_path)
            for i, page in enumerate(pdf.pages):
                raw = page.extract_text()
                if raw:
                    items.append({
                        "text": raw.strip(),
                        "source": "pdf_fallback",
                        "type": "page_text",
                        "metadata": {"page_number": i + 1}
                    })
        except:
            pass

        return items
