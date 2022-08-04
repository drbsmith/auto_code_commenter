# staging-phaas-giving-api:locker {#locker}

# Locker - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | name | | NO | varchar |  |
| 2 | number | | NO | int |  |
| 3 | expiration | | NO | bigint |  |
| 4 | completed | | NO | tinyint |  |
| 5 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | name | | NO | varchar | latin1_swedish_ci | varchar(255) | PRI |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | locker |
| 2 | number | | NO | int | | int(11) | PRI |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | locker |
| 3 | expiration | | NO | bigint | | bigint(20) |  |  | select |  |  | | | | 19 | 0 | | def | staging-phaas-giving-api | locker |
| 4 | completed | | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | locker |
| 5 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | locker |


@package staging-phaas-giving-api/public
