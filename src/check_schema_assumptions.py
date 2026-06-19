import pandas as pd

from config import RAW_DATA_DIR, PROJECT_ROOT


OUTPUT_PATH = PROJECT_ROOT / "docs" / "schema_checks.md"


def read_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / name)


def duplicate_key_count(df: pd.DataFrame, columns: list[str]) -> int:
    return int(df.duplicated(subset=columns).sum())


def missing_fk_count(child: pd.Series, parent: pd.Series) -> int:
    child_values = set(child.dropna())
    parent_values = set(parent.dropna())
    return len(child_values - parent_values)


def missing_values(child: pd.Series, parent: pd.Series) -> list[str]:
    child_values = set(child.dropna())
    parent_values = set(parent.dropna())
    return sorted(str(value) for value in child_values - parent_values)


def make_row(check: str, result: int) -> str:
    return f"| {check} | {result} |"


def main() -> None:
    customers = read_csv("olist_customers_dataset.csv")
    orders = read_csv("olist_orders_dataset.csv")
    order_items = read_csv("olist_order_items_dataset.csv")
    payments = read_csv("olist_order_payments_dataset.csv")
    reviews = read_csv("olist_order_reviews_dataset.csv")
    products = read_csv("olist_products_dataset.csv")
    sellers = read_csv("olist_sellers_dataset.csv")
    categories = read_csv("product_category_name_translation.csv")
    missing_categories = missing_values(
        products["product_category_name"],
        categories["product_category_name"],
    )

    rows = [
        make_row("Duplicate customer_id values", duplicate_key_count(customers, ["customer_id"])),
        make_row("Duplicate order_id values", duplicate_key_count(orders, ["order_id"])),
        make_row("Duplicate product_id values", duplicate_key_count(products, ["product_id"])),
        make_row("Duplicate seller_id values", duplicate_key_count(sellers, ["seller_id"])),
        make_row(
            "Duplicate order item keys",
            duplicate_key_count(order_items, ["order_id", "order_item_id"]),
        ),
        make_row(
            "Duplicate payment keys",
            duplicate_key_count(payments, ["order_id", "payment_sequential"]),
        ),
        make_row(
            "Duplicate review keys",
            duplicate_key_count(reviews, ["review_id", "order_id"]),
        ),
        make_row(
            "Orders with customer_id not found in customers",
            missing_fk_count(orders["customer_id"], customers["customer_id"]),
        ),
        make_row(
            "Order items with order_id not found in orders",
            missing_fk_count(order_items["order_id"], orders["order_id"]),
        ),
        make_row(
            "Order items with product_id not found in products",
            missing_fk_count(order_items["product_id"], products["product_id"]),
        ),
        make_row(
            "Order items with seller_id not found in sellers",
            missing_fk_count(order_items["seller_id"], sellers["seller_id"]),
        ),
        make_row(
            "Payments with order_id not found in orders",
            missing_fk_count(payments["order_id"], orders["order_id"]),
        ),
        make_row(
            "Reviews with order_id not found in orders",
            missing_fk_count(reviews["order_id"], orders["order_id"]),
        ),
        make_row(
            "Product categories not found in translation table",
            len(missing_categories),
        ),
    ]

    content = "\n".join(
        [
            "# Schema Checks",
            "",
            "These checks help decide primary keys and foreign keys for the first schema draft.",
            "",
            "| Check | Count |",
            "| --- | --- |",
            *rows,
            "",
            "## Missing Product Categories",
            "",
            "\n".join(f"- {category}" for category in missing_categories),
            "",
        ]
    )

    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(f"Schema checks written to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
