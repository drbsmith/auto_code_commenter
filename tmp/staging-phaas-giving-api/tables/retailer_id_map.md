# staging-phaas-giving-api:retailer_id_map {#retailer_id_map}

# Retailer Id Map - Table Description

TODOC:

## Columns

| | Column Name | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- |
| 1 | transaction_center_id | NO | varchar |  |
| 2 | processor_id | NO | varchar |  |
| 3 | retailer_id | NO | varchar |  |
----
## Detailed Structure
| | Column Name | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | transaction_center_id | NO | varchar | latin1_swedish_ci | varchar(10) | PRI |  | select |  |  | 10 | 10 | latin1 | def | staging-phaas-giving-api | retailer_id_map |
| 2 | processor_id | NO | varchar | latin1_swedish_ci | varchar(10) | PRI |  | select |  |  | 10 | 10 | latin1 | def | staging-phaas-giving-api | retailer_id_map |
| 3 | retailer_id | NO | varchar | latin1_swedish_ci | varchar(100) |  |  | select |  |  | 100 | 100 | latin1 | def | staging-phaas-giving-api | retailer_id_map |


@package staging-phaas-giving-api/public
