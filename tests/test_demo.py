import csv
from decimal import Decimal
from pathlib import Path
import pytest
pytestmark = pytest.mark.demo

DEMO_DIR = Path(__file__).resolve().parents[1] / "demo_data"


def read_demo_csv(filename):
    """Read records from a demonstration CSV file."""
    with (DEMO_DIR / filename).open(
        encoding="utf-8-sig",
        newline=""
    ) as file:
        return list(csv.DictReader(file))


def test_demo_products():
    """Verify the demonstration product catalog."""
    products = read_demo_csv(
        "desafio_tecnico_ai_eng - products.csv"
    )

    assert len(products) == 4
    assert all(product["product_id"] for product in products)


def test_demo_order_relationship():
    """Verify that demo orders reference valid customers."""
    orders = read_demo_csv(
        "desafio_tecnico_ai_eng - orders.csv"
    )
    customers = read_demo_csv(
        "desafio_tecnico_ai_eng - customers.csv"
    )

    customer_ids = {
        customer["customer_id"]
        for customer in customers
    }

    assert all(
        order["customer_id"] in customer_ids
        for order in orders
    )


def test_demo_promotion_calculation():
    """Verify the expected demo promotional price."""
    products = read_demo_csv(
        "desafio_tecnico_ai_eng - products.csv"
    )
    promotions = read_demo_csv(
        "desafio_tecnico_ai_eng - promotions.csv"
    )

    product_map = {
        product["product_id"]: product
        for product in products
    }

    promotion = promotions[0]
    product = product_map[promotion["product_id"]]

    original_price = Decimal(product["price_brl"])
    discount = Decimal(promotion["discount_percent"])

    final_price = (
        original_price
        * (Decimal("100") - discount)
        / Decimal("100")
    )

    assert final_price == Decimal("809.10")


def test_demo_policies():
    """Verify the demo policy document exists."""
    policy_file = DEMO_DIR / "demo_policies.txt"

    assert policy_file.exists()

    text = policy_file.read_text(encoding="utf-8")

    assert "DEMO STORE POLICIES" in text
    assert "Returns:" in text
