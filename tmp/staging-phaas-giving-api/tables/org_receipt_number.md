# staging-phaas-giving-api:org_receipt_number {#org_receipt_number}

# Org Receipt Number - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | organization_id | | NO | varchar |  |
| 2 | next_receipt_number | 1 | YES | int |  |
| 3 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 4 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | org_receipt_number |
| 2 | next_receipt_number | 1 | YES | int | | int(10) unsigned |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | org_receipt_number |
| 3 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | org_receipt_number |
| 4 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | org_receipt_number |


@package staging-phaas-giving-api/public
