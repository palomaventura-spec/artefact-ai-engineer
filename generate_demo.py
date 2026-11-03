
import csv
from pathlib import Path

DEMO_DIR = Path(__file__).resolve().parent / "demo_data"
DEMO_DIR.mkdir(exist_ok=True)


def save_csv(filename, headers, rows):
    path = DEMO_DIR / filename

    with path.open(
        "w", encoding="utf-8-sig", newline=""
    ) as file:
        writer = csv.DictWriter(
            file, fieldnames=headers
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created: {filename}")


save_csv(
    "desafio_tecnico_ai_eng - categories.csv",
    ["category_id", "name"],
    [
        {"category_id": "1", "name": "Guitarras"},
        {"category_id": "5", "name": "Violões"},
        {"category_id": "6", "name": "Ukuleles"},
    ]
)

save_csv(
    "desafio_tecnico_ai_eng - products.csv",
    [
        "product_id", "price_brl", "name",
        "category_id", "description",
        "stock_quantity", "status", "specs",
        "created_at"
    ],
    [
        {
            "product_id": "1001",
            "price_brl": "599.90",
            "name": "Demo Classic Guitar",
            "category_id": "5",
            "description": "Beginner nylon-string guitar.",
            "stock_quantity": "10",
            "status": "active",
            "specs": "{}",
            "created_at": "2026-01-10",
        },
        {
            "product_id": "1002",
            "price_brl": "899.00",
            "name": "Demo Acoustic Guitar",
            "category_id": "5",
            "description": "Steel-string acoustic guitar.",
            "stock_quantity": "5",
            "status": "active",
            "specs": "{}",
            "created_at": "2026-01-10",
        },
        {
            "product_id": "1003",
            "price_brl": "1200.00",
            "name": "Demo Electric Guitar",
            "category_id": "1",
            "description": "Electric guitar for practice.",
            "stock_quantity": "3",
            "status": "active",
            "specs": "{}",
            "created_at": "2026-01-10",
        },
        {
            "product_id": "1004",
            "price_brl": "350.00",
            "name": "Demo Concert Ukulele",
            "category_id": "6",
            "description": "Concert-size ukulele.",
            "stock_quantity": "4",
            "status": "active",
            "specs": "{}",
            "created_at": "2026-01-10",
        },
    ]
)

save_csv(
    "desafio_tecnico_ai_eng - customers.csv",
    ["customer_id", "name", "phone", "email", "city"],
    [
        {
            "customer_id": "1",
            "name": "Demo Customer",
            "phone": "(00) 00000-0000",
            "email": "customer@example.com",
            "city": "Demo City",
        }
    ]
)

save_csv(
    "desafio_tecnico_ai_eng - orders.csv",
    [
        "order_id", "customer_id", "order_date",
        "status", "total_brl", "payment_method",
        "tracking_code", "estimated_delivery", "notes"
    ],
    [
        {
            "order_id": "100",
            "customer_id": "1",
            "order_date": "2026-01-15",
            "status": "delivered",
            "total_brl": "599.90",
            "payment_method": "pix",
            "tracking_code": "DEMO123456",
            "estimated_delivery": "2026-01-22",
            "notes": "",
        }
    ]
)

save_csv(
    "desafio_tecnico_ai_eng - order_items.csv",
    ["order_id", "quantity", "product_id"],
    [
        {
            "order_id": "100",
            "quantity": "1",
            "product_id": "1001",
        }
    ]
)

save_csv(
    "desafio_tecnico_ai_eng - promotions.csv",
    [
        "promotion_id", "product_id",
        "discount_percent", "description",
        "is_active"
    ],
    [
        {
            "promotion_id": "1",
            "product_id": "1002",
            "discount_percent": "10",
            "description": "Demo Special Offer",
            "is_active": "1",
        }
    ]
)

policy_text = """
DEMO STORE POLICIES

This is a fictional demonstration policy document,
not the original Artefact challenge manual.

Payment: PIX and credit cards are accepted.

Returns: Demo online purchases may be returned
within 7 calendar days after delivery.

Shipping: Delivery estimates are illustrative.
Shipping status is not updated in real time.

Promotions: Promotional discounts cannot be
combined with other discounts.

Customer support: Unresolved requests should
be referred to a human representative.
"""

(DEMO_DIR / "demo_policies.txt").write_text(
    policy_text.strip(), encoding="utf-8"
)

print("\nDemo dataset created successfully!")
