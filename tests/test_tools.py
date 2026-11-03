
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "app"))

from tools import search_products
from orders import get_order_status
from promotions import get_active_promotions


def test_product_search():
    products = search_products(
        category_id=5,
        max_price=1000,
        limit=100
    )

    assert len(products) == 12

    for product in products:
        assert product["price_brl"] <= 1000
        assert product["stock_quantity"] > 0


def test_order_rejects_invalid_email():
    result = get_order_status(
        order_id=1,
        customer_email="invalid@example.com"
    )

    assert result["success"] is False


def test_order_accepts_matching_email():
    result = get_order_status(
        order_id=1,
        customer_email="pedro.oliveira@jmail.com"
    )

    assert result["success"] is True
    assert result["status"] == "delivered"
    assert result["order_id"] == "1"
    assert result["total_brl"] == "11499"


def test_active_promotions():
    promotions = get_active_promotions()

    assert len(promotions) == 4

    names = {
        item["product_name"]
        for item in promotions
    }

    assert "Kalani KAL-700T Tenor Natural" in names
    assert "Ohana CK-20 Concert Natural" in names


def test_discount_calculation():
    promotions = get_active_promotions()

    kalani = next(
        item for item in promotions
        if item["product_id"] == "127"
    )

    assert kalani["discount_percent"] == 10
    assert kalani["discounted_price_brl"] == 323.10
