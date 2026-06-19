# Schema Checks

These checks help decide primary keys and foreign keys for the first schema draft.

| Check | Count |
| --- | --- |
| Duplicate customer_id values | 0 |
| Duplicate order_id values | 0 |
| Duplicate product_id values | 0 |
| Duplicate seller_id values | 0 |
| Duplicate order item keys | 0 |
| Duplicate payment keys | 0 |
| Duplicate review keys | 0 |
| Orders with customer_id not found in customers | 0 |
| Order items with order_id not found in orders | 0 |
| Order items with product_id not found in products | 0 |
| Order items with seller_id not found in sellers | 0 |
| Payments with order_id not found in orders | 0 |
| Reviews with order_id not found in orders | 0 |
| Product categories not found in translation table | 2 |

## Missing Product Categories

- pc_gamer
- portateis_cozinha_e_preparadores_de_alimentos
