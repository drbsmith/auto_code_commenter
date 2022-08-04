# staging-phaas-giving-api:purchase {#purchase}

# Purchase - Table Description

TODOC:

## Columns

| | Column Name | Column Default | Is Nullable | Data Type | Notes |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar |  |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp |  |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp |  |
| 4 | organization_id | | NO | varchar |  |
| 5 | user_id |  | NO | varchar |  |
| 6 | total | 0.00 | NO | decimal |  |
| 7 | total_donations | 0.00 | NO | decimal |  |
| 8 | total_tickets | 0.00 | NO | decimal |  |
| 9 | total_paid | 0.00 | NO | decimal |  |
| 10 | total_card | 0.00 | NO | decimal |  |
| 11 | total_card_refunds_amount | 0.00 | NO | decimal |  |
| 12 | total_cash | 0.00 | NO | decimal |  |
| 13 | total_check | 0.00 | NO | decimal |  |
| 14 | total_other | 0.00 | NO | decimal |  |
| 15 | total_paid_donations | 0.00 | NO | decimal |  |
| 16 | total_paid_tickets | 0.00 | NO | decimal |  |
| 17 | total_covered_costs | 0.00 | NO | decimal |  |
| 18 | total_sales_tax | 0.00 | NO | decimal |  |
| 19 | total_fees_withheld_from_refunds_amount | 0.00 | NO | decimal |  |
| 20 | is_paid | 0 | NO | tinyint |  |
| 21 | donation_count | 0 | NO | int |  |
| 22 | ticket_count | 0 | NO | int |  |
| 23 | payment_count | 0 | NO | int |  |
| 24 | refunded_payment_count | 0 | NO | int |  |
| 25 | latest_refund_status |  | NO | varchar |  |
| 26 | latest_dispute_status |  | NO | varchar |  |
| 27 | org_name |  | NO | varchar |  |
| 28 | org_street |  | NO | varchar |  |
| 29 | org_city |  | NO | varchar |  |
| 30 | org_state |  | NO | varchar |  |
| 31 | org_zip |  | NO | varchar |  |
| 32 | org_phone |  | NO | varchar |  |
| 33 | org_website |  | NO | varchar |  |
| 34 | org_email |  | NO | varchar |  |
| 35 | org_logo_url |  | NO | varchar |  |
| 36 | org_tax_id |  | NO | varchar |  |
| 37 | receipt_details | | NO | text |  |
----
## Detailed Structure
| | Column Name | Column Default | Is Nullable | Data Type | Collation Name | Column Type | Column Key | Extra | Privileges | Column Comment | Generation Expression | Character Maximum Length | Character Octet Length | Character Set Name | Numeric Precision | Numeric Scale | Datetime Precision | Table Catalog | Table Schema | Table Name |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | id | | NO | varchar | latin1_swedish_ci | varchar(255) | PRI |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 2 | created | CURRENT_TIMESTAMP | NO | timestamp | | timestamp | MUL |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | purchase |
| 3 | updated | CURRENT_TIMESTAMP | NO | timestamp | | timestamp |  |  | select |  |  | | | | | | 0 | def | staging-phaas-giving-api | purchase |
| 4 | organization_id | | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 5 | user_id |  | NO | varchar | latin1_swedish_ci | varchar(50) | MUL |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 6 | total | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 7 | total_donations | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 8 | total_tickets | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 9 | total_paid | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 10 | total_card | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 11 | total_card_refunds_amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 12 | total_cash | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 13 | total_check | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 14 | total_other | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 15 | total_paid_donations | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 16 | total_paid_tickets | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 17 | total_covered_costs | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 18 | total_sales_tax | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 19 | total_fees_withheld_from_refunds_amount | 0.00 | NO | decimal | | decimal(10,2) |  |  | select |  |  | | | | 10 | 2 | | def | staging-phaas-giving-api | purchase |
| 20 | is_paid | 0 | NO | tinyint | | tinyint(1) |  |  | select |  |  | | | | 3 | 0 | | def | staging-phaas-giving-api | purchase |
| 21 | donation_count | 0 | NO | int | | int(11) |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | purchase |
| 22 | ticket_count | 0 | NO | int | | int(11) |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | purchase |
| 23 | payment_count | 0 | NO | int | | int(11) |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | purchase |
| 24 | refunded_payment_count | 0 | NO | int | | int(11) |  |  | select |  |  | | | | 10 | 0 | | def | staging-phaas-giving-api | purchase |
| 25 | latest_refund_status |  | NO | varchar | latin1_swedish_ci | varchar(20) |  |  | select |  |  | 20 | 20 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 26 | latest_dispute_status |  | NO | varchar | latin1_swedish_ci | varchar(50) |  |  | select |  |  | 50 | 50 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 27 | org_name |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 28 | org_street |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 29 | org_city |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 30 | org_state |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 31 | org_zip |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 32 | org_phone |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 33 | org_website |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 34 | org_email |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 35 | org_logo_url |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 36 | org_tax_id |  | NO | varchar | latin1_swedish_ci | varchar(255) |  |  | select |  |  | 255 | 255 | latin1 | | | | def | staging-phaas-giving-api | purchase |
| 37 | receipt_details | | NO | text | latin1_swedish_ci | text |  |  | select |  |  | 65535 | 65535 | latin1 | | | | def | staging-phaas-giving-api | purchase |


@package staging-phaas-giving-api/public
