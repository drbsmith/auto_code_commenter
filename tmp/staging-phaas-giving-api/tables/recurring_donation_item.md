# staging-phaas-giving-api:recurring_donation_item {#recurring_donation_item}

# Recurring Donation Item - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | recurring_donation_item_id | | NO | varchar |  |
| 2 | recurring_donation_id | | NO | varchar |  |
| 3 | organization_id | | NO | varchar |  |
| 4 | donation_id |  | NO | varchar |  |
| 5 | is_done | 0 | NO | tinyint |  |
| 6 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 7 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | recurring_donation_item_id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation_item |
| 2 | recurring_donation_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation_item |
| 3 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation_item |
| 4 | donation_id |  | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation_item |
| 5 | is_done | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | recurring_donation_item |
| 6 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | recurring_donation_item |
| 7 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | recurring_donation_item |


@package staging-phaas-giving-api/public
