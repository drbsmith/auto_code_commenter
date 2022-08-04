# staging-phaas-giving-api:merchant_account {#merchant_account}

# Merchant Account - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | merchant_account_id | | NO | varchar |  |
| 2 | organization_id | | NO | varchar |  |
| 3 | merchant_type |  | NO | varchar |  |
| 4 | external_id |  | NO | varchar |  |
| 5 | stripe_connected_account_id |  | NO | varchar |  |
| 6 | merchant_data | | NO | text |  |
| 7 | name | | NO | varchar |  |
| 8 | status |  | NO | varchar |  |
| 9 | fake_payments | 0 | NO | tinyint |  |
| 10 | last_validated | CURRENT_TIMESTAMP | NO | datetime |  |
| 11 | created | CURRENT_TIMESTAMP | NO | datetime |  |
| 12 | updated | CURRENT_TIMESTAMP | NO | datetime |  |
| 13 | vpf_enabled | 0 | NO | tinyint |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | merchant_account_id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | merchant_account |
| 2 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | merchant_account |
| 3 | merchant_type |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | merchant_account |
| 4 | external_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | merchant_account |
| 5 | stripe_connected_account_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | merchant_account |
| 6 | merchant_data | | NO | text | latin1_swedish_ci | text |  |  | select |  |  | 65535 | 65535 | latin1 | | | | def | staging-phaas-giving-api | merchant_account |
| 7 | name | | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | merchant_account |
| 8 | status |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | merchant_account |
| 9 | fake_payments | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | merchant_account |
| 10 | last_validated | CURRENT_TIMESTAMP | NO | datetime | | datetime |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | merchant_account |
| 11 | created | CURRENT_TIMESTAMP | NO | datetime | | datetime |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | merchant_account |
| 12 | updated | CURRENT_TIMESTAMP | NO | datetime | | datetime |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | merchant_account |
| 13 | vpf_enabled | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | merchant_account |


@package staging-phaas-giving-api/public
