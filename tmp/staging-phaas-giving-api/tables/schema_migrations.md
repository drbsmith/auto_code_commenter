# staging-phaas-giving-api:schema_migrations {#schema_migrations}

# Schema Migrations - Table Description

TODOC:

## Columns

| | Column Name | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- |
| 1 | version | NO | bigint |  |
| 2 | dirty | NO | tinyint |  |
----
## Detailed Structure
| | Column Name | Is Nullable | Data Type | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Numeric Precision | Numeric Scale | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | version | NO | bigint | bigint(20) | PRI |  | select |  |  | 19 | 0 | def | staging-phaas-giving-api | schema_migrations |
| 2 | dirty | NO | tinyint | tinyint(1) |  |  | select |  |  | 3 | 0 | def | staging-phaas-giving-api | schema_migrations |


@package staging-phaas-giving-api/public
