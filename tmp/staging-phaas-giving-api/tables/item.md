# staging-phaas-giving-api:item {#item}

# Item - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar | Primary key |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
| 4 | organization_id | | NO | varchar | Organization striping key |
| 5 | purchase_id | | NO | varchar | Foreign key to Purchase table |
| 6 | amount_cents | 0 | NO | int |  |
| 7 | tags |  | NO | varchar |  |
| 8 | type |  | NO | varchar | one of: t2g-donation, vevt-appeal, vevt-auction-lot, vevt-donation, vevt-fixed-price, vevt-impact, vevt-misc, vevt-raffle ,vevt-sales-tax, vevt-sponsor-attachment-event-sale, vevt-ticket |
| 9 | description |  | NO | varchar |  |
| 10 | source |  | NO | varchar |  |
| 11 | parent_source |  | NO | varchar |  |
| 12 | source_name |  | NO | varchar |  |
| 13 | source_data |  | NO | varchar |  |
| 14 | supporter_first_name |  | NO | varchar |  |
| 15 | supporter_last_name |  | NO | varchar |  |
| 16 | supporter_email |  | NO | varchar |  |
| 17 | supporter_mobile_phone |  | NO | varchar |  |
| 18 | greatfeats_participant_id |  | NO | varchar |  |
| 19 | details_json |  | NO | varchar |  |
| 20 | donation_id |  | NO | varchar | Foreign key to Donation table |
| 21 | value_cents | 0 | NO | int |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | item |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | item |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | item |
| 4 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | item |
| 5 | purchase_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | item |
| 6 | amount_cents | 0 | NO | int | | int(10) unsigned |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | item |
| 7 | tags |  | NO | varchar | latin1_swedish_ci | varchar(1000) |  |  | select |  |  | 1000 | 1000 | latin1 | | | | def | staging-phaas-giving-api | item |
| 8 | type |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | item |
| 9 | description |  | NO | varchar | latin1_swedish_ci | varchar(500) |  |  | select |  |  | 500 | 500 | latin1 | | | | def | staging-phaas-giving-api | item |
| 10 | source |  | NO | varchar | latin1_swedish_ci | varchar(255) | MUL |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | item |
| 11 | parent_source |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | item |
| 12 | source_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | item |
| 13 | source_data |  | NO | varchar | latin1_swedish_ci | varchar(1000) |  |  | select |  |  | 1000 | 1000 | latin1 | | | | def | staging-phaas-giving-api | item |
| 14 | supporter_first_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | item |
| 15 | supporter_last_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | item |
| 16 | supporter_email |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | item |
| 17 | supporter_mobile_phone |  | NO | varchar | latin1_swedish_ci | varchar(20) |  |  | select |  |  | 20 | 20 | latin1 | | | | def | staging-phaas-giving-api | item |
| 18 | greatfeats_participant_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | item |
| 19 | details_json |  | NO | varchar | latin1_swedish_ci | varchar(5000) |  |  | select |  |  | 5000 | 5000 | latin1 | | | | def | staging-phaas-giving-api | item |
| 20 | donation_id |  | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | item |
| 21 | value_cents | 0 | NO | int | | int(10) unsigned |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | item |


@package staging-phaas-giving-api/public
