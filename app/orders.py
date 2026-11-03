
from database import (
    get_orders,
    get_order_items,
    get_customers,
    get_products,
)


def get_order_status(order_id, customer_email):
    """
    Return order information only when the
    provided email matches the order owner.
    """

    orders = get_orders()
    customers = get_customers()
    order_items = get_order_items()
    products = get_products()

    order = next(
        (
            item for item in orders
            if item["order_id"] == str(order_id)
        ),
        None
    )

    if order is None:
        return {
            "success": False,
            "message": "Order not found or customer not verified."
        }

    customer = next(
        (
            item for item in customers
            if item["customer_id"] == order["customer_id"]
        ),
        None
    )

    if (
        customer is None
        or customer["email"].strip().casefold()
        != customer_email.strip().casefold()
    ):
        return {
            "success": False,
            "message": "Order not found or customer not verified."
        }

    product_map = {
        product["product_id"]: product
        for product in products
    }

    items = []

    for item in order_items:
        if item["order_id"] != str(order_id):
            continue

        product = product_map.get(item["product_id"])

        items.append({
            "product": (
                product["name"]
                if product else "Unknown product"
            ),
            "quantity": int(item["quantity"])
        })

    return {
        "success": True,
        "order_id": order["order_id"],
        "status": order["status"],
        "order_date": order["order_date"],
        "total_brl": order["total_brl"],
        "tracking_code": order["tracking_code"],
        "estimated_delivery": order["estimated_delivery"],
        "items": items,
        "notice": (
            "Information retrieved from the provided "
            "dataset, not a live shipping service."
        )
    }



if __name__ == "__main__":
    import json

    result = get_order_status(
        order_id=1,
        customer_email="pedro.oliveira@jmail.com"
    )

    print(json.dumps(
        result,
        indent=2,
        ensure_ascii=False
    ))
