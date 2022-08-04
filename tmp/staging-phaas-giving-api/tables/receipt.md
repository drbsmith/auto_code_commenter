# staging-phaas-giving-api:receipt {#receipt}

# Receipt - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | receipt_id | | NO | varchar |  |
| 2 | organization_id | | NO | varchar |  |
| 3 | payment_id | | NO | varchar | Foreign key to Payment table |
| 4 | receipt_number | | NO | varchar |  |
| 5 | url | | NO | varchar |  |
| 6 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 7 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | receipt_id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | receipt |
| 2 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | receipt |
| 3 | payment_id | | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | receipt |
| 4 | receipt_number | | NO | varchar | latin1_swedish_ci | varchar(20) | MUL |  | select |  |  | 20 | 20 | latin1 | | def | staging-phaas-giving-api | receipt |
| 5 | url | | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | def | staging-phaas-giving-api | receipt |
| 6 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | 0 | def | staging-phaas-giving-api | receipt |
| 7 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | 0 | def | staging-phaas-giving-api | receipt |


@package staging-phaas-giving-api/public
