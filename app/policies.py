
import re
from pypdf import PdfReader

from database import DATA_DIR, DATA_MODE


def clean_text(text: str) -> str:
    """Normalize whitespace extracted from policy documents."""
    return re.sub(r"\s+", " ", text).strip()


def load_store_policies() -> list[dict]:
    """
    Load store policies from the configured dataset.

    Demo mode reads a fictional TXT document.
    Original mode reads the challenge PDF document.

    Returns:
        List of dictionaries containing page numbers
        and normalized policy text.
    """

    if DATA_MODE == "demo":
        policy_file = DATA_DIR / "demo_policies.txt"

        if not policy_file.is_file():
            raise FileNotFoundError(
                f"Demo policy file not found: {policy_file}"
            )

        text = clean_text(
            policy_file.read_text(encoding="utf-8")
        )

        if not text:
            raise ValueError("Demo policy file is empty.")

        return [{
            "page": 1,
            "text": text
        }]

    pdf_files = sorted(DATA_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            f"No policy PDF found in: {DATA_DIR}"
        )

    reader = PdfReader(str(pdf_files[0]))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = clean_text(page.extract_text() or "")

        if text:
            pages.append({
                "page": page_number,
                "text": text
            })

    if not pages:
        raise ValueError(
            "No readable policy text found in the PDF."
        )

    return pages


if __name__ == "__main__":
    policies = load_store_policies()

    print("STORE POLICIES")
    print("-" * 50)
    print(f"Data mode: {DATA_MODE}")
    print(f"Pages loaded: {len(policies)}")

    for page in policies:
        print(f"\nPage {page['page']}:")
        print(page["text"][:500])
        print("-" * 50)
