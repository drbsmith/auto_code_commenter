# staging-phaas-giving-api:ticket {#ticket}

# Ticket - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | ticket_id | | NO | varchar |  |
| 2 | organization_id | | NO | varchar |  |
| 3 | purchase_id | | NO | varchar | Foreign key to purchase table |
| 4 | user_id |  | NO | varchar | Mostly empty, or one of: genclient:event, genclient:giving, phaas-int-test, testUserId |
| 5 | amount | 0.00 | NO | decimal |  |
| 6 | ticket_type_id |  | NO | varchar |  |
| 7 | ticket_type_name |  | NO | varchar |  |
| 8 | ticket_details | | NO | text |  |
| 9 | source |  | NO | varchar |  |
| 10 | source_id |  | NO | varchar |  |
| 11 | source_name |  | NO | varchar |  |
| 12 | event_details | | NO | text |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | ticket_id | | NO | varchar | latin1_swedish_ci | varchar(255) | PRI |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 2 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 3 | purchase_id | | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 4 | user_id |  | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 5 | amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | def | staging-phaas-giving-api | ticket |
| 6 | ticket_type_id |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 7 | ticket_type_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 8 | ticket_details | | NO | text | latin1_swedish_ci | text |  |  | select |  |  | 65535 | 65535 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 9 | source |  | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 10 | source_id |  | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 11 | source_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | def | staging-phaas-giving-api | ticket |
| 12 | event_details | | NO | text | latin1_swedish_ci | text |  |  | select |  |  | 65535 | 65535 | latin1 | | | def | staging-phaas-giving-api | ticket |


@package staging-phaas-giving-api/public
