
import re
from pathlib import Path
from pypdf import PdfReader

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def clean_text(text):
    """Normalize whitespace extracted from PDF pages."""
    return re.sub(r"\s+", " ", text).strip()


def load_store_policies():
    """Extract and normalize store policy pages."""
    pdf_files = list(DATA_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError("No policy PDF found.")

    reader = PdfReader(str(pdf_files[0]))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = clean_text(page.extract_text() or "")

        if text:
            pages.append({
                "page": page_number,
                "text": text
            })

    return pages


if __name__ == "__main__":
    policies = load_store_policies()

    print(f"Pages loaded: {len(policies)}")

    for page in policies:
        print(
            f"\nPage {page['page']}: "
            f"{page['text'][:300]}"
        )
