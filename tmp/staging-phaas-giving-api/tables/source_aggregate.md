# staging-phaas-giving-api:source_aggregate {#source_aggregate}

# Source Aggregate - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | source | | NO | varchar |  |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
| 4 | total_donated | 0 | NO | float |  |
| 5 | seed_amount | 0 | NO | float |  |
| 6 | total_external_donations | 0 | NO | float |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | source | | NO | varchar | latin1_swedish_ci | varchar(255) | PRI |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | source_aggregate |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | 0 | def | staging-phaas-giving-api | source_aggregate |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | 0 | def | staging-phaas-giving-api | source_aggregate |
| 4 | total_donated | 0 | NO | float | | float |  |  | select |  |  | | | | 12 | | def | staging-phaas-giving-api | source_aggregate |
| 5 | seed_amount | 0 | NO | float | | float |  |  | select |  |  | | | | 12 | | def | staging-phaas-giving-api | source_aggregate |
| 6 | total_external_donations | 0 | NO | float | | float |  |  | select |  |  | | | | 12 | | def | staging-phaas-giving-api | source_aggregate |


@package staging-phaas-giving-api/public
