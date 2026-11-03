
from decimal import Decimal
from database import get_products


def search_products(
    keyword=None,
    max_price=None,
    in_stock=True,
    limit=10,
    category_id=None
):
    """
    Search products by keyword, price, category and availability.
    """
    results = []

    for product in get_products():
        if product["status"].lower() != "active":
            continue

        if category_id is not None:
            if product["category_id"] != str(category_id):
                continue

        stock = int(product["stock_quantity"])
        price = Decimal(product["price_brl"])

        if in_stock and stock <= 0:
            continue

        if max_price is not None:
            if price > Decimal(str(max_price)):
                continue

        if keyword:
            searchable_text = (
                product["name"] + " " +
                product["description"]
            ).casefold()

            if keyword.casefold() not in searchable_text:
                continue

        results.append({
            "product_id": product["product_id"],
            "name": product["name"],
            "price_brl": float(price),
            "stock_quantity": stock,
            "description": product["description"]
        })

    results.sort(key=lambda item: item["price_brl"])

    return results[:limit]


if __name__ == "__main__":
    print("PRODUCT SEARCH TEST")
    print("-" * 50)

    products = search_products(
        max_price=1000,
        category_id=5,
        limit=100
    )

    for product in products:
        print(
            f"{product['name']} | "
            f"R$ {product['price_brl']:.2f} | "
            f"Stock: {product['stock_quantity']}"
        )

    print(f"\nProducts found: {len(products)}")
