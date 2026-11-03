
import csv
from pathlib import Path

# Caminho para os arquivos do desafio
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_csv(filename):
    """Carrega um CSV e retorna uma lista de registros."""
    file_path = DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {file_path}"
        )

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_products():
    """Retorna os produtos cadastrados na loja."""
    return load_csv("desafio_tecnico_ai_eng - products.csv")


def get_categories():
    """Return all product categories."""
    return load_csv("desafio_tecnico_ai_eng - categories.csv")



if __name__ == "__main__":
    products = get_products()

    print(f"Total de produtos cadastrados: {len(products)}")
    print("\nPrimeiros 3 produtos:\n")

    for product in products[:3]:
        print(product)
        print("-" * 60)

def get_orders():
    return load_csv("desafio_tecnico_ai_eng - orders.csv")


def get_order_items():
    return load_csv("desafio_tecnico_ai_eng - order_items.csv")


def get_customers():
    return load_csv("desafio_tecnico_ai_eng - customers.csv")


def get_promotions():
    return load_csv("desafio_tecnico_ai_eng - promotions.csv")
