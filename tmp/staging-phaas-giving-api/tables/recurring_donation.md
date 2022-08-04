# staging-phaas-giving-api:recurring_donation {#recurring_donation}

# Recurring Donation - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | recurring_donation_id | | NO | varchar |  |
| 2 | recurring_donation_group | | NO | varchar |  |
| 3 | organization_id | | NO | varchar |  |
| 4 | merchant_account_id |  | NO | varchar |  |
| 5 | email |  | NO | varchar |  |
| 6 | first_name |  | NO | varchar |  |
| 7 | last_name |  | NO | varchar |  |
| 8 | recognition_name |  | NO | varchar |  |
| 9 | address_street |  | NO | varchar |  |
| 10 | address_city |  | NO | varchar |  |
| 11 | address_state |  | NO | varchar |  |
| 12 | address_country |  | NO | varchar |  |
| 13 | address_zip |  | NO | varchar |  |
| 14 | is_active | 0 | NO | tinyint |  |
| 15 | status |  | NO | varchar |  |
| 16 | failure_count | 0 | NO | int |  |
| 17 | domain |  | NO | varchar |  |
| 18 | source |  | NO | varchar |  |
| 19 | source_id |  | NO | varchar |  |
| 20 | source_name |  | NO | varchar |  |
| 21 | currency_code |  | NO | varchar |  |
| 22 | amount | 0.00 | NO | decimal |  |
| 23 | covered_cost_fee_amount_cents | 0 | NO | int |  |
| 24 | cover_costs | 0 | NO | tinyint |  |
| 25 | schedule | | YES | text |  |
| 26 | stripe_customer_id |  | NO | varchar |  |
| 27 | card_token |  | NO | varchar |  |
| 28 | card_type |  | NO | varchar |  |
| 29 | card_expiration_year | 0 | NO | int |  |
| 30 | card_expiration_month | 0 | NO | int |  |
| 31 | card_last_four |  | NO | varchar |  |
| 32 | next_charge_date | | YES | timestamp |  |
| 33 | group_created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 34 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 35 | ended | | YES | timestamp |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | recurring_donation_id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 2 | recurring_donation_group | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 3 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 4 | merchant_account_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 5 | email |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 6 | first_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 7 | last_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 8 | recognition_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 9 | address_street |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 10 | address_city |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 11 | address_state |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 12 | address_country |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 13 | address_zip |  | NO | varchar | latin1_swedish_ci | varchar(10) |  |  | select |  |  | 10 | 10 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 14 | is_active | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | recurring_donation |
| 15 | status |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 16 | failure_count | 0 | NO | int | | int(11) |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | recurring_donation |
| 17 | domain |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 18 | source |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 19 | source_id |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 20 | source_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 21 | currency_code |  | NO | varchar | latin1_swedish_ci | varchar(3) |  |  | select |  |  | 3 | 3 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 22 | amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | recurring_donation |
| 23 | covered_cost_fee_amount_cents | 0 | NO | int | | int(10) unsigned |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | recurring_donation |
| 24 | cover_costs | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | recurring_donation |
| 25 | schedule | | YES | text | latin1_swedish_ci | text |  |  | select |  |  | 65535 | 65535 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 26 | stripe_customer_id |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 27 | card_token |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 28 | card_type |  | NO | varchar | latin1_swedish_ci | varchar(20) |  |  | select |  |  | 20 | 20 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 29 | card_expiration_year | 0 | NO | int | | int(11) |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | recurring_donation |
| 30 | card_expiration_month | 0 | NO | int | | int(11) |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | recurring_donation |
| 31 | card_last_four |  | NO | varchar | latin1_swedish_ci | varchar(4) |  |  | select |  |  | 4 | 4 | latin1 | | | | def | staging-phaas-giving-api | recurring_donation |
| 32 | next_charge_date | | YES | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | recurring_donation |
| 33 | group_created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | recurring_donation |
| 34 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | recurring_donation |
| 35 | ended | | YES | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | recurring_donation |


@package staging-phaas-giving-api/public
