# staging-phaas-giving-api:dispute {#dispute}

# Dispute - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | dispute_id | | NO | varchar |  |
| 2 | organization_id | | NO | varchar |  |
| 3 | purchase_id |  | NO | varchar |  |
| 4 | payment_id |  | NO | varchar |  |
| 5 | stripe_dispute_id | | NO | varchar |  |
| 6 | stripe_transfer_id | | NO | varchar |  |
| 7 | charge_id | | NO | varchar |  |
| 8 | amount | 0.00 | NO | decimal |  |
| 9 | domain |  | NO | varchar |  |
| 10 | source |  | NO | varchar |  |
| 11 | source_id |  | NO | varchar |  |
| 12 | source_name |  | NO | varchar |  |
| 13 | reason |  | NO | varchar |  |
| 14 | status |  | NO | varchar |  |
| 15 | is_inquiry | 0 | NO | tinyint |  |
| 16 | transfer_reversed | 0 | NO | tinyint |  |
| 17 | evidence_submitted | 0 | NO | tinyint |  |
| 18 | accepted | 0 | NO | tinyint |  |
| 19 | respond_by | CURRENT_TIMESTAMP | NO | timestamp |  |
| 20 | effective | | NO | timestamp |  |
| 21 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 22 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | dispute_id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 2 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 3 | purchase_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 4 | payment_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 5 | stripe_dispute_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 6 | stripe_transfer_id | | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 7 | charge_id | | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 8 | amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | dispute |
| 9 | domain |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 10 | source |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 11 | source_id |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 12 | source_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 13 | reason |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 14 | status |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | dispute |
| 15 | is_inquiry | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | dispute |
| 16 | transfer_reversed | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | dispute |
| 17 | evidence_submitted | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | dispute |
| 18 | accepted | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | dispute |
| 19 | respond_by | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | dispute |
| 20 | effective | | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | dispute |
| 21 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | dispute |
| 22 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | dispute |


@package staging-phaas-giving-api/public
