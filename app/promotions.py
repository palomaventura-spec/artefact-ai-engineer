
from decimal import Decimal
from database import get_promotions, get_products


def get_active_promotions():
    """Return active promotions with product details."""
    products = {
        product["product_id"]: product
        for product in get_products()
    }

    results = []

    for promotion in get_promotions():
        if promotion["is_active"] != "1":
            continue

        product = products.get(promotion["product_id"])

        if not product:
            continue

        if product["status"].lower() != "active":
            continue

        if int(product["stock_quantity"]) <= 0:
            continue

        original_price = Decimal(product["price_brl"])
        discount = Decimal(promotion["discount_percent"])

        discounted_price = (
            original_price * (Decimal("100") - discount)
            / Decimal("100")
        ).quantize(Decimal("0.01"))

        results.append({
            "product_id": product["product_id"],
            "product_name": product["name"],
            "original_price_brl": float(original_price),
            "discount_percent": float(discount),
            "discounted_price_brl": float(discounted_price),
            "promotion": promotion["description"],
        })

    return results


if __name__ == "__main__":
    import json

    promotions = get_active_promotions()

    print("ACTIVE PROMOTIONS")
    print("-" * 50)

    print(json.dumps(
        promotions,
        indent=2,
        ensure_ascii=False
    ))

    print(f"\nActive promotions found: {len(promotions)}")
