# staging-phaas-giving-api:merchant_account_update {#merchant_account_update}

# Merchant Account Update - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar |  |
| 2 | merchant_type | | NO | varchar |  |
| 3 | external_id | | NO | varchar |  |
| 4 | status |  | NO | varchar |  |
| 5 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | merchant_account_update |
| 2 | merchant_type | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | merchant_account_update |
| 3 | external_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | def | staging-phaas-giving-api | merchant_account_update |
| 4 | status |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | def | staging-phaas-giving-api | merchant_account_update |
| 5 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | 0 | def | staging-phaas-giving-api | merchant_account_update |


@package staging-phaas-giving-api/public
