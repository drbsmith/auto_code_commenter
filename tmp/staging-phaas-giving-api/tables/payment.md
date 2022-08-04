# staging-phaas-giving-api:payment {#payment}

# Payment - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar |  |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
| 4 | organization_id | | NO | varchar |  |
| 5 | user_id |  | NO | varchar |  |
| 6 | submitted_by_user_id |  | NO | varchar |  |
| 7 | merchant_account_id |  | NO | varchar |  |
| 8 | merchant_type |  | NO | varchar |  |
| 9 | purchase_id | | NO | varchar |  |
| 10 | partner_merchant_id |  | NO | varchar |  |
| 11 | source |  | NO | varchar |  |
| 12 | source_name |  | NO | varchar |  |
| 13 | source_id |  | NO | varchar |  |
| 14 | payment_type |  | NO | varchar |  |
| 15 | payment_type_other_notes |  | NO | varchar |  |
| 16 | amount | 0.00 | NO | decimal |  |
| 17 | fee_amount | 0.00 | NO | decimal |  |
| 18 | fee_cc_percent | 0.00 | NO | decimal |  |
| 19 | cc_percent_fee | 0.00 | NO | decimal |  |
| 20 | cc_flat_fee | 0.00 | NO | decimal |  |
| 21 | date | CURRENT_TIMESTAMP | NO | timestamp |  |
| 22 | card_last_four |  | NO | varchar |  |
| 23 | check_number |  | NO | varchar |  |
| 24 | payment_method |  | NO | varchar |  |
| 25 | stripe_customer_id |  | NO | varchar |  |
| 26 | transaction_id |  | NO | varchar |  |
| 27 | transaction_success | 0 | NO | tinyint |  |
| 28 | transaction_error | | NO | text |  |
| 29 | latest_refund_status |  | NO | varchar |  |
| 30 | latest_dispute_status |  | NO | varchar |  |
| 31 | payer_name |  | NO | varchar |  |
| 32 | payer_company_name |  | NO | varchar |  |
| 33 | payer_street |  | NO | varchar |  |
| 34 | payer_city |  | NO | varchar |  |
| 35 | payer_state |  | NO | varchar |  |
| 36 | payer_country | USA | NO | varchar |  |
| 37 | payer_zip |  | NO | varchar |  |
| 38 | payer_phone |  | NO | varchar |  |
| 39 | payer_email |  | NO | varchar |  |
| 40 | organization_fee_amount | 0.00 | NO | decimal |  |
| 41 | ticket_fee_amount_cents | 0 | NO | int |  |
| 42 | sales_tax_amount_cents | 0 | NO | int |  |
| 43 | is_known_settled | 0 | NO | tinyint |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar | latin1_swedish_ci | varchar(50) | PRI |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp | MUL |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | payment |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | payment |
| 4 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 5 | user_id |  | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 6 | submitted_by_user_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 7 | merchant_account_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 8 | merchant_type |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 9 | purchase_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 10 | partner_merchant_id |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 11 | source |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 12 | source_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 13 | source_id |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 14 | payment_type |  | NO | varchar | latin1_swedish_ci | varchar(20) | MUL |  | select |  |  | 20 | 20 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 15 | payment_type_other_notes |  | NO | varchar | latin1_swedish_ci | varchar(25) |  |  | select |  |  | 25 | 25 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 16 | amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | payment |
| 17 | fee_amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | payment |
| 18 | fee_cc_percent | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | payment |
| 19 | cc_percent_fee | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | payment |
| 20 | cc_flat_fee | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | payment |
| 21 | date | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | payment |
| 22 | card_last_four |  | NO | varchar | latin1_swedish_ci | varchar(4) |  |  | select |  |  | 4 | 4 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 23 | check_number |  | NO | varchar | latin1_swedish_ci | varchar(10) |  |  | select |  |  | 10 | 10 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 24 | payment_method |  | NO | varchar | latin1_swedish_ci | varchar(20) |  |  | select |  |  | 20 | 20 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 25 | stripe_customer_id |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 26 | transaction_id |  | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 27 | transaction_success | 0 | NO | tinyint | | tinyint(1) | MUL |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | payment |
| 28 | transaction_error | | NO | text | latin1_swedish_ci | text |  |  | select |  |  | 65535 | 65535 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 29 | latest_refund_status |  | NO | varchar | latin1_swedish_ci | varchar(20) |  |  | select |  |  | 20 | 20 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 30 | latest_dispute_status |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 31 | payer_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 32 | payer_company_name |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 33 | payer_street |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 34 | payer_city |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 35 | payer_state |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 36 | payer_country | USA | NO | varchar | latin1_swedish_ci | varchar(3) |  |  | select |  |  | 3 | 3 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 37 | payer_zip |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 38 | payer_phone |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 39 | payer_email |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | payment |
| 40 | organization_fee_amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | payment |
| 41 | ticket_fee_amount_cents | 0 | NO | int | | int(10) unsigned |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | payment |
| 42 | sales_tax_amount_cents | 0 | NO | int | | int(10) unsigned |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | payment |
| 43 | is_known_settled | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | payment |


@package staging-phaas-giving-api/public
