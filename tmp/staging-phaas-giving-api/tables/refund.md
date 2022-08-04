# staging-phaas-giving-api:refund {#refund}

# Refund - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | refund_id | | NO | varchar | Primary key |
| 2 | external_id |  | NO | varchar | looks like Stripe refund id, or an 8 digit number, mostly empty. |
| 3 | organization_id |  | NO | varchar |  |
| 4 | purchase_id |  | NO | varchar | Foreign key to Purchase table |
| 5 | payment_id |  | NO | varchar | Foreign key to Payment table |
| 6 | amount | 0.00 | NO | decimal |  |
| 7 | fees_withheld_amount | | NO | decimal |  |
| 8 | reason |  | NO | varchar |  |
| 9 | status |  | NO | varchar |  |
| 10 | refund_type |  | NO | varchar |  |
| 11 | initiated_by_user_id |  | NO | varchar | service that initiated the refund, one of: genclient:Giving |
| 12 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 13 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | refund_id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 2 | external_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 3 | organization_id |  | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 4 | purchase_id |  | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 5 | payment_id |  | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 6 | amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | refund |
| 7 | fees_withheld_amount | | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | refund |
| 8 | reason |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 9 | status |  | NO | varchar | latin1_swedish_ci | varchar(20) | MUL |  | select |  |  | 20 | 20 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 10 | refund_type |  | NO | varchar | latin1_swedish_ci | varchar(20) |  |  | select |  |  | 20 | 20 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 11 | initiated_by_user_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | refund |
| 12 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | refund |
| 13 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | refund |


@package staging-phaas-giving-api/public
