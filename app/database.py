
import csv
import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# Dataset configuration
DATA_MODE = os.getenv("DATA_MODE", "demo").strip().lower()

if DATA_MODE not in ("demo", "original"):
    raise ValueError(
        "Invalid DATA_MODE. Use 'demo' or 'original'."
    )

# Select the appropriate data directory
DATA_DIR = BASE_DIR / (
    "demo_data" if DATA_MODE == "demo" else "data"
)


def load_csv(filename: str) -> list[dict]:
    """
    Load a CSV file from the configured dataset directory.

    Args:
        filename: Name of the CSV file.

    Returns:
        List of dictionaries containing the CSV records.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    file_path = DATA_DIR / filename

    if not file_path.is_file():
        raise FileNotFoundError(
            f"CSV file not found: {file_path}"
        )

    with file_path.open(
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:
        return list(csv.DictReader(file))


def get_products() -> list[dict]:
    """Return all products from the selected dataset."""
    return load_csv(
        "desafio_tecnico_ai_eng - products.csv"
    )


def get_categories() -> list[dict]:
    """Return all product categories."""
    return load_csv(
        "desafio_tecnico_ai_eng - categories.csv"
    )


def get_orders() -> list[dict]:
    """Return all orders."""
    return load_csv(
        "desafio_tecnico_ai_eng - orders.csv"
    )


def get_order_items() -> list[dict]:
    """Return all order items."""
    return load_csv(
        "desafio_tecnico_ai_eng - order_items.csv"
    )


def get_customers() -> list[dict]:
    """Return all customers."""
    return load_csv(
        "desafio_tecnico_ai_eng - customers.csv"
    )


def get_promotions() -> list[dict]:
    """Return all promotions."""
    return load_csv(
        "desafio_tecnico_ai_eng - promotions.csv"
    )


if __name__ == "__main__":
    products = get_products()

    print("DATABASE TEST")
    print("-" * 50)
    print(f"Data mode: {DATA_MODE}")
    print(f"Data directory: {DATA_DIR}")
    print(f"Total products: {len(products)}")

    print("\nFirst 3 products:\n")

    for product in products[:3]:
        print(product)
        print("-" * 50)
