# Schema Design

The dataset is split into several CSV files, so a relational database fits this project well.

## Main Tables

| Table | Purpose |
|---|---|
| customers | customer location and unique customer id |
| orders | order status and delivery dates |
| order_items | products and sellers inside each order |
| order_payments | payment method and payment value |
| order_reviews | customer review score and review text |
| products | product category and product attributes |
| sellers | seller location |
| geolocation | zip code level location data |
| product_category_translation | English names for product categories |

## Main Relationships

| Relationship | Type |
|---|---|
| customers to orders | one customer can have many orders |
| orders to order_items | one order can have many items |
| products to order_items | one product can appear in many order items |
| sellers to order_items | one seller can sell many order items |
| orders to order_payments | one order can have one or more payments |
| orders to order_reviews | one order can have review data |
| product_category_translation to products | category names can be matched for most products |

## Notes

- `geolocation` does not have a clean primary key in the raw dataset.
- Some date columns have missing values because not every order reached every delivery step.
- Review text fields have many missing values because customers can leave a score without writing a comment.
- `products.product_category_name` is not enforced as a foreign key because two categories are missing from the translation table.
